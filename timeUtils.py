class TimeUtils:
    def __init__(self):
        pass

    @staticmethod
    def checkTime():
        pass

    @staticmethod
    def consumedTime_decorator(func):
        import time

        def wrapper(args):

            s = time.time()

            x = func(*args)

            s1 = time.time()

            print(f"{round(s1 - s, 1)} seconds consumed")

            return x

        return wrapper
