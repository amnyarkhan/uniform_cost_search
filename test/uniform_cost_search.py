# importing the libraries to solve the search problem
from simpleai.search import SearchProblem, uniform_cost


# Define the cost of connected nodes as 2x2 array structured as [[]:node A paths to all]

# As the nodes in the graph are represented as alhabets from A TO E
# Associate each alphabet to numerical values

'''
A = 1
B = 2
C = 3
D = 4
E = 5
'''

COSTS = [
    [0, 4, 'inf',2,'inf'],
    [4, 0, 3, 1, 5],
    ['inf', 3, 0, 'inf', 6],
    [2, 1,'inf', 0, 8],
    ['inf', 5, 6, 8, 0]
    
]

# Lets define the search problem
class Route(SearchProblem):
    
    def __init__(self, initial, goal):
        
        self.initial = initial-1
        self.goal = goal-1
        super(Route, self).__init__(initial_state=self.initial)
    
    # We need to define list of actions
    def actions(self, state):
        actions = []
        
        for action in range(len(COSTS[state])):
            
            if COSTS[state][action] not in ['inf',0]:
                actions.append(action)
        return actions
    
    # For results we just return the action
    def result(self, state, action):
        return action
    
    # Check if the goal has been reaced
    def is_goal(self, state):
        return state == self.goal
    
    #Cost of action is moving from node a to node b
    def cost(self, state, action, state2):
        return COSTS[state][action]
    
    
    # We want to find the shortest way from node 1(A) to node 3 (C)
problem = Route(1,3)
    
result = uniform_cost(problem)
    
path = [x[1]+1 for x in result.path()]
    
print(f'THE route is {path} and the cost is {result.cost}')