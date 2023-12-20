#include <mutex>
class FooBar {
private:
    int n;
    std::mutex foo_lock;
    std::mutex bar_lock;

public:
    FooBar(int n) {
        this->n = n;
        this->foo_lock;
        this->bar_lock;
        (this->bar_lock).lock();
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            (this->foo_lock).lock();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            (this->bar_lock).unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            (this->bar_lock).lock();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            (this->foo_lock).unlock();
        }
    }
};