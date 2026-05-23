import libjjs

demo_character = libjjs.Character()

# demo_character.create_raw_skill(
#     {
#         "COOLDOWN": 0,
#         "NAME": "Quick Swap",
#         "DATA": '{"Line":[{"SPEED":100,"K_NAME":"SPECIAL","SPEC":"Boogie Woogie","ENABLE VARIANTS":false}],"Prop":[],"Req":[]}',
#         "K_NAME": "SPECIAL",
#     },
# )

demo_character.create.special(
    "Quick Swap",
    '{"Line":[{"SPEED":100,"K_NAME":"SPECIAL","SPEC":"Boogie Woogie","ENABLE VARIANTS":false}],"Prop":[],"Req":[]}',
    0,
)

print(demo_character.export_character_code())
