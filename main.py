import numpy as np

def stringToArray(string):
    return np.asarray(list(map(int,string.split())))
def arrayToString(nparray):
    return ' '.join(map(str,nparray))

class State:
    def __init__(prevMoveList,state):
        self.prevMoveList = prevMoveList
        self.state = stringToArray(state)
class Puzzle:
    frontier = []
    explored_set = set()
    def set_custom_initial_state(string):
        sef.initial_state = stringToArray(string)
        

    def __init__(self,dim):
        self.dim = dim
        self.initial_state = np.random.shuffle(np.arange(start=1,stop=dim ** 2 + 1))
        linewidth_dict = {2:5,3:7,4:15,5:17}
        np.set_printoptions(linewidth=linewidth_dict[dim])
        
p1 = Puzzle(2)

print(p1.initial_state)
