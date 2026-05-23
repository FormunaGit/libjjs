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


class Character:
    def __init__(self):
        self.raw: list[GenericSkill] = []
        self.create = self.CreateHelper(self)

    # Creates a raw skill from the given data
    def create_raw_skill(self, skill_data: GenericSkill):
        self.raw.append(skill_data)

    # Exports the character data as a JSON string
    def export_raw(self) -> str:
        return json.dumps(self.raw, separators=(",", ":"))

    # Exports the character as a JJS character code
    def export_character_code(self) -> str:
        zstd_encoded = zstd.compress(self.export_raw().encode("utf-8"))
        base64_encoded = base64.b64encode(zstd_encoded)
        return base64_encoded.decode("utf-8")

    # Helper class for creating attacks
    class CreateHelper:
        def __init__(self, character):
            self.character = character

        @staticmethod
        def _build_data(
            line: list[dict], prop: list[dict] | None = None, req: list[dict] | None = None
        ) -> str:
            return json.dumps(
                {"Line": line, "Prop": prop or [], "Req": req or []},
                separators=(",", ":"),
            )

        # Adds a basic skill to the character
        def skill(
            self,
            name: str,
            line: list[dict],
            cooldown: int,
            key: int | None = None,
            add: bool = False,
            prop: list[dict] | None = None,
            req: list[dict] | None = None,
        ):
            skill_data: SkillType = {
                "NAME": name,
                "DATA": self._build_data(line, prop, req),
                "K_NAME": "SKILL",
                "COOLDOWN": cooldown,
                "KEY": key if key is not None else len(self.character.raw) + 1,
                "ADD": add,
            }
            self.character.create_raw_skill(skill_data)

        # Adds a special to the character
        def special(
            self,
            name: str,
            line: list[dict],
            cooldown: int,
            prop: list[dict] | None = None,
            req: list[dict] | None = None,
        ):
            skill_data: SpecialType = {
                "NAME": name,
                "DATA": self._build_data(line, prop, req),
                "K_NAME": "SPECIAL",
                "COOLDOWN": cooldown,
            }
            self.character.create_raw_skill(skill_data)

        # Adds a melee attack to the character
        def melee(
            self,
            name: str,
            line: list[dict],
            prop: list[dict] | None = None,
            req: list[dict] | None = None,
        ):
            skill_data: MeleeType = {
                "NAME": name,
                "DATA": self._build_data(line, prop, req),
                "K_NAME": "MELEE",
            }
            self.character.create_raw_skill(skill_data)

        # Adds a dash/chase move to the character
        def chase(
            self,
            name: str,
            line: list[dict],
            cooldown: int,
            prop: list[dict] | None = None,
            req: list[dict] | None = None,
        ):
            skill_data: ChaseType = {
                "NAME": name,
                "DATA": self._build_data(line, prop, req),
                "K_NAME": "CHASE",
                "COOLDOWN": cooldown,
            }
            self.character.create_raw_skill(skill_data)

        # Adds an awakening move to the character
        def awakening(
            self,
            name: str,
            line: list[dict],
            duration: int,
            delay: int,
            prop: list[dict] | None = None,
            req: list[dict] | None = None,
        ):
            skill_data: AwakeningType = {
                "NAME": name,
                "DATA": self._build_data(line, prop, req),
                "K_NAME": "AWAKENING",
                "DURATION": duration,
                "DELAY": delay,
            }
            self.character.create_raw_skill(skill_data)


# Helper class to hold all the nodes.


class Nodes:
    def __init__(self):
        pass

    def WAIT(self, TIME: int = 1):
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
            "FORCE": str(force),
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
            "POSITION": str(position),
            "ROTATION": str(rotation),
            "SIZE": str(size),
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
        size: list[int] = [1, 1, 1],
        color: str = "255, 255, 255",
        opacity: float = 0,
        alt_position: list[int] = [0, 0, 0],
        alt_rotation: list[int] = [0, 0, 0],
        alt_size: list[int] = [1, 1, 1],
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
            "POSITION": str(position),
            "ROTATION": str(rotation),
            "SIZE": str(size),
            "COLOR": color,
            "OPACITY": opacity,
            "ALT POSITION": str(alt_position),
            "ALT ROTATION": str(alt_rotation),
            "ALT SIZE": str(alt_size),
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
            "POSITION": str(position),
            "ROTATION": str(rotation),
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
            "SIZE": str(size),
            "POSITION": str(position),
            "ROTATION": str(rotation),
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
            "POSITION": str(position),
            "ROTATION": str(rotation),
            "PROJECTILE TAG": projectile_tag,
            "LAST HIT": last_hit,
            "RELATIVE FROM BRANCH": relative_from_branch,
        }

    def ADD_AWAKENING(
        self,
        amount: int = 5,
    ):
        return {"K_NAME": "ULTGIB", "AMOUNT": amount}

    def ADD_HEALTH(
        self,
        amount: int = 5,
    ):
        return {"K_NAME": "HPGIB", "AMOUNT": amount}

    def ADD_EVASION(
        self,
        amount: int = 5,
    ):
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
