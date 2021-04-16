import numpy as np
import queue
#https://docs.python.org/3/library/queue.html
#https://numpy.org/doc/stable/reference/generated/numpy.argmax.html

def stringToArray(string):
    return np.asarray(list(map(int,string.split())))
def arrayToString(nparray):
    return ' '.join(map(str,nparray))

class State:
    def __init__(self,prevMoveList,state,dim):
        self.state = state
        self.prevMoveList = prevMoveList
        self.emptyTile = np.argmax(state)
        self.dim = dim
    def expand(self):
        full_expansion = []
        full_expansion.append(self.swapDown())
        full_expansion.append(self.swapUp())
        full_expansion.append(self.swapLeft())
        full_expansion.append(self.swapRight())
        return full_expansion 
    def swapDown(self):
        p = self.state   
        #index of emptyTile
        i = self.emptyTile
        #maximum index of array(to check is swapDown is valid)
        m = self.dim ** 2 - 1
        #return new state if swapDown is legal, else return exact same state
        if i + self.dim <= m:
            p[i],p[i + self.dim] = p[i + self.dim],p[i]
            self.prevMoveList = self.prevMoveList + ' Down'
            self.state = p
            new_state = arrayToString(p) 
            print(self.prevMoveList, new_state) 
            return (self.prevMoveList, new_state)           

        print(self.prevMoveList, self.state) 
        return (self.prevMoveList, self.state) 
         
    def swapUp(self):
        p = self.state   
        i = self.emptyTile
        #return new state if swapUp is legal, else return exact same state
        if i -  self.dim >= 0:
            p[i],p[i + self.dim] = p[i + self.dim],p[i]
            self.prevMoveList = self.prevMoveList + ' Up'
            self.state = p
            new_state = arrayToString(p) 
            return (self.prevMoveList, new_state)           
        return (self.prevMoveList, self.state) 

    def swapRight(self):
        #locals to make swap shorter
        p = self.state   
        i = self.emptyTile
        #return new state if swapRight is legal, else return exact same state
        if i %  self.dim != self.dim - 1:
            p[i],p[i + self.dim] = p[i + self.dim],p[i]
            self.prevMoveList = self.prevMoveList + ' Right'
            self.state = p
            new_state = arrayToString(p) 
            return (self.prevMoveList, new_state)           
        return (self.prevMoveList, self.state) 


    def swapLeft(self):
        p = self.state   
        i = self.emptyTile
        #return new state if swapLeft is legal, else return exact same state
        if i %  self.dim != 0:
            p[i],p[i + self.dim] = p[i + self.dim],p[i]
            self.prevMoveList = self.prevMoveList + ' Left'
            self.state = p
            new_state = arrayToString(p) 
            return (self.prevMoveList, new_state)           
        return (self.prevMoveList, self.state) 


class Puzzle:
    frontier = queue.PriorityQueue() 
    explored_set = set()

    def set_custom_initial_state(self,string):
        self.initial_state = stringToArray(string)
    def graph_search(self):
        self.frontier.put((0,'',self.initial_state))
        self.explored_set = set()
        while not self.frontier.empty():
            explored_state = self.frontier.get()
            s1 = State(explored_state[1],explored_state[2],self.dim)
            s1.expand()
        return 0

    def __init__(self,dim,heuristic):
        self.dim = dim
        solved_state = np.arange(start=1,stop=dim ** 2 + 1)
        self.goal_state = solved_state.copy()
        self.initial_state = solved_state.copy()
        np.random.shuffle(self.initial_state)
        linewidth_dict = {2:5,3:7,4:15,5:17}
        np.set_printoptions(linewidth=linewidth_dict[dim])

        
p1 = Puzzle(2,'ucs')
p1.set_custom_initial_state('1 4 3 2')

p1.graph_search()

