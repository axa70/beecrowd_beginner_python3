# C code for honeywalk problem
#https://github.com/ltowarek/honeycomb-walk/blob/master/src/honeycomb_walk.cpp 


#Code done by chatgpt
class HoneycombWalk:
    def __init__(self):
        self.max_steps = 50
        self.steps = [[[-1] * (2 * self.max_steps + 1) for _ in range(2 * self.max_steps + 1)] for _ in range(2 * self.max_steps + 1)]

    def walk(self, number_of_steps):
        return self._walk(0, 0, number_of_steps)

    def _walk(self, x, y, s):
        if s == 0:
            if x == 0 and y == 0:
                return 1
            else:
                return 0

        if self.steps[x + self.max_steps][y + self.max_steps][s] != -1:
            return self.steps[x + self.max_steps][y + self.max_steps][s]

        output = 0
        output += self._walk(x - 1, y - 1, s - 1)
        output += self._walk(x, y - 1, s - 1)
        output += self._walk(x + 1, y, s - 1)
        output += self._walk(x + 1, y + 1, s - 1)
        output += self._walk(x, y + 1, s - 1)
        output += self._walk(x - 1, y, s - 1)

        self.steps[x + self.max_steps][y + self.max_steps][s] = output

        return output


# Example usage:
N = int(input())

for i in range(N):
    honeycomb = HoneycombWalk()
    number_of_steps = int(input())
    #print("Number of paths with", number_of_steps, "steps:", honeycomb.walk(number_of_steps))
    print(honeycomb.walk(number_of_steps))