import numpy as np
import queue


# https://docs.python.org/3/library/queue.html
# https://numpy.org/doc/stable/reference/generated/numpy.argmax.html

def stringToArray(string):
    return np.asarray(list(map(int, string.split())))


def arrayToString(nparray):
    return ' '.join(map(str, nparray))


class State:
    def __init__(self, prevMoveList, state, dim,heuristic_type):
        self.state = state
        self.heuristic = 0
        self.heuristic_type = heuristic_type
        self.prevMoveList = prevMoveList
        self.emptyTile = np.argmax(state)
        self.dim = dim

    def evaluate_heuristic(self,arr):
        if self.heuristic_type == "ucs":
            heuristic = 0
        if self.heuristic_type == "misplaced_tiles":
            heuristic = 0
            for i in range(0,len(arr)):
                if arr[i] != i + 1:
                    heuristic +=1
        self.heuristic = heuristic



    def expand(self):
        full_expansion = [self.swapDown(), self.swapUp(), self.swapRight(), self.swapLeft()]
        #   print(full_expansion)
        return full_expansion

    def swapDown(self):
        p = self.state.copy()
        # index of emptyTile
        i = self.emptyTile
        # maximum index of array(to check is swapDown is valid)
        m = self.dim ** 2 - 1
        # return new state if swapDown is legal, else return exact same state
        if i + self.dim <= m:
            p[i], p[i + self.dim] = p[i + self.dim], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic,self.prevMoveList + 'Down', new_state

        return self.heuristic,self.prevMoveList, arrayToString(self.state)

    def swapUp(self):
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapUp is legal, else return exact same state
        if i - self.dim >= 0:
            p[i], p[i - self.dim] = p[i - self.dim], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic,self.prevMoveList + 'Up', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic,self.prevMoveList, arrayToString(self.state)

    def swapRight(self):
        # locals to make swap shorter
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapRight is legal, else return exact same state
        if i % self.dim != self.dim - 1:
            p[i], p[i + 1] = p[i + 1], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic,self.prevMoveList + 'Right', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic,self.prevMoveList, arrayToString(self.state)

    def swapLeft(self):
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapLeft is legal, else return exact same state
        if i % self.dim != 0:
            p[i], p[i - 1] = p[i - 1], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic,self.prevMoveList + 'Left', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic,self.prevMoveList, arrayToString(self.state)


class Puzzle:
    frontier = queue.PriorityQueue()
    explored_set = set()

    def set_custom_initial_state(self, string):
        self.initial_state = stringToArray(string)

    def graph_search(self):
        tiebreak = 0
        self.frontier.put((0,tiebreak, '', self.initial_state))
        self.explored_set = set()
        while 1:
            if self.frontier.empty():
                return 'failure'
            else:
                explored_state = self.frontier.get()
                s1 = State(explored_state[2], explored_state[3], self.dim,
                           self.heuristic)
                if np.array_equal(s1. state, self.goal_state):
                    return 'success', s1.prevMoveList
                new_states = s1.expand()
                for i in new_states:
                    if i[1] not in self.explored_set:
                        self.explored_set.add(i[2])
                        self.frontier.put((i[0],tiebreak, i[1], stringToArray(i[2])))
            tiebreak+=1
                # print(self.explored_set)

    def __init__(self, dim, heuristic):
        self.dim = dim
        self.heuristic = heuristic
        solved_state = np.arange(start=1, stop=dim ** 2 + 1)
        self.goal_state = solved_state.copy()
        self.initial_state = solved_state.copy()
        np.random.shuffle(self.initial_state)
        linewidth_dict = {2: 5, 3: 7, 4: 15, 5: 17}
        np.set_printoptions(linewidth=linewidth_dict[dim])


p1 = Puzzle(3, 'misplaced_tiles')
p1.set_custom_initial_state('1 9 3 4 2 6 7 5 8')

print(p1.graph_search())
