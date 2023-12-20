class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.condvar = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.condvar:
                while (self.i % 5 == 0 or self.i % 3 != 0) and self.i <= self.n:
                    self.condvar.wait()
                if self.i > self.n:
                    self.condvar.notify_all()
                    break
                printFizz()
                self.i += 1
                self.condvar.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condvar:
                while (self.i % 5 != 0 or self.i % 3 == 0) and self.i <= self.n:
                    self.condvar.wait()
                if self.i > self.n:
                    self.condvar.notify_all()
                    break
                printBuzz()
                self.i += 1
                self.condvar.notify_all()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condvar:
                while (self.i % 5 != 0 or self.i % 3 != 0) and self.i <= self.n:
                    self.condvar.wait()
                if self.i > self.n:
                    self.condvar.notify_all()
                    break
                printFizzBuzz()
                self.i += 1
                self.condvar.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condvar:
                while (self.i % 5 == 0 or self.i % 3 == 0) and self.i <= self.n:
                    self.condvar.wait()
                if self.i > self.n:
                    self.condvar.notify_all()
                    break
                printNumber(self.i)
                self.i += 1
                self.condvar.notify_all()


        