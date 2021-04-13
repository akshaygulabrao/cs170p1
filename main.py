
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
        init_goal_state =np.arange(dim ** 2).reshape(dim,dim)
        self.empty_tile =dim ** 2 
        self.goal_state = init_goal_state

p1 = puzzle(4)

print(np.random.shuffle(p1.goal_state))
print(p1.empty_tile)
print(p1.initial_state)



