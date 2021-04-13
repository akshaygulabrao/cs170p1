
import numpy as np
class state:
    def __init__(self,arr,parent,dim):
        self.arr = arr
        self.parent = parent
        self.goal = goal


class puzzle:
    def set_initial_state(self,state):
        self.initial_state = state
    def __init__(self,dim):
        init_goal_state =np.arange(start=1,stop = dim ** 2+1)
        self.empty_tile =dim ** 2 
        self.goal_state = init_goal_state
np.set_printoptions(linewidth=15)
p1 = puzzle(4)

a = p1.goal_state.copy()
np.random.shuffle(a)
print(a)
print(p1.empty_tile)
#print(p1.initial_state)



