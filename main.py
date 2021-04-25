import numpy as np
import queue
import math


# https://docs.python.org/3/library/queue.html
# https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
# https://stackoverflow.com/questions/34472814/use-a-any-or-a-all
# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html?highlight=permutation#numpy.random.permutation
# https://stackoverflow.com/questions/41210142/get-all-permutations-of-a-numpy-array
# https://numpy.org/doc/stable/reference/generated/numpy.load.html
# https://numpy.org/doc/stable/reference/generated/numpy.save.html
# https://www.geeksforgeeks.org/python-math-function-hypot/
# http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/#:~:text=Both%20require%20at%20least%2031,starting%20at%20the%20goal%20state).
# https://stackoverflow.com/questions/18129830/count-the-uppercase-letters-in-a-string-with-python

def stringToArray(string):
    return np.asarray(list(map(int, string.split())))


def arrayToString(nparray):
    return ' '.join(map(str, nparray))
def arrayPrint(a,dim):
    for i in range(dim):
        for j in range(dim):
            if a[i*dim + j] != 9:
                print(str(a[i*dim + j]),end=' ')
            else:
                print(str(a[i*dim + j]),end = ' ')
class State:
    def __init__(self, prevMoveList, state, dim, heuristic_type):
        self.state = state
        #print(self.state)
        self.heuristic = 0
        self.heuristic_type = heuristic_type
        self.prevMoveList = prevMoveList
        self.emptyTile = np.argmax(state)
        self.dim = dim
        self.evaluate_heuristic(state)

    def evaluate_heuristic(self, arr):
        if self.heuristic_type == "ucs":
            heuristic = 0
        if self.heuristic_type == "misplaced_tiles":
            heuristic = 0
            for i in range(0, len(arr)):
                if arr[i] != i + 1:
                    heuristic += 1
        if self.heuristic_type == "euclidean_distance":
            heuristic = 0
            for i in range(0,len(arr)):
                destination = arr[i] - 1
                source = i
                heuristic += math.hypot(abs(destination - source) // 3,
                                        abs(destination - source) % 3)
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
            return self.heuristic, self.prevMoveList + 'Down', new_state

        return self.heuristic, self.prevMoveList, arrayToString(self.state)

    def swapUp(self):
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapUp is legal, else return exact same state
        if i - self.dim >= 0:
            p[i], p[i - self.dim] = p[i - self.dim], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic, self.prevMoveList + 'Up', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic, self.prevMoveList, arrayToString(self.state)

    def swapRight(self):
        # locals to make swap shorter
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapRight is legal, else return exact same state
        if i % self.dim != self.dim - 1:
            p[i], p[i + 1] = p[i + 1], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic, self.prevMoveList + 'Right', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic, self.prevMoveList, arrayToString(self.state)

    def swapLeft(self):
        p = self.state.copy()
        i = self.emptyTile
        # return new state if swapLeft is legal, else return exact same state
        if i % self.dim != 0:
            p[i], p[i - 1] = p[i - 1], p[i]
            self.evaluate_heuristic(p)
            new_state = arrayToString(p)
            return self.heuristic, self.prevMoveList + 'Left', new_state
        self.evaluate_heuristic(self.state)
        return self.heuristic, self.prevMoveList, arrayToString(self.state)


class Puzzle:
    frontier = queue.PriorityQueue()
    explored_set = set()

    def set_custom_initial_state(self, string):
        self.initial_state = stringToArray(string)

    def graph_search(self):
        expanded_nodes = 0
        maximum_frontier_size = 0
        self.frontier.put((0, 0, '', self.initial_state))
        self.explored_set = set()
        while 1:
            # print(self.frontier.queue)
            maximum_frontier_size = max(maximum_frontier_size,self.frontier.qsize())
            if self.frontier.empty():
                return 'failure'
            else:
                explored_state = self.frontier.get()
                print(f'The best state to expand with g(n)={explored_state[1]}'
                      f' h(n) = {explored_state[0] - explored_state[1]} is')
                s1 = State(explored_state[2], explored_state[3], self.dim,
                           self.heuristic)
                print(s1.state,sep= " ")

                if np.array_equal(s1.state, self.goal_state):
                    print("maximum frontier size: ",maximum_frontier_size)
                    print("expanded nodes: ",expanded_nodes)
                    depth = sum(1 for letter in s1.prevMoveList if letter.isupper())
                    print('Depth: ',depth)
                    return 'success', s1.prevMoveList
                else:
                    print('Expanding this node...')
                    new_states = s1.expand()
                    expanded_nodes += 1
                    for i in new_states:
                        if i[2] not in self.explored_set:
                            self.explored_set.add(i[2])
                            depth = sum(1 for letter in i[1] if letter.isupper())
                            self.frontier.put((i[0] + depth,depth, i[1], stringToArray(i[2])))
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

print('Welcome to 862007974 8 puzzle solver.')
print('Type 1 to use a default puzzle, or 2 to enter your own puzzle')
default_custom = input()
#default_custom = 1
print('Enter algorithm choice')
print('1. UCS\n2. Misplaced Tiles\n3. Euclidean Distance')
algorithm = input()
#algorithm = 1
#print(type(algorithm))
algorithm_dict = {1 : 'ucs',2: 'misplaced_tiles',3: 'euclidean_distance'}
p1 = Puzzle(3, algorithm_dict[int(algorithm)])
if default_custom == '2':
    print("Enter your array as a string Ex: '8 6 7 2 5 4 3 9 1'")
    print("9 is the blank space")
    array = input()
    p1.set_custom_initial_state(arrayToString(array))
else:
    #print(algorithm_dict[algorithm])
    p1.set_custom_initial_state('1 2 3 4 9 6 7 5 8')
print(p1.graph_search())
