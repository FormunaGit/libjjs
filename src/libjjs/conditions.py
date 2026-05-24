class Conditions:
    def IN_AIR(self, flip: bool = False) -> dict:
        return {"K_NAME": "AIR", "FLIP": flip}

    def IS_JUMPING(self, flip: bool = False) -> dict:
        return {"K_NAME": "JUMP", "FLIP": flip}

    def HAS_TARGET(self, flip: bool = False) -> dict:
        return {"K_NAME": "AIM", "FLIP": flip}

    def IS_AWAKENED(self, flip: bool = False) -> dict:
        return {"K_NAME": "ULT", "FLIP": flip}

    def HAS_AWK_BAR(self, amount: float = 2, flip: bool = False) -> dict:
        return {"K_NAME": "BAR", "AMOUNT": amount, "FLIP": flip}

    def DURABILITY(self, durability: float = 1) -> dict:
        return {"K_NAME": "DUR", "DURABILITY": durability}

    def HAS_HEALTH(self, amount: float = 1, flip: bool = False) -> dict:
        return {"K_NAME": "HP", "AMOUNT": amount, "FLIP": flip}

    def IS_IN_DOMAIN(self, flip: bool = False) -> dict:
        return {"K_NAME": "DOMAIN", "FLIP": flip}

    def IS_HOLDING(self, flip: bool = False) -> dict:
        return {"K_NAME": "HOLD", "FLIP": flip}
