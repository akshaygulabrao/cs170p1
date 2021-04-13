import numpy as np
import anytree

class state:
    discovered_states =set() 
    def swapLeft(self):
        return 1 
    def swapRight(self):
        return 1
    def swapUp(self):
        return 2
    def swapDown(self):
        return 2 
    def __init__(self,prev_operation_list,current_state):
       self.prev_operation_list = prev_operation_list;
       self.current_state = current_state
       self.discovered_states.add(current_state)
       #print(np.asarray(list(map(int,current_state.split()))))

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

