class H2O:
    def __init__(self):
        self.o_mutex = threading.Lock()
        self.h_mutex = threading.Lock()
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(2)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_mutex:
            self.h_sem.acquire()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.o_sem.release()



    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_mutex:
            self.o_sem.acquire()
            self.o_sem.acquire()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            self.h_sem.release()
            self.h_sem.release()