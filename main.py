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
            arr = stringToArray(current_state_string)
            arr[self.marker],arr[self.marker-1] = arr[self.marker -1],arr[self.marker]
            string_state = self.arrayToString(arr)
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
        if self.marker + self.dim <= self.dim ** 2 - 1:
            print('SwapDown')
            arr = stringToArray(self.current_state_string)
            arr[self.marker],arr[self.marker+self.dim]= arr[self.marker+self.dim],arr[self.marker]
            string_state = arrayToString(arr)
            app_str = self.prevMovelist + 'Swap Down ' 
            print(arrayToString(arr))
            new_state = (app_str,arrayToString(arr))
            return new_state
    def eval(self):
        job_list = []
        job_list.append(self.swapDown())
        print(job_list)
        return job_list 


    def __init__(self,prevMovelist,current_state_string):
       self.prevMovelist = prevMovelist;
       self.current_state_string = current_state_string
       self.current_state_np = stringToArray(current_state_string)
       self.marker = np.argmax(self.current_state_np)
       self.dim = int(math.sqrt(self.current_state_np[self.marker]))
       
     

class puzzle:
    discovered_states = set()
    frontier = queue.Queue() 
    def set_initial_state(self,state):
        arr = stringToArray(state)
        if len(arr) == self.dim ** 2:
            self.initial_state =arr 
        else:
            print('ILLEGAL BOARD')
            self.set_random_initial_state()
    def set_random_initial_state(self):
        np.random.shuffle(self.initial_state)
    def checkGoalState(self):
        #checks if the list is sorted
        return np.all(self.current_state_np[:-1] <= self.current_state_np[1:])
    def solve(self):
        print(self.initial_state)
        frontier.put(('',arrayToString(self.initial_state)))
        explored_set = set()
        if frontier.empty():
            return 'failure'
        else:
            chosen_state = frontier.get() 
            #print(chosen_state)
            s = state(chosen_state[0],chosen_state[1])
            #print(s.eval())
            #print(s.prevMovelist,s.current_state_string)
              
        
    def __init__(self,dim):
        self.dim = dim
        self.goal_state = np.arange(start=1,stop = dim ** 2+1)
        linewidth_dict = {2:5,3:7,4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
        self.initial_state = self.goal_state.copy() 
        self.set_random_initial_state()
p1 = puzzle(2)
p1.set_initial_state('1 4 3 2')
p1.solve()
