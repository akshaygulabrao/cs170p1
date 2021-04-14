import numpy as np
import anytree
import math

class state:
    discovered_states =set()

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
            if string_state in self.discovered_states:
                return 0
            else:
                self.discovered_states.add(string_state)
                state(self.prevMovelist,string_state)
                return 1
    def eval(self):
        job_list = []
        job_list.append(self.swapDown())
        job_list.append(self.swapUp())
        job_list.append(self.swapLeft())
        job_list.append(self.swapRight())
        return [job for job in job_list if job != 0]

    def stringToArray(self,string):
        return np.asarray(list(map(int,string.split())))
    def arrayToString(self,nparray):
        return ' '.join(map(str,nparray)) 
    def checkGoalState(self):
        #checks if the list is sorted
        return np.all(self.current_state_np[:-1] <= self.current_state_np[1:])

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
    frontier = []
    def set_custom_initial_state(self,state):
        if len(state) == self.dim ** 2:
            self.initial_state = state
        else:
            print('ILLEGAL BOARD')
            set_random_initial_state(self)
    def set_random_initial_state(self):
        np.random.shuffle(self.initial_state)
    def solve(self,):
        print(self.initial_state)
        frontier.push(state([],' '.join(map(str,self.initial_state))))
        while frontier not empty:
            frontier.push(frontier.pop().eval())
    def __init__(self,dim):
        self.dim = dim
        self.goal_state = np.arange(start=1,stop = dim ** 2+1)
        linewidth_dict = {2:5,3:7,4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
        self.initial_state = self.goal_state.copy() 
        self.set_random_initial_state()
p1 = puzzle(10)
#print(p1.initial_state)
#p1.set_custom_initial_state(np.asarray(list(map(int,'1 2 4 3'.split()))))
p1.solve()

