import libjjs

nodes = libjjs.Nodes()
conditions = libjjs.Conditions()

demo_character = libjjs.Character()

# Create a faster Todo special that only works when in the air
demo_character.create.skill(
    "Quick Swap",
    [
        nodes.SPECIAL(
            "Boogie Woogie",
            100,
            enable_variants=False,
        )
    ],
    kind="SPECIAL",
    cooldown=0,
    conditions=[conditions.IN_AIR()],
)

# A more complicated skill that uses variables and properties
ghost_duration = 0.2
repeat_count = 20

demo_character.create.skill(
    "Lagspike",
    [
        nodes.SET_COOLDOWN(ghost_duration * repeat_count),
        nodes.STATE("SpeedMultiplier", 2, ghost_duration * repeat_count),
        nodes.VISUAL("Field of View", 2, amount=160),
        nodes.VISUAL("Visibility", 0, opacity=1, alt_opacity=1),
        nodes.VISUAL("Afterimage2", ghost_duration),
        nodes.WAIT(ghost_duration),
        nodes.LOOP(2, repeat_count),
        nodes.VISUAL("Visibility", 0.1, opacity=1, alt_opacity=0),
        nodes.VISUAL(
            "Field of View", amount=0, easing_style="Sine", easing_direction="InOut"
        ),
    ],
    cooldown=1,
    properties=libjjs.Properties(no_stun=True),
)

print(demo_character.export_character_code())
