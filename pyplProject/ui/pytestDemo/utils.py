n: int = 100  # called as type hinting
lst: list[int] = [1, 2, 3, 4]
dt: dict[str, int] = {"key": 1}


# num is an int type and return type is float
def root(num: int) -> float:
    return pow(num, 0.5)
