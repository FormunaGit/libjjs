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
