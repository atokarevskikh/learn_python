class CountFromBy:


    def __init__(self, value: int=0, increment: int=1) -> None:
        self.value = value
        self.increment = increment
    

    def increase(self) -> None:
        self.value += self.increment
    
    
    def __repr__(self) -> str:
        return str(self.value)
