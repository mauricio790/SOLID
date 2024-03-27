import Level

class Student():
    def __init__(self) -> None:
        pass

    def graduate(self, level: Level):
        # graduate according to education level
        print(f"Felicidades! {level.graduate()}")