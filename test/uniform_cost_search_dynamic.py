import argparse
import math
import pandas as pd
from simpleai.search import SearchProblem, uniform_cost

class Route(SearchProblem):
    def __init__(self, start, goal, costs):
        self.goal = goal
        self.costs = costs
        super().__init__(initial_state=start)

    def actions(self, state):
        return [
            j for j, c in enumerate(self.costs[state])
            if j != state and c != math.inf and c != 0
        ]

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return self.costs[state][action]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--goal", required=True)
    args = parser.parse_args()

    # ✅ Read CSV with headers (A,B,C,D,E) and NO index column
    df = pd.read_csv(args.file)
    df = pd.read_csv(args.file)
    print("DF HEAD:\n", df.head())
    print("DF COLUMNS:", df.columns.tolist())
    print("DF INDEX:", df.index.tolist())


    # ✅ Use column names as labels
    labels = list(df.columns)

    # ✅ Replace 'inf' strings with math.inf and convert to float
    df = df.replace("inf", math.inf)
    df = df.astype(float)

    costs = df.values.tolist()

    # Validate start/goal
    args.start = args.start.upper()
    args.goal = args.goal.upper()

    if args.start not in labels or args.goal not in labels:
        raise ValueError(f"Nodes must be one of {labels}")

    start_idx = labels.index(args.start)
    goal_idx = labels.index(args.goal)

    problem = Route(start_idx, goal_idx, costs)
    result = uniform_cost(problem)

    states = [state for (_, state) in result.path()]
    path_labels = [labels[s] for s in states]

    print("Shortest path:", " -> ".join(path_labels))
    print("Total cost:", result.cost)


if __name__ == "__main__":
    main()
