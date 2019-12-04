import random


class Data(object):
    def __init__(self):
        self.numbers = []
        self.start_game()

    def start_game(self):
        self.numbers.clear()
        self.numbers = [[0] * 4 for _ in range(4)]
        for _ in range(2):
            self.random_display()

    def random_display(self):
        randoms = [random.randint(0, 3) for _ in range(3)]
        if self.numbers[randoms[0]][randoms[1]]:
            return self.random_display()
        self.numbers[randoms[0]][randoms[1]] = [2, 2, 2, 4][randoms[2]]

    def right_move(self):
        return self.move()

    def left_move(self):
        for i in range(4):
            self.numbers[i] = self.numbers[i][::-1]
        flag = self.move()
        for i in range(4):
            self.numbers[i] = self.numbers[i][::-1]
        return flag

    def down_move(self):
        for i in range(3):
            self.exchange_data([0, i], [i, 3], [3, 3 - i], [3 - i, 0])
        self.exchange_data([1, 1], [1, 2], [2, 2], [2, 1])
        flag = self.move()
        for i in range(3):
            self.exchange_data([0, i], [3 - i, 0], [3, 3 - i], [i, 3])
        self.exchange_data([1, 1], [2, 1], [2, 2], [1, 2])
        return flag

    def up_move(self):
        for i in range(3):
            self.exchange_data([0, i], [3 - i, 0], [3, 3 - i], [i, 3])
        self.exchange_data([1, 1], [2, 1], [2, 2], [1, 2])
        flag = self.move()
        for i in range(3):
            self.exchange_data([0, i], [i, 3], [3, 3 - i], [3 - i, 0])
        self.exchange_data([1, 1], [1, 2], [2, 2], [2, 1])
        return flag

    def exchange_data(self, *args):
        for i in range(len(args) - 1):
            self.numbers[args[i][0]][args[i][1]], self.numbers[args[i + 1][0]][args[i + 1][1]] = \
                self.numbers[args[i + 1][0]][args[i + 1][1]], self.numbers[args[i][0]][args[i][1]]

    def move(self):
        flag = False
        for i in range(4):
            for j in range(3, 0, -1):
                for m in range(j - 1, -1, -1):
                    if self.numbers[i][m]:
                        if not self.numbers[i][j]:
                            self.numbers[i][j] = self.numbers[i][m]
                            self.numbers[i][m] = 0
                            for n in range(m - 1, -1, -1):
                                if self.numbers[i][n]:
                                    if self.numbers[i][j] == self.numbers[i][n]:
                                        self.numbers[i][j] *= 2
                                        self.numbers[i][n] = 0
                                    break
                            flag = True
                        elif self.numbers[i][j] == self.numbers[i][m]:
                            self.numbers[i][j] *= 2
                            self.numbers[i][m] = 0
                            flag = True
                        break
        return flag
