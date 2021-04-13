
import numpy as np
class state:
    def __init__(self,arr,parent,dim):
        self.arr = arr
        self.parent = parent
        self.goal = goal


class puzzle:
    def set_custom_initial_state(self,state):
        self.initial_state = state
    def set_random_initial_state(self,state):
        self.initial_state = np.random.shuffle(p1.goal_state.copy())
    def __init__(self,dim):
        init_goal_state =np.arange(start=1,stop = dim ** 2+1)
        self.empty_tile =dim ** 2 
        self.goal_state = init_goal_state
        linewidth_dict = { 4:15,5:17,6:19,7:22,8:25,9:28,10:44} 
        np.set_printoptions(linewidth=linewidth_dict[dim])
p1 = puzzle(10)

print(p1.goal_state)


