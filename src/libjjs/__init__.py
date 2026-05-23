import base64
import json
from typing import Literal, TypedDict

import zstd


class BaseSkill(TypedDict):  # every skilltype has these fields
    NAME: str
    DATA: str


# ------------------------- #
class SkillType(BaseSkill):  # normal abilities
    K_NAME: Literal["SKILL"]
    COOLDOWN: int
    KEY: int
    ADD: bool


class MeleeType(BaseSkill):  # melee abilities
    K_NAME: Literal["MELEE"]


class ChaseType(BaseSkill):  # dash
    K_NAME: Literal["CHASE"]
    COOLDOWN: int


class AwakeningType(BaseSkill):  # g-move ability
    K_NAME: Literal["AWAKENING"]
    DURATION: int
    DELAY: int


class SpecialType(BaseSkill):  # r-move ability
    K_NAME: Literal["SPECIAL"]
    COOLDOWN: int


GenericSkill = (
    BaseSkill | SkillType | MeleeType | ChaseType | AwakeningType | SpecialType
)


NODE_DEFAULTS: dict[str, dict[str, object]] = {
    "WAIT": {"TIME": 1},
    "SKILL": {
        "MOVE": "Divergent Fist",
        "SPEED": 1,
        "START": 0,
        "HOLD FOR": 0,
        "ENABLE VARIANTS": True,
        "CANCEL LAST": False,
    },
    "SPECIAL": {
        "SPEC": "Limitless",
        "SPEED": 1,
        "ENABLE VARIANTS": True,
        "CANCEL LAST": False,
    },
    "ANIM": {
        "ANIM_USE": [1, 1],
        "PREVIEW": [0, 3.6],
        "SPEED": 1,
        "FADE IN": 0.1,
        "FADE OUT": 0,
        "LAST HIT": -1,
        "LOOPED": False,
    },
    "SFX": {
        "ID": 12222253,
        "START": 0,
        "END": 500,
        "SPEED": 1,
        "VOLUME": 1,
        "GLOBAL": False,
        "PROJECTILE TAG": "nil",
        "CANCEL": False,
    },
    "VELO": {
        "FORCE": "0, 0, 0",
        "TIME": 0,
        "FADE": False,
        "TRACK": False,
        "LAST HIT": -1,
        "RAGDOLL": 0,
        "TRUE RAGDOLL": False,
        "RELATIVE FROM BRANCH": False,
    },
    "CONNECT": {"SIGNAL": "Nothing", "TIME": 0.1, "RANGE": 99999999},
    "HITBOX": {
        "POSITION": "0, 0, 4",
        "ROTATION": "0, 0, 0",
        "SIZE": "6, 6, 6",
        "STUN": 1,
        "STUN ANIM": False,
        "DAMAGE": 1,
        "DEBREE": 0,
        "ATTACK TYPE": "Melee",
        "BLOCKABLE": True,
        "360 BLOCK": False,
        "CANCEL ENEMY": True,
        "CLEAR KNOCKBACK": False,
        "CAN KILL": True,
        "HIT RAGDOLL": False,
        "HIT USER": False,
        "SINGLE TARGET": True,
        "BRANCH": "nil",
        "BRANCH TARGET": "nil",
        "BRANCH FINISHER": "nil",
        "PROJECTILE TAG": "nil",
    },
    "BRANCH": {"BRANCH": "nil", "RANDOM": "", "LAST HIT": -1},
    "VISUAL": {
        "EFFECT": "Slash",
        "TIME": 1,
        "POSITION": "0, 0, 0",
        "ROTATION": "0, 0, 0",
        "SIZE": 1,
        "COLOR": "255, 255, 255",
        "OPACITY": 0,
        "ALT POSITION": "0, 0, 0",
        "ALT ROTATION": "0, 0, 0",
        "ALT SIZE": 1,
        "ALT COLOR": "255, 255, 255",
        "ALT OPACITY": 0,
        "TEXTURE": 2,
        "BODY PART": "HumanoidRootPart",
        "EASING STYLE": "Linear",
        "EASING DIRECTION": "In",
        "PROJECTILE TAG": "nil",
        "VISUAL TAG": "nil",
        "AMOUNT": 1,
        "RUN ON SERVER": False,
        "RELATIVE FROM BRANCH": False,
        "CANCEL ON INTERRUPT": False,
        "CAN COLLIDE": False,
        "LAST HIT": -1,
    },
    "GRAB": {
        "BODY PART": "HumanoidRootPart",
        "BODY PART2": "HumanoidRootPart",
        "TIME": 1,
        "POSITION": "0, 0, 0",
        "ROTATION": "0, 0, 0",
        "LAST HIT": 1,
    },
    "PROJECTILE": {
        "DAMAGE": 1,
        "STUN": 1,
        "SPEED": 1,
        "SIZE": "6, 6, 6",
        "POSITION": "0, 0, 0",
        "ROTATION": "0, 0, 0",
        "ATTACK TYPE": "Melee",
        "PROJECTILE TAG": "nil",
        "REFLECT COUNT": 0,
        "FILTER INTERVAL": 1,
        "BRANCH": "nil",
        "BRANCH TARGET": "nil",
        "BRANCH COLLIDED": "nil",
        "CONTINUE": False,
        "HIT RAGDOLL": False,
        "STUN ANIM": False,
        "HIT USER": False,
        "BLOCKABLE": True,
        "AIM LAST HIT": -1,
        "TIME": 1,
        "IGNORE WAKEUP": True,
        "DEBREE": 0,
        "CANCEL ENEMY": True,
        "CACHE": True,
    },
    "COUNTER": {
        "TIME": 1,
        "STUN": 1,
        "ATTACK TYPE2": "Melee",
        "BRANCH": "nil",
        "BRANCH TARGET": "nil",
        "CANCEL ENEMY": True,
        "REMOVE ON HIT": True,
    },
    "TAG": {
        "TAG": "nil",
        "VALUE": "nil",
        "TIME": 1,
        "ADD/REMOVE": True,
        "CHECK": False,
        "SET": True,
        "BRANCH": "nil",
        "LAST HIT": -1,
    },
    "STATE": {
        "STATE": "Stun",
        "VALUE": 1,
        "TIME": 1,
        "DISABLE BURST": False,
        "CANCEL ON END": False,
        "LAST HIT": -1,
        "BRANCH": "nil",
        "CHECK": False,
    },
    "TELEPORT": {
        "POSITION": "0, 0, 0",
        "ROTATION": "0, 0, 0",
        "PROJECTILE TAG": "nil",
        "LAST HIT": -1,
        "RELATIVE FROM BRANCH": False,
    },
    "ULTGIB": {"AMOUNT": 5},
    "HPGIB": {"AMOUNT": 5},
    "EVGIB": {"AMOUNT": 5},
    "HITCNCL": {"TIME": 1, "ENDLAG": 1, "BRANCH": "nil", "FLIP": False},
    "SETCD": {"KEY": -1, "COOLDOWN": -1},
    "LOOP": {"LOOP BACK": 1, "HOLD": False, "LOOP AMOUNT": 3},
}


PROPERTIES_DEFAULTS = {
    "DMG": 1,
    "KNOCK": 1,
    "INV": False,
    "REP": False,
    "REP2": False,
    "AWK": False,
    "KEEP": False,
    "AWK2": False,
    "USE": False,
    "USEONDEATH": False,
    "NOSTUN": False,
    "NOCANCEL": False,
    "VAR": "-",
}

CONDITIONS_DEFAULTS = {
    "AIR": {"FLIP": False},
    "JUMP": {"FLIP": False},
    "AIM": {"FLIP": False},
    "ULT": {"FLIP": False},
    "BAR": {"AMOUNT": 2, "FLIP": False},
    "DUR": {"DURABILITY": 1},
    "HP": {"AMOUNT": 1, "FLIP": False},
    "DOMAIN": {"FLIP": False},
    "HOLD": {"FLIP": False},
}


class Character:
    def __init__(self):
        self.raw: list[GenericSkill] = []
        self.create = self.CreateHelper(self)

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
                        1 for s in self.character.raw if s.get("K_NAME") == "SKILL"
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


class Nodes:
    def WAIT(self, TIME: float = 1):
        return {"K_NAME": "WAIT", "TIME": TIME}

    def SKILL(
        self,
        move_name: str = "Divergent Fist",
        speed: float = 1,
        cancel_last: bool = False,
        enable_variants: bool = True,
        hold_for: float = 0,
        start: float = 0,
    ):
        return {
            "K_NAME": "SKILL",
            "MOVE": move_name,
            "SPEED": speed,
            "START": start,
            "HOLD FOR": hold_for,
            "ENABLE VARIANTS": enable_variants,
            "CANCEL LAST": cancel_last,
        }

    def SPECIAL(
        self,
        spec: str = "Limitless",
        speed: float = 1,
        cancel_last: bool = False,
        enable_variants: bool = True,
    ):
        return {
            "K_NAME": "SPECIAL",
            "SPEC": spec,
            "SPEED": speed,
            "ENABLE VARIANTS": enable_variants,
            "CANCEL LAST": cancel_last,
        }

    def ANIM(
        self,
        animation: list[int] = [1, 1],
        start: float = 0,
        end: float = 3.6,
        looped: bool = False,
        speed: float = 1,
        fade_in: float = 0.1,
        fade_out: float = 0,
        last_hit: int = -1,
    ):
        # ANIM_USE seems to be in [character#, anim#] format, so this is gojo's hollowpurple
        # hollow purple is the default cuz its [1,1] i guess
        return {
            "K_NAME": "ANIM",
            "ANIM_USE": animation,
            "PREVIEW": [start, end],
            "SPEED": speed,
            "FADE IN": fade_in,
            "FADE OUT": fade_out,
            "LAST HIT": last_hit,
            "LOOPED": looped,
        }

    def SOUND(
        self,
        id: int = 12222253,
        speed: float = 1,
        volume: float = 1,
        start: float = 0,
        end: float = 500,
        cancel: bool = False,
        global_: bool = False,
        projectile_tag: str = "nil",
    ):
        return {
            "K_NAME": "SFX",
            "ID": id,
            "START": start,
            "END": end,
            "SPEED": speed,
            "VOLUME": volume,
            "GLOBAL": global_,
            "PROJECTILE TAG": projectile_tag,
            "CANCEL": cancel,
        }

    def VELOCITY(
        self,
        force: list[int] = [0, 0, 0],
        time: int = 0,
        fade: bool = False,
        track: bool = False,
        last_hit: int = -1,
        ragdoll: int = 0,
        true_ragdoll: bool = False,
        relative_from_branch: bool = False,
    ):
        return {
            "K_NAME": "VELO",
            "FORCE": str(force).replace("[", "").replace("]", ""),
            "TIME": time,
            "FADE": fade,
            "TRACK": track,
            "LAST HIT": last_hit,
            "RAGDOLL": ragdoll,
            "TRUE RAGDOLL": true_ragdoll,
            "RELATIVE FROM BRANCH": relative_from_branch,
        }

    def CONNECT(
        self,
        signal: str = "Nothing",
        time: float = 0.1,
        range: float = 99999999,
    ):
        return {"K_NAME": "CONNECT", "SIGNAL": signal, "TIME": time, "RANGE": range}

    def HITBOX(
        self,
        position: list[int] = [0, 0, 4],
        rotation: list[int] = [0, 0, 0],
        size: list[int] = [6, 6, 6],
        stun: float = 1,
        stun_anim: bool = False,
        damage: int = 1,
        debree: int = 0,
        attack_type: str = "Melee",  # CHOICE
        blockable: bool = True,
        blockable_360: bool = False,
        cancel_enemy: bool = True,
        clear_knockback: bool = False,
        can_kill: bool = True,
        hit_ragdoll: bool = False,
        hit_user: bool = False,
        single_target: bool = True,
        branch: str = "nil",
        branch_target: str = "nil",
        branch_finisher: str = "nil",
        projectile_tag: str = "nil",
    ):
        return {
            "K_NAME": "HITBOX",
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "SIZE": str(size).replace("[", "").replace("]", ""),
            "STUN": stun,
            "STUN ANIM": stun_anim,
            "DAMAGE": damage,
            "DEBREE": debree,
            "ATTACK TYPE": attack_type,
            "BLOCKABLE": blockable,
            "360 BLOCK": blockable_360,
            "CANCEL ENEMY": cancel_enemy,
            "CLEAR KNOCKBACK": clear_knockback,
            "CAN KILL": can_kill,
            "HIT RAGDOLL": hit_ragdoll,
            "HIT USER": hit_user,
            "SINGLE TARGET": single_target,
            "BRANCH": branch,
            "BRANCH TARGET": branch_target,
            "BRANCH FINISHER": branch_finisher,
            "PROJECTILE TAG": projectile_tag,
        }

    def BRANCH(
        self,
        branch: str = "nil",
        random: str = "",
        last_hit: int = -1,
    ):
        return {
            "K_NAME": "BRANCH",
            "BRANCH": branch,
            "RANDOM": random,
            "LAST HIT": last_hit,
        }

    def VISUAL(
        self,
        effect: str = "Slash",
        time: float = 1,
        position: list[int] = [0, 0, 0],
        rotation: list[int] = [0, 0, 0],
        size: float = 1,
        color: str = "255, 255, 255",
        opacity: float = 0,
        alt_position: list[int] = [0, 0, 0],
        alt_rotation: list[int] = [0, 0, 0],
        alt_size: float = 1,
        alt_color: str = "255, 255, 255",
        alt_opacity: float = 0,
        texture: int = 2,
        body_part: str = "HumanoidRootPart",
        easing_style: str = "Linear",
        easing_direction: str = "In",
        projectile_tag: str = "nil",
        visual_tag: str = "nil",
        amount: int = 1,
        run_on_server: bool = False,
        relative_from_branch: bool = False,
        cancel_on_interrupt: bool = False,
        can_collide: bool = False,
        last_hit: int = -1,
    ):
        return {
            "K_NAME": "VISUAL",
            "EFFECT": effect,
            "TIME": time,
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "SIZE": size,
            "COLOR": color,
            "OPACITY": opacity,
            "ALT POSITION": str(alt_position).replace("[", "").replace("]", ""),
            "ALT ROTATION": str(alt_rotation).replace("[", "").replace("]", ""),
            "ALT SIZE": alt_size,
            "ALT COLOR": alt_color,
            "ALT OPACITY": alt_opacity,
            "TEXTURE": texture,
            "BODY PART": body_part,
            "EASING STYLE": easing_style,
            "EASING DIRECTION": easing_direction,
            "PROJECTILE TAG": projectile_tag,
            "VISUAL TAG": visual_tag,
            "AMOUNT": amount,
            "RUN ON SERVER": run_on_server,
            "RELATIVE FROM BRANCH": relative_from_branch,
            "CANCEL ON INTERRUPT": cancel_on_interrupt,
            "CAN COLLIDE": can_collide,
            "LAST HIT": last_hit,
        }

    def GRAB(
        self,
        body_part: str = "HumanoidRootPart",
        body_part2: str = "HumanoidRootPart",
        time: float = 1,
        position: list[int] = [0, 0, 0],
        rotation: list[int] = [0, 0, 0],
        last_hit: int = 1,
    ):
        return {
            "K_NAME": "GRAB",
            "BODY PART": body_part,
            "BODY PART2": body_part2,
            "TIME": time,
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "LAST HIT": last_hit,
        }

    def PROJECTILE(
        self,
        damage: int = 1,
        stun: float = 1,
        speed: float = 1,
        size: list[int] = [6, 6, 6],
        position: list[int] = [0, 0, 0],
        rotation: list[int] = [0, 0, 0],
        attack_type: str = "Melee",  # CHOICE
        projectile_tag: str = "nil",
        reflect_count: int = 0,
        filter_interval: int = 1,
        branch: str = "nil",
        branch_target: str = "nil",
        branch_collided: str = "nil",
        continue_: bool = False,
        hit_ragdoll: bool = False,
        stun_anim: bool = False,
        hit_user: bool = False,
        blockable: bool = True,
        aim_last_hit: int = -1,
        time: float = 1,
        ignore_wakeup: bool = True,
        debree: int = 0,
        cancel_enemy: bool = True,
        cache: bool = True,
    ):
        return {
            "K_NAME": "PROJECTILE",
            "DAMAGE": damage,
            "STUN": stun,
            "SPEED": speed,
            "SIZE": str(size).replace("[", "").replace("]", ""),
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "ATTACK TYPE": attack_type,  # CHOICE
            "PROJECTILE TAG": projectile_tag,
            "REFLECT COUNT": reflect_count,
            "FILTER INTERVAL": filter_interval,
            "BRANCH": branch,
            "BRANCH TARGET": branch_target,
            "BRANCH COLLIDED": branch_collided,
            "CONTINUE": continue_,
            "HIT RAGDOLL": hit_ragdoll,
            "STUN ANIM": stun_anim,
            "HIT USER": hit_user,
            "BLOCKABLE": blockable,
            "AIM LAST HIT": aim_last_hit,
            "TIME": time,
            "IGNORE WAKEUP": ignore_wakeup,
            "DEBREE": debree,
            "CANCEL ENEMY": cancel_enemy,
            "CACHE": cache,
        }

    def COUNTER(
        self,
        time: float = 1,
        stun: float = 1,
        attack_type: str = "Melee",  # MULTICHOICE
        branch: str = "nil",
        branch_target: str = "nil",
        cancel_enemy: bool = True,
        remove_on_hit: bool = True,
    ):
        return {
            "K_NAME": "COUNTER",
            "TIME": time,
            "STUN": stun,
            "ATTACK TYPE2": attack_type,
            "BRANCH": branch,
            "BRANCH TARGET": branch_target,
            "CANCEL ENEMY": cancel_enemy,
            "REMOVE ON HIT": remove_on_hit,
        }

    def TAG(
        self,
        tag: str = "nil",
        value: str = "nil",
        time: float = 1,
        add_remove: bool = True,
        check: bool = False,
        set_value: bool = True,
        branch: str = "nil",
        last_hit: int = -1,
    ):
        return {
            "K_NAME": "TAG",
            "TAG": tag,
            "VALUE": value,
            "TIME": time,
            "ADD/REMOVE": add_remove,
            "CHECK": check,
            "SET": set_value,
            "BRANCH": branch,
            "LAST HIT": last_hit,
        }

    def STATE(
        self,
        state: str = "Stun",  # CHOICE
        value: int = 1,
        time: float = 1,
        disable_burst: bool = False,
        cancel_on_end: bool = False,
        branch: str = "nil",
        check: bool = False,
        last_hit: int = -1,
    ):
        return {
            "K_NAME": "STATE",
            "STATE": state,
            "VALUE": value,
            "TIME": time,
            "DISABLE BURST": disable_burst,
            "CANCEL ON END": cancel_on_end,
            "LAST HIT": last_hit,
            "BRANCH": branch,
            "CHECK": check,
        }

    def TELEPORT(
        self,
        position: list[int] = [0, 0, 0],
        rotation: list[int] = [0, 0, 0],
        projectile_tag: str = "nil",
        last_hit: int = -1,
        relative_from_branch: bool = False,
    ):
        return {
            "K_NAME": "TELEPORT",
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "PROJECTILE TAG": projectile_tag,
            "LAST HIT": last_hit,
            "RELATIVE FROM BRANCH": relative_from_branch,
        }

    def ADD_AWAKENING(self, amount: int = 5):
        return {"K_NAME": "ULTGIB", "AMOUNT": amount}

    def ADD_HEALTH(self, amount: int = 5):
        return {"K_NAME": "HPGIB", "AMOUNT": amount}

    def ADD_EVASION(self, amount: int = 5):
        return {"K_NAME": "EVGIB", "AMOUNT": amount}

    def HIT_CANCEL(
        self,
        time: float = 1,
        endlag: float = 1,
        branch: str = "nil",
        flip: bool = False,
    ):
        return {
            "K_NAME": "HITCNCL",
            "TIME": time,
            "ENDLAG": endlag,
            "BRANCH": branch,
            "FLIP": flip,
        }

    def SET_COOLDOWN(self, cooldown: float = -1, key: int = -1):
        return {"KEY": key, "K_NAME": "SETCD", "COOLDOWN": cooldown}

    def LOOP(self, loop_back: int = 1, loop_amount: int = 3, hold: bool = False):
        return {
            "LOOP BACK": loop_back,
            "HOLD": hold,
            "LOOP AMOUNT": loop_amount,
            "K_NAME": "LOOP",
        }


class Conditions:
    def IN_AIR(self, flip: bool = False) -> dict:
        return {"K_NAME": "AIR", "FLIP": flip}

    def IS_JUMPING(self, flip: bool = False) -> dict:
        return {"K_NAME": "JUMP", "FLIP": flip}

    def HAS_TARGET(self, flip: bool = False) -> dict:
        return {"K_NAME": "AIM", "FLIP": flip}

    def IS_AWAKENED(self, flip: bool = False) -> dict:
        return {"K_NAME": "ULT", "FLIP": flip}

    def HAS_AWK_BAR(self, amount: float = 2, flip: bool = False) -> dict:
        return {"K_NAME": "BAR", "AMOUNT": amount, "FLIP": flip}

    def DURABILITY(self, durability: float = 1) -> dict:
        return {"K_NAME": "DUR", "DURABILITY": durability}

    def HAS_HEALTH(self, amount: float = 1, flip: bool = False) -> dict:
        return {"K_NAME": "HP", "AMOUNT": amount, "FLIP": flip}

    def IS_IN_DOMAIN(self, flip: bool = False) -> dict:
        return {"K_NAME": "DOMAIN", "FLIP": flip}

    def IS_HOLDING(self, flip: bool = False) -> dict:
        return {"K_NAME": "HOLD", "FLIP": flip}


def Branch(
    nodes: list[dict],
    conditions: list[dict] | None = None,
) -> dict:
    return {"nodes": nodes, "conditions": conditions or []}


def Properties(
    damage_multiplier: float = 1,
    knockback_multiplier: float = 1,
    invincible: bool = False,
    replace_skill_if_occupied: bool = False,
    prevent_override: bool = False,
    hide_in_awakening: bool = False,
    keep_when_moveset_switches: bool = False,
    hide_in_base: bool = False,
    use_when_obtained: bool = False,
    use_on_death: bool = False,
    no_stun: bool = False,
    no_cancel: bool = False,
    variant_tag: str = "-",
) -> dict:
    return {
        "DMG": damage_multiplier,
        "KNOCK": knockback_multiplier,
        "INV": invincible,
        "REP": replace_skill_if_occupied,
        "REP2": prevent_override,
        "AWK": hide_in_awakening,
        "KEEP": keep_when_moveset_switches,
        "AWK2": hide_in_base,
        "USE": use_when_obtained,
        "USEONDEATH": use_on_death,
        "NOSTUN": no_stun,
        "NOCANCEL": no_cancel,
        "VAR": variant_tag,
    }
