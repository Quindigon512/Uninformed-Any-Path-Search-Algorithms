#######################################################
# Author:   Quinn Trate
# Date:     September 24, 2023
# Class:    CMPSC 441 Artificial Intelligence
# Language: Python
# Purpose:  Implements Depth-First and Breadth-
#	    First Search Algorithms for the N-
#	    Queens and Farmers Problems.
#######################################################



########################################################
# Import
########################################################


from hw2_utils import *
from collections import deque


##########################################################
# 1. Uninformed Any-Path Search Algorithms
##########################################################


def depth_first_search(problem):
    # Initialization for depth first search
    node = Node(problem.init_state)
    frontier = deque([node])         # stack: append/pop
    explored = [problem.init_state]  # used as "visited"
    while len(frontier) > 0:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        for i in node.expand(problem):
            if i.state not in explored:
                explored.append(i.state)
                frontier.append(i)
    return Node(None)


def breadth_first_search(problem):
    # Initialization for breadth first search
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: append/popleft
    explored = [problem.init_state]  # used as "visited"
    while len(frontier) > 0:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        for i in node.expand(problem):
            if i.state not in explored:
                explored.append(i.state)
                frontier.append(i)
    return Node(None)





##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for NQueenProblem
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n

    
    def actions(self, state):
        if -1 not in state:
            return []
        empty = state.index(-1)
        arr = [i for i in range(0, len(state))]
        for column in range(0, empty):
            for hit in [state[column], state [column] - (empty - column), state[column] + (empty - column)]:
               if hit in arr:
                   arr.remove(hit)
        return arr
    

    def result(self, state, action):
        arr = []
        for elem in state:
            if elem == -1:
                break
            arr.append(elem)
        arr.append(action)
        for i in range(0, state.count(-1) - 1):
            arr.append(-1)
        return tuple(arr)
    
                        
    def goal_test(self, state):
        if -1 in state:
            return False
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    return False
        return True





##########################################################
# 3. Farmer's Problem
##########################################################


class FarmerProblem(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for FarmerProblem
    
    def __init__(self, init_state, goal_state = (False, False, False, False)):
        super().__init__(init_state, goal_state)

    
    def actions(self, state):
        arr = []
        for i in range(0, len(state)):
            if state[0] != state[i]:
                continue
            lst = list(state)
            lst[0] = not lst[0]
            if i > 0:
                lst[i] = not lst[i]
            valid = True
            for j in range(1, len(state) - 1):
                if lst[0] != lst[j] and lst[j] == lst[j + 1]:
                    valid = False
            if valid:
                if i == 0:
                    arr.append('F')
                elif i == 1:
                    arr.append('FG')
                elif i == 2:
                    arr.append('FC')
                elif i == 3:
                    arr.append('FX')
                else:
                    raise Exception("Not Proper Move")
        return arr

    
    def result(self, state, action):
        arr = list(state)
        arr[0] = not arr[0]
        if action == 'F':
            index = 0
        elif action == 'FG':
            index = 1
        elif action == 'FC':
            index = 2
        elif action == 'FX':
            index = 3
        else:
            raise Exception("Not Proper Move")
        if index != 0:
            arr[index] = not arr[index]
        return tuple(arr)

    
    def goal_test(self, state):
        return state == self.goal_state





##########################################################
# 4. Graph Problem
##########################################################


class GraphProblem(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for GraphProblem

    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

    
    def actions(self, state):
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        return action

    
    def goal_test(self, state):
        return state == self.goal_state
