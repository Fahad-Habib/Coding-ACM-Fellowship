import cProfile


def test_func():
    for i in range(100):
        pass


cProfile.run('test_func()')
