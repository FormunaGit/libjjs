from typing import Literal, TypedDict


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

#################################
Specials = Literal[
    "Limitless",
    "Combat Instincts",
    "Cleave",
    "Rhythm",
    "Door Guard",
    "Lurking Shadow",
    "Adaptation Wheel",
    "Self Transfiguration",
    "Convergence",
    "Boogie Woogie",
    "Fluttering Pounce",
    "Domain Amplification",
    "No Escape",
    "Mass BuildUp",
    "Incantation",
    "Rika",
    "Clairvoyance",
    "Energy Output",
    "Offload",
    "Acceleration",
    "Projection Sorcery",
    "Ratio Point",
    "Instant Transmission",
    "Helping Hand",
    "Flock",
    "Flower Field",
    "Restyle",
    "Earthen Insect Trance",
]

Effects = Literal[
    "Cancel",
    "Overlay",
    "Shake Light",
    "Clash",
    "Melee Trail",
    "Beams",
    "Wind Streak",
    "Star",
    "Mesh",
    "Light",
    "Billboard",
    "Wind Expand",
    "360 Wind",
    "Whirl Slash",
    "Camera",
    "Beam",
    "Circle Glow",
    "Flames",
    "Distortion",
    "Star Outline",
    "Afterimage2",
    "Field of View",
    "Cleave",
    "Cylinder",
    "Black Flash",
    "Energy Sparks",
    "Blood",
    "Cursed Energy",
    "Block",
    "Ring",
    "Sparks",
    "Mass Hit",
    "Burst",
    "Wedge",
    "Shake Heavy",
    "Slash",
    "Dismantle",
    "Afterimage",
    "Rough Energy",
    "Screen Color",
    "Sphere",
    "Weak Lightning",
    "Wind Ring",
    "Shine",
    "Shake Medium",
    "Visibility",
    "Glow",
]

AttackType = Literal[
    "Melee",
    "Bullet",
    "Explosion",
    "Swarm",
    "Domain",
]

States = Literal[
    "Stun",
    "IFrame",
    "NoM1",
    "NoSprint",
    "NoJump",
    "NoDash",
    "DisableChase",
    "Block",
    "DirectionLock",
    "SpeedMultiplier",
    "JumpMultiplier",
    "Scale",
]

EasingStyles = Literal[
    "Linear",
    "Sine",
    "Quad",
    "Cubic",
    "Exponential",
    "Back",
]

EasingDirections = Literal[
    "In",
    "Out",
    "InOut",
]

BodyParts = Literal[
    "HumanoidRootPart",
    "Head",
    "Torso",
    "Right Arm",
    "Left Arm",
    "Right Leg",
    "Left Leg",
]
