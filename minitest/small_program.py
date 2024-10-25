class SmallProgram(object):
    
    def __init__(self) -> None:
        self.result : list[str | int] = []


    def check_number(self, number: int) -> str | int:    
        if number % 3 == 0 and number % 5 == 0:
            return "FooBar"
        elif number % 3 == 0:
            return "Foo"
        elif number % 5 == 0:
            return "Bar"
        else:
            return number



    def is_prime_number(self, number: int) -> bool:
        if number <= 1:
            return False
        else:
            for idx in range(2, number):
                if number % idx == 0:
                    return False
            else:
                return True      


    def main(self) -> None:
        for i in range(100, 0, -1):
            if not self.is_prime_number(i):
                res = self.check_number(i)
                if res:
                    self.result.append(res)
        
        print(*self.result)








obj = SmallProgram()
obj.main()