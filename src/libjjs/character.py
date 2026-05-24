import base64
import json
from typing import Literal

import zstd

from .defaults import CONDITIONS_DEFAULTS, NODE_DEFAULTS, PROPERTIES_DEFAULTS
from .nodes import Nodes
from .types import BodyParts, GenericSkill
from .utils import Properties


class Character:
    def __init__(self, hide_character_extras: bool = False):
        self.raw: list[GenericSkill] = []
        self.create = self.CreateHelper(self)
        if hide_character_extras:
            self.create.skill(
                "init__HideCharacterExtras",
                [
                    # hide everything
                    Nodes().VISUAL("Visibility", opacity=1, alt_opacity=1),
                    # show limbs
                    *[
                        Nodes().VISUAL(
                            "Visibility", opacity=0, alt_opacity=0, body_part=limb
                        )
                        for limb in [
                            p for p in BodyParts.__args__ if p != "HumanoidRootPart"
                        ]
                    ],
                ],
                properties=Properties(
                    use_when_obtained=True, hide_in_awakening=True, hide_in_base=True
                ),
            )

    def create_raw_skill(self, skill_data: GenericSkill):
        self.raw.append(skill_data)

    def export_raw(self) -> str:
        return json.dumps(self.raw, separators=(",", ":"))

    def export_character_code(self) -> str:
        zstd_encoded = zstd.compress(self.export_raw().encode("utf-8"))
        base64_encoded = base64.b64encode(zstd_encoded)
        return base64_encoded.decode("utf-8")

    class CreateHelper:
        def __init__(self, character):
            self.character = character

        @staticmethod
        def _is_hidden(skill: GenericSkill) -> bool:
            try:
                data = json.loads(skill["DATA"])
                props = data.get("Prop", {})
                return props.get("AWK", False) or props.get("AWK2", False)
            except (json.JSONDecodeError, KeyError):
                return False

        @staticmethod
        def _build_data(
            line: list[dict],
            properties: dict | None = None,
            conditions: list[dict] | None = None,
            branches: dict[str, dict] | None = None,
        ) -> str:
            # remove default properties
            clean_props = {}
            if properties:
                for k, v in properties.items():
                    if k in PROPERTIES_DEFAULTS and PROPERTIES_DEFAULTS[k] == v:
                        continue
                    clean_props[k] = v

            # clean default values in nodes
            clean_line = []
            for node in line:
                k_name = node.get("K_NAME")
                if k_name in NODE_DEFAULTS:
                    defaults = NODE_DEFAULTS[k_name]
                    # keep K_NAME but slime out matching defaults
                    clean_node = {
                        k: v
                        for k, v in node.items()
                        if k == "K_NAME" or k not in defaults or defaults[k] != v
                    }
                    clean_line.append(clean_node)
                else:
                    clean_line.append(node)

            # clean conditions
            clean_conds = []
            if conditions:
                for cond in conditions:
                    c_name = cond.get("K_NAME")
                    if c_name in CONDITIONS_DEFAULTS:
                        defaults = CONDITIONS_DEFAULTS[c_name]
                        clean_cond = {
                            k: v
                            for k, v in cond.items()
                            if k == "K_NAME" or k not in defaults or defaults[k] != v
                        }
                        clean_conds.append(clean_cond)
                    else:
                        clean_conds.append(cond)

            # clean branches
            clean_branches = {}
            if branches:
                for branch_name, branch_data in branches.items():
                    branch_line = branch_data["nodes"]
                    branch_conds = branch_data.get("conditions")
                    clean_branch_line = []
                    for node in branch_line:
                        k_name = node.get("K_NAME")
                        if k_name in NODE_DEFAULTS:
                            defaults = NODE_DEFAULTS[k_name]
                            clean_node = {
                                k: v
                                for k, v in node.items()
                                if k == "K_NAME"
                                or k not in defaults
                                or defaults[k] != v
                            }
                            clean_branch_line.append(clean_node)
                        else:
                            clean_branch_line.append(node)

                    clean_branch_conds = []
                    if branch_conds:
                        for cond in branch_conds:
                            c_name = cond.get("K_NAME")
                            if c_name in CONDITIONS_DEFAULTS:
                                defaults = CONDITIONS_DEFAULTS[c_name]
                                clean_cond = {
                                    k: v
                                    for k, v in cond.items()
                                    if k == "K_NAME"
                                    or k not in defaults
                                    or defaults[k] != v
                                }
                                clean_branch_conds.append(clean_cond)
                            else:
                                clean_branch_conds.append(cond)

                    clean_branches[branch_name] = {
                        "Line": clean_branch_line,
                        "Req": clean_branch_conds,
                    }

            data = {
                "Line": clean_line,
                "Prop": clean_props,
                "Req": clean_conds,
            }
            if clean_branches:
                data["Branch"] = clean_branches

            return json.dumps(data, separators=(",", ":"))

        def skill(
            self,
            name: str,
            line: list[dict],
            kind: Literal["SKILL", "SPECIAL", "MELEE", "CHASE", "AWAKENING"] = "SKILL",
            cooldown: int | None = None,
            key: int | None = None,
            add: bool = False,
            duration: int | None = None,
            delay: int | None = None,
            properties: dict | None = None,
            conditions: list[dict] | None = None,
            branches: dict[str, dict] | None = None,
        ):
            data: dict[str, object] = {
                "NAME": name,
                "DATA": self._build_data(line, properties, conditions, branches),
                "K_NAME": kind,
            }
            if kind == "SKILL":
                if cooldown is not None:
                    data["COOLDOWN"] = cooldown
                data["KEY"] = (
                    key
                    if key is not None
                    else sum(
                        1
                        for s in self.character.raw
                        if s.get("K_NAME") == "SKILL" and not self._is_hidden(s)
                    )
                    + 1
                )
                if add:
                    data["ADD"] = add
            elif kind in ("SPECIAL", "CHASE"):
                if cooldown is not None:
                    data["COOLDOWN"] = cooldown
            elif kind == "AWAKENING":
                if duration is not None:
                    data["DURATION"] = duration
                if delay is not None:
                    data["DELAY"] = delay
            self.character.create_raw_skill(data)
