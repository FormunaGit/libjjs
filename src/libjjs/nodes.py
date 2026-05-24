from .types import (
    AttackType,
    BodyParts,
    EasingDirections,
    EasingStyles,
    Effects,
    Specials,
    States,
)


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
        spec: Specials = "Limitless",
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
        animation: list[float] = [1, 1],
        start: float = 0,
        end: float = 3.6,
        looped: bool = False,
        speed: float = 1,
        fade_in: float = 0.1,
        fade_out: float = 0,
        last_hit: float = -1,
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
        fade_in: float = 0,
        fade_out: float = 0,
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
            "FADE IN": fade_in,
            "FADE OUT": fade_out,
            "GLOBAL": global_,
            "PROJECTILE TAG": projectile_tag,
            "CANCEL": cancel,
        }

    def VELOCITY(
        self,
        force: list[float] = [0, 0, 0],
        time: int = 0,
        fade: bool = False,
        track: bool = False,
        last_hit: float = -1,
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
        position: list[float] = [0, 0, 4],
        rotation: list[float] = [0, 0, 0],
        size: list[float] = [6, 6, 6],
        stun: float = 1,
        stun_anim: bool = False,
        damage: int = 1,
        debree: int = 0,
        attack_type: AttackType = "Melee",
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
        ignore_wakeup: bool = False,
        preview: list[float] | None = None,
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
            "IGNORE WAKEUP": ignore_wakeup,
            "PREVIEW": preview if preview is not None else [0, 15],
        }

    def BRANCH(
        self,
        branch: str = "nil",
        random: str = "",
        last_hit: float = -1,
    ):
        return {
            "K_NAME": "BRANCH",
            "BRANCH": branch,
            "RANDOM": random,
            "LAST HIT": last_hit,
        }

    def VISUAL(
        self,
        effect: Effects = "Slash",
        time: float = 1,
        position: list[float] = [0, 0, 0],
        rotation: list[float] = [0, 0, 0],
        size: float = 1,
        color: str = "255, 255, 255",
        opacity: float = 0,
        alt_position: list[float] = [0, 0, 0],
        alt_rotation: list[float] = [0, 0, 0],
        alt_size: float = 1,
        alt_color: str = "255, 255, 255",
        alt_opacity: float = 0,
        texture: int = 2,
        body_part: BodyParts = "HumanoidRootPart",
        easing_style: EasingStyles = "Linear",
        easing_direction: EasingDirections = "In",
        projectile_tag: str = "nil",
        visual_tag: str = "nil",
        amount: int = 1,
        run_on_server: bool = False,
        relative_from_branch: bool = False,
        cancel_on_interrupt: bool = False,
        can_collide: bool = False,
        last_hit: float = -1,
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
        body_part: BodyParts = "HumanoidRootPart",
        body_part2: BodyParts = "HumanoidRootPart",
        time: float = 1,
        position: list[float] = [0, 0, 0],
        rotation: list[float] = [0, 0, 0],
        last_hit: float = 1,
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
        size: list[float] = [6, 6, 6],
        position: list[float] = [0, 0, 0],
        rotation: list[float] = [0, 0, 0],
        attack_type: AttackType = "Melee",
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
        aim_last_hit: float = -1,
        time: float = 1,
        ignore_wakeup: bool = True,
        debree: int = 0,
        cancel_enemy: bool = True,
        cache: bool = True,
        clear_knockback: bool = False,
    ):
        return {
            "K_NAME": "PROJECTILE",
            "DAMAGE": damage,
            "STUN": stun,
            "SPEED": speed,
            "SIZE": str(size).replace("[", "").replace("]", ""),
            "POSITION": str(position).replace("[", "").replace("]", ""),
            "ROTATION": str(rotation).replace("[", "").replace("]", ""),
            "ATTACK TYPE": attack_type,
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
            "CLEAR KNOCKBACK": clear_knockback,
        }

    def COUNTER(
        self,
        time: float = 1,
        stun: float = 1,
        attack_type: list[AttackType] = ["Melee"],
        branch: str = "nil",
        branch_target: str = "nil",
        cancel_enemy: bool = True,
        remove_on_hit: bool = True,
    ):
        return {
            "K_NAME": "COUNTER",
            "TIME": time,
            "STUN": stun,
            "ATTACK TYPE2": ",".join(attack_type),
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
        last_hit: float = -1,
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
        state: States = "Stun",
        value: int = 1,
        time: float = 1,
        disable_burst: bool = False,
        cancel_on_end: bool = False,
        branch: str = "nil",
        check: bool = False,
        last_hit: float = -1,
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
        position: list[float] = [0, 0, 0],
        rotation: list[float] = [0, 0, 0],
        projectile_tag: str = "nil",
        last_hit: float = -1,
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


class CustomNodes:
    def __init__(self):
        self._nodes = Nodes()

    def Domain(self):
        return self._nodes.VISUAL()
