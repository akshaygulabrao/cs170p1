
import numpy as np
class state:
    def __init__(self,arr,parent,dim):
        self.arr = arr
        self.parent = parent
        self.goal = goal


class puzzle:
    def set_custom_initial_state(self,state):
        if len(state) == dim ** 2:
            self.initial_state = state
        else:
            print('ILLEGAL BOARD')
            set_random_initial_state(self)
        
    def set_random_initial_state(self):
        self.inital_state = self.goal_state.copy()
        np.random.shuffle(self.initial_state)
        print(self.initial_state)
    def __init__(self,dim):
        init_goal_state =np.arange(start=1,stop = dim ** 2+1)
        self.empty_tile =dim ** 2 
        self.goal_state = init_goal_state
        linewidth_dict = { 3:7,4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
        self.initial_state = self.goal_state.copy() 
        self.set_random_initial_state()



p1 = puzzle(3)

#print(p1.initial_state)


