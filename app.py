class Test:
    def __init__(self, test1: int, test2: float, test3: str) -> None:
        self.test1: int = test1
        self.test2: float = test2
        self.test3: str = test3

    def __repr__(self) -> str:
        print(f"{self.test1}, {self.test2}, {self.test3}")


testobj = Test(34, 100.12, "updated this string too")
