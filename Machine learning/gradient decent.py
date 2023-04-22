# from random import randint


class Local_min:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __f(self, x):
        return self.a * x**2 + self.b * x + self.c

    def local_min(self, N, cur_x, step):
        for i in range(N):
            current_y = self.__f(cur_x)
            y_1 = self.__f(cur_x+0.01)

            d = current_y - y_1
            cur_x += d * step

        return cur_x



