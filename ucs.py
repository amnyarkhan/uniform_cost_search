import argparse
import math
import pandas as pd
from simpleai.search import SearchProblem, uniform_cost



class Route(SearchProblem):
    
    # Constructor will take start node , goal node and cost matrix
    def __init__(self, start, goal, costs):
        
        self.goal = goal
        self.costs = costs
        super().__init__(initial_state=start)
    
    # This method returns the actions list    
    def actions(self, state):
        return [
            j for j,c in enumerate(self.costs)
            if j != state and c != math.inf and c != 0
        ]
    
    def result(self, state, action):
        return action
    
    def is_goal(self, state):
        return state == self.goal
    
    def cost(self, state, action, state2):
        return self.costs[state][action]

def main():
    parser = argparse.ArgumentParser(description="Uniform Cost Search")
    
    parser.add_argument("--file",required=True,help="Path to csv file")
    parser.add_argument('--start',required=True,help="Starting Node")
    parser.add_argument('--goal',required=True, help="Goal Node")
    args = parser.parse_args()
    
    # Read the csv file with header
    df = pd.read_csv(args.file)
    
    # Use columns names as labels
    labels = list(df.columns)
    
    #Replace the "inf" string with math.inf and convert to float
    df = df.replace("inf",math.inf)
    df = df.astype(float)
    
    costs = df.values.tolist()
    
    #Validate the start / goal
    args.start = args.start.upper()
    args.goal = args.goal.upper()
    
    if args.start not in labels or args.goal not in labels:
        raise ValueError(f"Node must be one of {labels}")
    
    start_idx = labels.index(args.start)
    goal_idx = labels.index(args.goal)
    
    problem = Route(start_idx,goal_idx,costs)
    result = uniform_cost(problem)
    
    states = [state for (_,state) in result.path()]
    path_labels = [labels[s] for s in states]
    
    print("Shortest Path","-->".join(path_labels))
    print("Total cost:", result.cost)

if __name__ == "__main__":
    main()