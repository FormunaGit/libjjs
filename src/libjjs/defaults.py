from .nodes import Nodes


_nodes = Nodes()

_NODE_BUILDERS: dict[str, str] = {
    "WAIT": "WAIT",
    "SKILL": "SKILL",
    "SPECIAL": "SPECIAL",
    "ANIM": "ANIM",
    "SFX": "SOUND",
    "VELO": "VELOCITY",
    "CONNECT": "CONNECT",
    "HITBOX": "HITBOX",
    "BRANCH": "BRANCH",
    "VISUAL": "VISUAL",
    "GRAB": "GRAB",
    "PROJECTILE": "PROJECTILE",
    "COUNTER": "COUNTER",
    "TAG": "TAG",
    "STATE": "STATE",
    "TELEPORT": "TELEPORT",
    "ULTGIB": "ADD_AWAKENING",
    "HPGIB": "ADD_HEALTH",
    "EVGIB": "ADD_EVASION",
    "HITCNCL": "HIT_CANCEL",
    "SETCD": "SET_COOLDOWN",
    "LOOP": "LOOP",
}

NODE_DEFAULTS: dict[str, dict[str, object]] = {
    k: getattr(_nodes, v)() for k, v in _NODE_BUILDERS.items()
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
