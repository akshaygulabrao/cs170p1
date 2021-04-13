import numpy as np
import anytree
import math

class state:
    discovered_states =set() 
    def swapLeft(self):
        if self.marker % self.dim == 0:
            return
        else: 
            #self.current_state_np[self.marker],
            #self.current_state_np[self.marker-1]=self.current_state_np[self.marker-1],
            #self.current_state_np[self.marker]
            print(self.current_state_np[self.marker])
            curr_string = ' '.join(map(str,self.current_state_np)) 
            if curr_string not in self.discovered_states:
                self.discovered_states.add(curr_string)
                print(self.discovered_states)
                state(self,self.prevMoveList.append(self.current_state_np,'swapLeft'))
            else:
                return
    def swapRight(self):
        return 1
    def swapUp(self):
        return 2
    def swapDown(self):
        return 2 
    
    def checkGoalState(self):
        #checks if the list is sorted
        return np.all(self.current_state_np[:-1] <= self.current_state_np[1:])

    def __init__(self,prev_operation_list,current_state_string):
       self.prev_operation_list = prev_operation_list;
       self.current_state_string = current_state_string
       self.discovered_states.add(current_state_string)
       self.current_state_np = np.asarray(list(map(int,current_state_string.split())))
       self.marker = np.argmax(self.current_state_np)
       self.dim = math.sqrt(self.current_state_np[self.marker])
       self.swapLeft()
     

class puzzle:
    def set_custom_initial_state(self,state):
        if len(state) == dim ** 2:
            self.initial_state = state
        else:
            print('ILLEGAL BOARD')
            set_random_initial_state(self)
    def set_random_initial_state(self):
        np.random.shuffle(self.initial_state)
    def solve(self):
        print(self.initial_state)
        state([],' '.join(map(str,self.initial_state)))
    def __init__(self,dim):
        self.goal_state = np.arange(start=1,stop = dim ** 2+1)
        linewidth_dict = {2:5,3:7,4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
        self.initial_state = self.goal_state.copy() 
        self.set_random_initial_state()
p1 = puzzle(2)
#print(p1.initial_state)
p1.solve()

