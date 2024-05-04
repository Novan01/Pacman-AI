# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node:

    ""
    def __init__(self, state, actions, cost) -> None:
        self.state = state
        self.actions = actions
        self.cost = cost
        
    
    def printNode(self):
        print("STATE: ", self.state, "ACTIONS: ", self.actions, ", COST: ", self.cost)
        
        

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    node = Node(problem.getStartState(), [], 0)
    frontier = util.Stack()
    frontier.push(node)
    explored = set({})
    
    while True:
        if frontier.isEmpty(): return False # if frontier is empty return false; possibly error message later
        
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.actions
        
        explored.add(node.state)
        successors = problem.getSuccessors(node.state)
        
        for successor in successors:
            child = Node(successor[0], node.actions + [successor[1]], successor[2])
            if child.state not in explored:
                frontier.push(child)

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    node = Node(problem.getStartState(), [], 0)
    frontier = util.Queue()
    frontier.push(node)
    explored = set({node.state})
    
    while True:
        if frontier.isEmpty(): return False # if frontier is empty return false; possibly error message later
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.actions

        successors = problem.getSuccessors(node.state)

        for successor in successors:
            child = Node(successor[0], node.actions + [successor[1]], successor[2])
            if child.state not in explored:
                explored.add(child.state)
                frontier.push(child)

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    """Set the root node, create the priority queue, push root node to frontier and create empty explored set"""
   
    node = Node(problem.getStartState(), [], 0)
    frontier = util.PriorityQueue()
    frontier.push(node, 0)
    explored = set() 
    
    while not frontier.isEmpty():
        
        node = frontier.pop()

        if problem.isGoalState(node.state): return node.actions
        
        if node.state not in explored:
            explored.add(node.state)

            successors = problem.getSuccessors(node.state)
            
            for successor in successors:
                child = Node(successor[0], node.actions + [successor[1]], node.cost + successor[2])
                frontier.update(child, child.cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

#page 99 psuedocode?
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #create empty frontier queue and explored set
    frontier = util.PriorityQueue()
    explored = set({})
    node = Node(problem.getStartState(), [], heuristic(problem.getStartState(), problem)) #maybe change heuristic to 0
    frontier.push(node, heuristic(node.state, problem))
    
    while not frontier.isEmpty():
        #get the current node
        node = frontier.pop()
        #if current node is the goal state
        if problem.isGoalState(node.state):
            return node.actions
        
        #for each action in problem.Actions(node.state) do
        if node.state not in explored:
            explored.add(node.state)
            for successor, action, cost in problem.getSuccessors(node.state):
                if not successor in explored:
                    #calculate f, g, h values for child node and add to frontier with priority f
                    g = node.cost + cost
                    h = heuristic(successor, problem)
                    f = g + h
                    child = Node(successor, node.actions + [action], g)
                    frontier.update(child, f)
                    
                

    
    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
