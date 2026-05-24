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
