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


class Animations:
    class HonoredOne:
        HollowPurple = ([1, 1],)
        InfiniteVoid = ([1, 2],)
        LapseBlue = ([1, 3],)
        LapseBlueMaximum = ([1, 4],)
        RapidPunches = ([1, 5],)
        ReversalRed = ([1, 6],)
        ReversalRedMaximum = ([1, 7],)
        Teleport = ([1, 8],)
        TwofoldHit = ([1, 9],)
        TwofoldKick = ([1, 10],)
        Ultimate = ([1, 11],)
        ShortVoid = ([1, 12],)
        Melee1 = ([1, 13],)
        Melee2 = ([1, 14],)
        Melee3 = ([1, 15],)
        Melee4 = ([1, 16],)
        Up = ([1, 17],)
        Down = ([1, 18],)
        Chase = ([1, 19],)

    class Vessel:
        CursedStrike = ([2, 1],)
        CursedStrikeHit = ([2, 2],)
        CrushingBlow = ([2, 3],)
        DivergentFist1 = ([2, 4],)
        DivergentFist2 = ([2, 5],)
        DivergentFist3 = ([2, 6],)
        DivergentFist4 = ([2, 7],)
        ManjiKick = ([2, 8],)
        ManjiKickHit = ([2, 9],)
        Cleave = ([2, 10],)
        Dismantle = ([2, 11],)
        FlameArrow = ([2, 12],)
        Rush = ([2, 13],)
        RushHit = ([2, 14],)
        MalevolentShrine = ([2, 15],)
        SlaughterDemon = ([2, 16],)
        Ultimate = ([2, 17],)
        UltimateEnchain = ([2, 18],)
        Instincts = ([2, 19],)
        Melee1 = ([2, 20],)
        Melee2 = ([2, 21],)
        Melee3 = ([2, 22],)
        Melee4 = ([2, 23],)

    class RestlessGambler:
        Counter = ([3, 1],)
        EnergySurge = ([3, 2],)
        FeverBuilder = ([3, 3],)
        IdleDeath = ([3, 4],)
        LuckyRushdown = ([3, 5],)
        LuckyVolley = ([3, 6],)
        OverLuck = ([3, 7],)
        ReserveBalls = ([3, 8],)
        Rhythm = ([3, 9],)
        RoughEnergy = ([3, 10],)
        ShutterDoors = ([3, 11],)
        Melee1 = ([3, 12],)
        Melee2 = ([3, 13],)
        Melee3 = ([3, 14],)
        Melee4 = ([3, 15],)
        Up = ([3, 16],)
        Chase = ([3, 17],)

    class TenShadows:
        DivineDog = ([4, 1],)
        GreatSerpent = ([4, 2],)
        MahoragaSummon = ([4, 3],)
        MahoragaUse = ([4, 4],)
        MaxElephant = ([4, 5],)
        Nue = ([4, 6],)
        RabbitEscape = ([4, 7],)
        Shadow = ([4, 8],)
        ShadowSwarm = ([4, 9],)
        ShadowSwarm1 = ([4, 10],)
        ShadowSwarm2 = ([4, 11],)
        ShadowSwarm3 = ([4, 12],)
        ShadowSwarmHit = ([4, 13],)
        ShadowSwarmRun = ([4, 14],)
        Ultimate = ([4, 15],)
        Melee1 = ([4, 16],)
        Melee2 = ([4, 17],)
        Melee3 = ([4, 18],)
        Melee4 = ([4, 19],)

    class Mahoraga:
        Adaptation = ([5, 1],)
        DivinePummel = ([5, 2],)
        Earthquake = ([5, 3],)
        GroundPitch = ([5, 4],)
        Parry = ([5, 5],)
        Takedown = ([5, 6],)
        WorldSlash = ([5, 7],)
        Melee1 = ([5, 8],)
        Melee2 = ([5, 9],)
        Melee3 = ([5, 10],)
        Melee4 = ([5, 11],)
        Up = ([5, 12],)
        Down = ([5, 13],)

    class Perfection:
        BodyRepel = ([6, 1],)
        CrushingRushdown = ([6, 2],)
        CrushingRushdownHit = ([6, 3],)
        DrillSplit = ([6, 4],)
        FaceBlitz = ([6, 5],)
        FocusStrike = ([6, 6],)
        ForceGrab = ([6, 7],)
        HeadSplitter = ([6, 8],)
        HeadSplitterHit = ([6, 9],)
        HeartPiercer = ([6, 10],)
        IdleTransfig = ([6, 11],)
        SelfPerfection = ([6, 12],)
        Soulfire = ([6, 13],)
        SpikeWrath = ([6, 14],)
        Stockpile = ([6, 15],)
        Ultimate = ([6, 16],)
        Ultimate2 = ([6, 17],)
        WideStrike = ([6, 18],)
        WideStrikeHit = ([6, 19],)
        ChaseClub = ([6, 20],)
        ChaseSword = ([6, 21],)
        ChaseArmor = ([6, 22],)
        Melee1 = ([6, 23],)
        Melee2 = ([6, 24],)
        Melee3 = ([6, 25],)
        Melee4 = ([6, 26],)
        Up = ([6, 27],)
        Club_Melee1 = ([6, 28],)
        Club_Melee2 = ([6, 29],)
        Club_Melee3 = ([6, 30],)
        Club_Melee4 = ([6, 31],)
        Down = ([6, 32],)
        Sword_Melee1 = ([6, 33],)
        Sword_Melee2 = ([6, 34],)
        Sword_Melee3 = ([6, 35],)
        Sword_Melee4 = ([6, 36],)

    class BloodManipulation:
        BloodEdge = ([7, 1],)
        BloodEdgeVictim = ([7, 2],)
        BloodRain = ([7, 3],)
        Convergence = ([7, 4],)
        PiercingBlood = ([7, 5],)
        PlasmaWave = ([7, 6],)
        RedScale = ([7, 7],)
        RedScaleAir = ([7, 8],)
        RedScaleVictim = ([7, 9],)
        SlicingExorcism = ([7, 10],)
        Supernova = ([7, 11],)
        SupernovaCounter = ([7, 12],)
        Ultimate = ([7, 13],)
        WingKing = ([7, 14],)
        WingKingVictim = ([7, 15],)
        Melee1 = ([7, 16],)
        Melee2 = ([7, 17],)
        Melee3 = ([7, 18],)
        Melee4 = ([7, 19],)

    class Switcher:
        Brothers = ([8, 1],)
        BruteForce = ([8, 2],)
        ClimaxJump = ([8, 3],)
        ClimaxJumpHit = ([8, 4],)
        Dreams = ([8, 5],)
        ElbowDrop = ([8, 6],)
        IdolDebut = ([8, 7],)
        PebbleThrow = ([8, 8],)
        PebbleThrowHit = ([8, 9],)
        SwiftKick = ([8, 10],)
        SwiftKickHit = ([8, 11],)
        Ultimate = ([8, 12],)
        UltimateSummon = ([8, 13],)
        JumpStart = ([8, 14],)
        JumpEnd = ([8, 15],)
        TakadaIdle = ([8, 16],)
        Emote = ([8, 17],)  # where does this even play
        Clap1 = ([8, 18],)
        Clap2 = ([8, 19],)
        Clap3 = ([8, 20],)
        Melee1 = ([8, 21],)
        Melee2 = ([8, 22],)
        Melee3 = ([8, 23],)
        Melee4 = ([8, 24],)

    class Locust:
        BlackMucus = ([9, 1],)
        BugFlight = ([9, 2],)
        Flight = ([9, 3],)
        FourArmed = ([9, 4],)
        SnapChomp = ([9, 5],)
        SnapChompHit = ([9, 6],)
        Ultimate = ([9, 7],)
        Melee1 = ([9, 8],)
        Melee2 = ([9, 9],)
        Melee3 = ([9, 10],)
        Melee4 = ([9, 11],)

    class DefenseAttorney:
        DeadlySentence = ([10, 1],)
        Execution = ([10, 2],)
        ExecutionHit1 = ([10, 3],)
        ExecutionHit2 = ([10, 4],)
        ExecutionHit3 = ([10, 5],)
        ExtendSwing = ([10, 6],)
        FinalJudgement = ([10, 7],)
        FinalJudgementHit = ([10, 8],)
        Grapple = ([10, 9],)
        JusticeServed = ([10, 10],)
        JusticeServedHit = ([10, 11],)
        TwirlingStrikes = ([10, 12],)
        Ultimate = ([10, 13],)
        Dodge1 = ([10, 14],)
        Dodge2 = ([10, 15],)
        Dodge3 = ([10, 16],)
        Dodge4 = ([10, 17],)
        Dodge5 = ([10, 18],)
        Verdict = ([10, 19],)
        TripleSentence = ([10, 20],)
        TripleSentenceHit = ([10, 21],)
        JudgeReach = ([10, 22],)
        JudgeReachHit = ([10, 23],)
        JudgeReachHit2 = ([10, 24],)
        GavelThrow = ([10, 25],)
        Melee1 = ([10, 26],)
        Melee2 = ([10, 27],)
        Melee3 = ([10, 28],)
        Melee4 = ([10, 29],)
        AltMelee1 = ([10, 30],)  # dunno what these are for
        AltMelee2 = ([10, 31],)
        AltMelee3 = ([10, 32],)
        AltMelee4 = ([10, 33],)
        Chase = ([10, 34],)
        JudgeReach2 = ([10, 35],)
        PressingCharges = ([10, 36],)

    class StarRage:
        GarudaRebound = ([11, 1],)
        GarudaStab = ([11, 2],)
        GarudaStabHit = ([11, 3],)
        MassBreaker = ([11, 4],)
        RisingStar = ([11, 5],)
        Ultimate = ([11, 6],)
        Melee1 = ([11, 7],)
        Melee2 = ([11, 8],)
        Melee3 = ([11, 9],)
        Melee4 = ([11, 10],)
        AltMelee1 = ([11, 30],)  # again, dunno what these are for
        AltMelee2 = ([11, 31],)
        AltMelee3 = ([11, 32],)
        AltMelee4 = ([11, 33],)

    class Heian:
        Chant = ([12, 1],)
        Dismantle = ([12, 2],)
        FlameArrow = ([12, 3],)
        Kamutoke = ([12, 4],)
        MalevolentShrine = ([12, 5],)
        WCS = ([12, 6],)

    class CursedPartners:
        ResoluteSlash = ([13, 1],)
        Revolve = ([13, 2],)
        SeveringPath = ([13, 3],)
        Sheath = ([13, 4],)
        Veilstep = ([13, 5],)
        VeilstepDive = ([13, 6],)
        SeveringPathAir = ([13, 7],)
        RevolveReaction = ([13, 8],)
        YutaBeam = ([13, 9],)
        Launch = ([13, 10],)
        Ultimate = ([13, 11],)
        JacobLadder = ([13, 12],)
        JacobLadderTarget = ([13, 13],)
        ElbowBeatdown = ([13, 14],)
        ElbowBeatdownTarget = ([13, 15],)
        RunSlash = ([13, 16],)
        CursedSpeech = ([13, 17],)
        Melee1 = ([13, 18],)
        Melee2 = ([13, 19],)
        Melee3 = ([13, 20],)
        Melee4 = ([13, 21],)
        Chase = ([13, 22],)
        Up = ([13, 23],)
        Down = ([13, 24],)
        SeveringSwing = ([13, 25],)
        Outburst = ([13, 26],)
        QuickdrawAerial = ([13, 27],)
        SecondWind = ([13, 28],)
        EnergyRipple = ([13, 29],)
        Ult_Melee1 = ([13, 30],)
        Ult_Melee2 = ([13, 31],)
        Ult_Melee3 = ([13, 32],)
        Ult_Melee4 = ([13, 33],)
        Ultimate2 = ([13, 34],)

    class AspiringMangaka:
        Despair = ([14, 1],)
        EyeCatch = ([14, 2],)
        ShutUp = ([14, 3],)
        ShutUpVictim = ([14, 4],)
        Sacrilegious = ([14, 5],)
        SacrilegiousHit = ([14, 6],)
        Ultimate = ([14, 7],)
        UltimateHit = ([14, 8],)
        UltimateAfter = ([14, 9],)
        Mark = ([14, 10],)
        Melee1 = ([14, 11],)
        Melee2 = ([14, 12],)
        Melee3 = ([14, 13],)
        Melee4 = ([14, 14],)
        Up = ([14, 15],)

    class PuppetMaster:
        BoostOnStart = ([15, 1],)
        BoostOnEnd = ([15, 2],)
        BoostOnTarget = ([15, 3],)
        UltraSpin = ([15, 4],)
        UltraSpinHit = ([15, 5],)
        UltraCannon = ([15, 6],)
        User = ([15, 7],)
        Grab = ([15, 8],)
        Kick = ([15, 9],)
        FunnyFall = ([15, 10],)
        SmoothLanding1 = ([15, 11],)
        SmoothLanding2 = ([15, 12],)
        BackSlide = ([15, 13],)
        SupermanLanding = ([15, 14],)
        ArmsFlyIn = ([15, 15],)
        BoostOn = ([15, 16],)
        BoostOnHit = ([15, 17],)
        HeatEmission = ([15, 18],)
        MiracleCannon = ([15, 19],)
        PigeonViola = ([15, 20],)
        AbsoluteDestructionOLD = ([15, 21],)
        GunShot = ([15, 22],)
        Kick = ([15, 23],)
        JumpCrouch = ([15, 24],)
        Stagger = ([15, 25],)
        Spawn = ([15, 26],)
        UltEnd = ([15, 27],)
        Melee1 = ([15, 28],)
        Melee2 = ([15, 29],)
        Melee3 = ([15, 30],)
        Melee4 = ([15, 31],)
        Ult_Melee1 = ([15, 32],)
        Ult_Melee2 = ([15, 33],)
        Ult_Melee3 = ([15, 34],)
        Ult_Melee4 = ([15, 35],)
        Up = ([15, 36],)
        AbsoluteDestruction = ([15, 37],)
        AbsoluteDestructionAir = ([15, 38],)

    class HeadOfTheHei:
        Bleedout = ([16, 1],)
        BleedoutHit = ([16, 2],)
        CursoryImpact = ([16, 3],)
        DecisiveStrike = ([16, 4],)
        DecisiveStrikeHit = ([16, 5],)
        Flicker = ([16, 6],)
        ProjectionBreaker = ([16, 7],)
        Ultimate = ([16, 8],)
        UltimateHit = ([16, 9],)
        TopSpeed = ([16, 10],)
        FlashFreezing = ([16, 11],)
        TendrilGrab = ([16, 12],)
        MoonPalace = ([16, 13],)
        Acceleration = ([16, 14],)
        Melee1 = ([16, 15],)
        Melee2 = ([16, 16],)
        Melee3 = ([16, 17],)
        Melee4 = ([16, 18],)
        Ult_Melee1 = ([16, 19],)
        Ult_Melee2 = ([16, 20],)
        Ult_Melee3 = ([16, 21],)
        Ult_Melee4 = ([16, 22],)

    class Salaryman:
        CleavingWhirlwind = ([17, 1],)
        SeveranceKick = ([17, 2],)
        BluntCut = ([17, 3],)
        Stabilize = ([17, 4],)
        StabilizeTarget = ([17, 5],)
        StabilizeTargetShort = ([17, 6],)
        RatioBreak1 = ([17, 7],)
        RatioBreak2 = ([17, 8],)
        RatioBreak3 = ([17, 9],)
        RatioBreak4 = ([17, 10],)
        RatioBreakStun = ([17, 11],)
        Ultimate = ([17, 12],)
        Melee1 = ([17, 13],)
        Melee2 = ([17, 14],)
        Melee3 = ([17, 15],)
        Melee4 = ([17, 16],)
        Up = ([17, 17],)
        Down = ([17, 18],)
        Ult_Melee1 = ([17, 19],)
        Ult_Melee2 = ([17, 20],)
        Ult_Melee3 = ([17, 21],)
        Ult_Melee4 = ([17, 22],)
        Sharpen = ([17, 23],)
        Interrogate = ([17, 24],)
        InterrogateHit = ([17, 25],)
        InterrogateFinalHit = ([17, 26],)
        Collapse = ([17, 27],)

    class MonkeyKid:
        Kamehameha = ([18, 1],)
        KiSpam = ([18, 2],)
        StaffExtend = ([18, 3],)
        StaffUppercut = ([18, 4],)
        Ultimate = ([18, 5],)
        Melee1 = ([18, 6],)
        Melee2 = ([18, 7],)
        Melee3 = ([18, 8],)
        Melee4 = ([18, 9],)

    class LuckyCoward:
        Ambush = ([19, 1],)
        Stinger = ([19, 2],)
        Backstab = ([19, 3],)
        BackstabTargetBack = ([19, 4],)
        BackstabTargetFront = ([19, 5],)
        Trip = ([19, 6],)
        CheapShot = ([19, 7],)
        DirtyPlay = ([19, 8],)
        JawbreakerHit = ([19, 9],)
        JarbreakerVictim = ([19, 10],)
        Melee1 = ([19, 11],)
        Melee2 = ([19, 12],)
        Melee3 = ([19, 13],)
        Melee4 = ([19, 14],)
        Melee4Victim = ([19, 15],)
        MeleeChase = ([19, 16],)
        SwordChase = ([19, 17],)
        Up = ([19, 18],)
        Down = ([19, 19],)
        Taunt1 = ([19, 20],)
        Taunt2 = ([19, 21],)
        Taunt3 = ([19, 22],)
        Taunt4 = ([19, 23],)

    class CrowCharmer:
        BirdCall = ([20, 1],)
        BirdHold = ([20, 2],)
        Bounding = ([20, 3],)
        BoundingVictim = ([20, 4],)
        Circling = ([20, 5],)
        CirclingVictim = ([20, 6],)
        CirclingVictimFinisher = ([20, 7],)
        Flock = ([20, 8],)
        GlidingFlight = ([20, 9],)
        GlidingFlightVictim = ([20, 10],)
        ImpetusUpdraft = ([20, 11],)
        Melee1 = ([20, 12],)
        Melee2 = ([20, 13],)
        Melee3 = ([20, 14],)
        Melee4 = ([20, 15],)
        Up = ([20, 16],)
        Down = ([20, 17],)
        Chase = ([20, 18],)

    class DisasterPlants:
        BudShot = ([21, 1],)
        DefenseResponse = ([21, 2],)
        FlowerField = ([21, 3],)
        RootSwarm = ([21, 4],)
        SurgingThorns = ([21, 5],)
        Melee1 = ([21, 6],)
        Melee2 = ([21, 7],)
        Melee3 = ([21, 8],)
        Melee4 = ([21, 9],)
        Chase = ([21, 10],)

    class TrueCannon:
        Appetizer = ([22, 1],)
        GraniteBlast = ([22, 2],)
        HadNoIdea = ([22, 3],)
        HadNoIdeaHit = ([22, 4],)
        Recovery = ([22, 5],)
        Recovery2 = ([22, 6],)
        SecondHelping = ([22, 7],)
        ThisDessert = ([22, 8],)
        ThisDessertHit = ([22, 9],)
        Ultimate = ([22, 10],)
        Unsatisfied = ([22, 11],)
        WhatAreYouAfter = ([22, 12],)
        WhatAreYouAfterHit = ([22, 13],)
        Chase = ([22, 14],)
        Melee3_2 = ([22, 15],)
        WerentInvited = ([22, 16],)
        Recovery3 = ([22, 17],)

    class BlackDeath:
        FesteringStrikes = ([23, 1],)
        Detach = ([23, 2],)
        Reattach = ([23, 3],)
        ChokeholdHit = ([23, 4],)
        ChokeholdVictim = ([23, 5],)
        EarthenTrance = ([23, 6],)
        RoachSwarm = ([23, 7],)
        Melee1 = ([23, 8],)
        Melee2 = ([23, 9],)
        Melee3 = ([23, 10],)
        Melee4 = ([23, 11],)
        Ult_Melee1 = ([23, 12],)
        Ult_Melee2 = ([23, 13],)
        Ult_Melee3 = ([23, 14],)
        Ult_Melee4 = ([23, 15],)
        Parthenogenesis = ([23, 16],)
        Eat = ([23, 17],)
        EatVictim = ([23, 18],)

    class Emotes:
        Sasage = ([24, 1],)
        Objection = ([24, 2],)
        Guy = ([24, 3],)
        Baldi = ([24, 4],)
        Legend = ([24, 5],)
        FingerWag = ([24, 6],)
        Briefcase = ([24, 7],)
        IrisOut2 = ([24, 8],)
        Pipebomb = ([24, 9],)
        ChaosEmerald = ([24, 10],)
        UFO = ([24, 11],)
        Potential3 = ([24, 12],)
        Greedler = ([24, 13],)
        Flop = ([24, 14],)
        Sunglasses = ([24, 15],)
        Doomer = ([24, 16],)
        Stance = ([24, 17],)
        WelcomeBack = ([24, 18],)
        Popipo = ([24, 19],)
        Aizo = ([24, 20],)
        Moneylender = ([24, 21],)
        Role = ([24, 22],)
        RatDance = ([24, 23],)
        Looping = ([24, 24],)
        Emote_1A = ([24, 25],)
        Unlicensed = ([24, 26],)
        Sturdy = ([24, 27],)
        LagTrain = ([24, 28],)
        OKTOBERFEST = ([24, 29],)
        Mystery = ([24, 30],)
        Gangdance = ([24, 31],)
        Birdbrain = ([24, 32],)
        Spin = ([24, 33],)
        PopStep = ([24, 34],)
        PonyStory = ([24, 35],)
        ElectroShuffle = ([24, 36],)
        Potential = ([24, 37],)
        SeatDepression = ([24, 38],)
        PeaceSign = ([24, 39],)
        Hopping = ([24, 40],)
        Role2 = ([24, 41],)
        SecretTechnique = ([24, 42],)
        Train = ([24, 43],)
        Delightful = ([24, 44],)
        NuhUh = ([24, 45],)
        Confess = ([24, 46],)
        Sprint = ([24, 47],)
        Specialist = ([24, 48],)
        HighFive = ([24, 49],)
        SimplyWalkAroundIt = ([24, 50],)
        Breakdance = ([24, 51],)
        Fumo = ([24, 52],)
        Gubby = ([24, 53],)
        SH3NANIGANS = ([24, 54],)
        Ship = ([24, 55],)
        Crazy = ([24, 56],)
        FusionDance = ([24, 57],)
        Tomadachi = ([24, 58],)
        NevadaMadness = ([24, 59],)
        When = ([24, 60],)
        ChestBump = ([24, 61],)
        Cardboard = ([24, 62],)
        Haircut = ([24, 63],)
        MochiMaker = ([24, 64],)
        Sit2 = ([24, 65],)
        ShubaDuck = ([24, 66],)
        Unlicensed2 = ([24, 67],)
        Piano = ([24, 68],)
        Kawaii = ([24, 69],)
        Homelander = ([24, 70],)
        Yeah = ([24, 71],)
        Broom = ([24, 72],)
        Wonderland = ([24, 73],)
        Kikifuku = ([24, 74],)
        MESMERIZED = ([24, 75],)
        Cookie = ([24, 76],)
        Facepalm = ([24, 77],)
        DeadOrAlive = ([24, 78],)
        Mannrobics = ([24, 79],)
        Neurotoxin = ([24, 80],)
        Strech2 = ([24, 81],)
        Challenger = ([24, 82],)
        Unlucky = ([24, 83],)
        Sneeze = ([24, 84],)
        Brain = ([24, 85],)
        Mockery = ([24, 86],)
        Throne = ([24, 87],)
        DieOfDeath = ([24, 88],)
        Modulo = ([24, 89],)
        Oddloop = ([24, 90],)
        Mechanism = ([24, 91],)
        ShowMeYaMoves = ([24, 92],)
        Paradise2 = ([24, 93],)
        Reader = ([24, 94],)
        Watashi = ([24, 95],)
        Split = ([24, 96],)
        CookingGranny = ([24, 97],)
        IrisOut = ([24, 98],)
        Trumpet = ([24, 99],)
        Bow = ([24, 100],)
        Power = ([24, 101],)
        Drums = ([24, 102],)
        Chill = ([24, 103],)
        Helicopter = ([24, 104],)
        Chill2 = ([24, 105],)
        HowTzeWasMoving = ([24, 106],)
        Miko = ([24, 107],)
        MirrorWorld = ([24, 108],)
        Lethal = ([24, 109],)
        Drag = ([24, 110],)
        Killbind = ([24, 111],)
        SpareChange = ([24, 112],)
        Coinflip = ([24, 113],)
        More = ([24, 114],)
        Clap = ([24, 115],)
        Stylish = ([24, 116],)
        Unlicensed3 = ([24, 117],)
        Message = ([24, 118],)
        Thunder = ([24, 119],)
        Heart = ([24, 120],)
        Winner = ([24, 121],)
        Grillify = ([24, 122],)
        Mozzarella = ([24, 123],)
        Rainwalk = ([24, 124],)
        Jiggy = ([24, 125],)
        SwordSurfing = ([24, 126],)
        BubbleBlower = ([24, 127],)
        VirtualInsanity = ([24, 128],)
        MissMe = ([24, 129],)
        Broke = ([24, 130],)
        KazotskyKick = ([24, 131],)
        Menacing = ([24, 132],)
        Selfie = ([24, 133],)
        Caramelldansen = ([24, 134],)
        ImOld = ([24, 135],)
        AuraMonster = ([24, 136],)
        Heart111 = ([24, 137],)
        EggheadsEndeavour = ([24, 138],)
        Provocation = ([24, 139],)
        DevilHunter = ([24, 140],)
        Superstar1 = ([24, 141],)
        LowCortisol = ([24, 142],)
        Flow = ([24, 143],)
        Score = ([24, 144],)
        ItsGoingDown = ([24, 145],)
        GroundDrone = ([24, 146],)
        Update = ([24, 147],)
        Roach = ([24, 148],)
        Warfstache = ([24, 149],)
        Meditation = ([24, 150],)
        Static = ([24, 151],)
        TVTime = ([24, 152],)
        Dogsync = ([24, 153],)
        HeartbeatHeartbreak = ([24, 154],)
        EntryFlow = ([24, 155],)
        Snap = ([24, 156],)
        Taunt = ([24, 157],)
        Basketball = ([24, 158],)
        BrightestHeart = ([24, 159],)
        Clash = ([24, 160],)
        IMissTheQuiet = ([24, 161],)
        Insanity = ([24, 162],)
        Stomp = ([24, 163],)
        TrickyDJ = ([24, 164],)
        Conga = ([24, 165],)
        Camera = ([24, 166],)
        StreamerAdventures = ([24, 167],)
        Unyeah = ([24, 168],)
        HoofShuffle = ([24, 169],)
        StrongestOfHistory = ([24, 170],)
        StarPower = ([24, 171],)
        CursedInstincts = ([24, 172],)
        BigShoe = ([24, 173],)
        Popcorn = ([24, 174],)
        Clash2 = ([24, 175],)
        Perfect = ([24, 176],)
        OPP = ([24, 177],)
        ExcuseMeSir = ([24, 178],)
        BillyBounce = ([24, 179],)
        DreamFriends = ([24, 180],)
        Mourning = ([24, 181],)
        Insane2 = ([24, 182],)
        Boombox = ([24, 183],)
        LostMedia = ([24, 184],)
        Sidepot = ([24, 185],)
        Camcorder = ([24, 186],)
        Bird = ([24, 187],)
        Speedster = ([24, 188],)
        Paradise = ([24, 189],)
        Potential2 = ([24, 190],)
        Paradise3 = ([24, 191],)
        Pickaxe = ([24, 192],)
        Coin = ([24, 193],)
        SmoothCriminal = ([24, 194],)
        Bling = ([24, 195],)
        TrueSelf = ([24, 196],)
        Pokedance = ([24, 197],)
        Science = ([24, 198],)
        ItsNoUse = ([24, 199],)
        Stretch = ([24, 200],)
        Tiger = ([24, 201],)
        Hugo = ([24, 202],)
        Tired = ([24, 203],)
        NanaBooBoo = ([24, 204],)
        Comedian = ([24, 205],)
        Burnice = ([24, 206],)
        Dare = ([24, 207],)
        Paced = ([24, 208],)
        Jeep = ([24, 209],)
        Rocks = ([24, 210],)
        MoneyFan = ([24, 211],)
        Honored = ([24, 212],)
        Bow3 = ([24, 213],)
        ChalkToss = ([24, 214],)
        LuckStar = ([24, 215],)
        Turron = ([24, 216],)
        Nervous = ([24, 217],)
        TakeMyHat = ([24, 218],)
        SpokenFor = ([24, 219],)
        Emote_61 = ([24, 220],)
        DidYouSeeThat = ([24, 221],)
        TrueCurse = ([24, 222],)
        Democracy = ([24, 223],)
        SaiyanWalk = ([24, 224],)
        DemonDance = ([24, 225],)
        BrazilianCalisthenics = ([24, 226],)
        Equestria = ([24, 227],)
        Bang = ([24, 228],)
        LiarDancer = ([24, 229],)
        GangFlex = ([24, 230],)
        Love = ([24, 231],)
        HardJump = ([24, 232],)
        DoTheBartman = ([24, 233],)
        Envelope = ([24, 234],)
        Legend2 = ([24, 235],)
        Lonely = ([24, 236],)
        RAHHH = ([24, 237],)
        JaxToy = ([24, 238],)
        Guidance = ([24, 239],)
        AbsoluteCinema = ([24, 240],)
        Jevil = ([24, 241],)
        Demon = ([24, 242],)
        Murder = ([24, 243],)
        Turbo = ([24, 244],)
        Vessel = ([24, 245],)
        Teto = ([24, 246],)
        HippocampalReload = ([24, 247],)
        Jackpot = ([24, 248],)
        Garbage = ([24, 249],)
        Yamcha = ([24, 250],)
        Megaphone = ([24, 251],)
        GlassHeart = ([24, 252],)
        Ghouls = ([24, 253],)
        Vance = ([24, 254],)
        Extinguish = ([24, 255],)
        LightSticks = ([24, 256],)
        Sit = ([24, 257],)
        Ganon = ([24, 258],)
        BizarreDuo = ([24, 259],)
        Ragdoll = ([24, 260],)
        Swap = ([24, 261],)
        StrongestOfToday = ([24, 262],)
        Carry = ([24, 263],)
        Jolly = ([24, 264],)
        Sugawara = ([24, 265],)
        Chirumiru = ([24, 266],)
        Garry = ([24, 267],)
        Smug = ([24, 268],)
        LyingRage = ([24, 269],)
        Bathtub = ([24, 270],)
        MUSTARD = ([24, 271],)
        Slipbeat = ([24, 272],)
        BoomMic = ([24, 273],)
        BlueSky = ([24, 274],)
        OnTop = ([24, 275],)
        Jackpot2 = ([24, 276],)
        AMimir = ([24, 277],)
        PitchforkProtest = ([24, 278],)
        Superstar3 = ([24, 279],)
        FingerStand = ([24, 280],)
        Spin2 = ([24, 281],)
        Retrial = ([24, 282],)
        Fumokill = ([24, 283],)
        Potion = ([24, 284],)
        Brainrot = ([24, 285],)
        AreYou = ([24, 286],)
        PsychicRun = ([24, 287],)
        Places = ([24, 288],)
        KickBack = ([24, 289],)
        Piggyback = ([24, 290],)
        WarGirl = ([24, 291],)
        Salesman = ([24, 292],)
        DeadWrong = ([24, 293],)
        ExProvocation = ([24, 294],)
        Superstar2 = ([24, 295],)
        Photos = ([24, 296],)
        Vesselll = ([24, 297],)
        Cooking = ([24, 298],)
        Eggrolled = ([24, 299],)
        Sanitizer = ([24, 300],)
        Windy = ([24, 301],)
        Reclassed = ([24, 302],)
        Competent = ([24, 303],)
        Bizarre = ([24, 304],)
        LemonCookie = ([24, 305],)
        SpeedFeat = ([24, 306],)
        SodaPop = ([24, 307],)
        Onion = ([24, 308],)
        ABA = ([24, 309],)
        Headphones = ([24, 310],)
        Cake = ([24, 311],)
        Hug = ([24, 312],)
        Wait = ([24, 313],)
        Awkward = ([24, 314],)
        Insane = ([24, 315],)
        TestEmote = ([24, 316],)
        Silly = ([24, 317],)
        NecoArc = ([24, 318],)
        Bow2 = ([24, 319],)
        Dragon = ([24, 320],)
        Lob = ([24, 321],)
