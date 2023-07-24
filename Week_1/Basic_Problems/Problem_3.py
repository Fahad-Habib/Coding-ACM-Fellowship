from time import time


def test_func():
    for i in range(1, 10000000):
        pass


start = time()
test_func()
print(time() - start)
