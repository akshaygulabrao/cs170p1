import numpy as np
import anytree
import math
import queue

explored_set= set()
frontier = queue.Queue() 

def stringToArray(string):
    return np.asarray(list(map(int,string.split())))
def arrayToString(nparray):
    return ' '.join(map(str,nparray)) 


class state:
    def swapLeft(self):
        if self.marker % self.dim != 0:
            self.current_state_np[self.marker],self.current_state_np[self.marker-1]=self.current_state_np[self.marker-1],self.current_state_np[self.marker] 
            string_state = self.arrayToString(self.current_state_np)
            self.prevMovelist.append((string_state,'Swap Right'))
            if string_state in self.discovered_states:
                return 0
            else:
                self.discovered_states.add(string_state)
                return state(self.prevMovelist,string_state)

    def swapRight(self):
        if self.marker % self.dim != self.dim -1:
            self.current_state_np[self.marker],self.current_state_np[self.marker+1]=self.current_state_np[self.marker+1],self.current_state_np[self.marker]
            string_state = self.arrayToString(self.current_state_np)
            self.prevMovelist.append((string_state,'Swap Right'))
            if string_state in self.discovered_states:
                return 0
            else:
                self.discovered_states.add(string_state)
                return state(self.prevMovelist,string_state)
    def swapUp(self):
        if self.marker - self.dim > 0:
            self.current_state_np[self.marker],self.current_state_np[self.marker - self.dim]= self.current_state_np[self.marker - self.dim],self.current_state_np[self.marker]
            string_state = self.arrayToString(self.current_state_np)
            print(string_state)
            self.prevMovelist.append((string_state,'Swap Up'))
            if string_state in self.discovered_states:
                return 0
            else:
                self.discovered_states.add(string_state)
                return state(self.prevMovelist,string_state)
    def swapDown(self):
        if self.marker + self.dim < self.dim ** 2 - 1:
            self.current_state_np[self.marker],self.current_state_np[self.marker + self.dim]= self.current_state_np[self.marker + self.dim],self.current_state_np[self.marker]
            string_state = self.arrayToString(self.current_state_np)
            self.prevMovelist.append((string_state,'Swap Down'))
        return self.current_state_np
    def eval(self):
        job_list = []
        job_list.append(self.swapDown())
        job_list.append(self.swapUp())
        return [job for job in job_list if job != 0]


    def __init__(self,prevMovelist,current_state_string):
       self.prevMovelist = prevMovelist;
       self.current_state_string = current_state_string
       print(self.current_state_string)
       self.discovered_states.add(current_state_string)
       self.current_state_np = self.stringToArray(current_state_string)
       self.marker = np.argmax(self.current_state_np)
       self.dim = int(math.sqrt(self.current_state_np[self.marker]))
       
     

class puzzle:
    discovered_states = set()
    frontier = queue.Queue() 
    def set_custom_initial_state(self,state):
        if len(state) == self.dim ** 2:
            self.initial_state = state
        else:
            print('ILLEGAL BOARD')
            set_random_initial_state(self)
    def set_random_initial_state(self):
        np.random.shuffle(self.initial_state)
    def checkGoalState(self):
        #checks if the list is sorted
        return np.all(self.current_state_np[:-1] <= self.current_state_np[1:])
    def solve(self):
        print(self.initial_state)
        frontier.put('',arrayToString(self.initial_state))
        explored_set = set()
        while(1):
            if frontier.empty():
                return 'failure'
             
        
    def __init__(self,dim):
        self.dim = dim
        self.goal_state = np.arange(start=1,stop = dim ** 2+1)
        linewidth_dict = {2:5,3:7,4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
        self.initial_state = self.goal_state.copy() 
        self.set_random_initial_state()
p1 = puzzle(2)
p1.solve()
