import libjjs

nodes = libjjs.Nodes()
conditions = libjjs.Conditions()

demo_character = libjjs.Character(True)

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
ghost_duration = 0.3
repeat_count = 500

demo_character.create.skill(
    "Lagspike",
    [
        # init
        nodes.SET_COOLDOWN(ghost_duration * repeat_count),
        nodes.STATE("SpeedMultiplier", 2, ghost_duration * repeat_count),
        nodes.VISUAL("Field of View", 2, amount=160),
        nodes.VISUAL("Visibility", 0, opacity=1, alt_opacity=1),
        # the main loop
        nodes.STATE("Block", check=True, branch="blockstop"),
        nodes.VISUAL("Field of View", 0, amount=160),
        nodes.VISUAL("Afterimage2", ghost_duration),
        nodes.WAIT(ghost_duration),
        nodes.LOOP(4, repeat_count),
        # cleanup
        nodes.VISUAL("Visibility", 0.1, opacity=1, alt_opacity=0),
        nodes.VISUAL(
            "Field of View", amount=0, easing_style="Sine", easing_direction="InOut"
        ),
    ],
    cooldown=1,
    properties=libjjs.Properties(no_stun=True),
    branches={
        # force stop mechanic, block to reset effects
        "blockstop": libjjs.Branch(
            [
                nodes.STATE("SpeedMultiplier", time=0, value=1),
                nodes.VISUAL(
                    "Field of View",
                    amount=0,
                    easing_style="Sine",
                    easing_direction="InOut",
                ),
                nodes.VISUAL("Visibility", 0.1, opacity=1, alt_opacity=0),
                nodes.SET_COOLDOWN(0),
                nodes.VISUAL("Star", opacity=0.9, alt_opacity=1),
                nodes.VISUAL("Circle Glow", opacity=0, alt_opacity=1),
            ]
        )
    },
)

print(demo_character.export_character_code())
