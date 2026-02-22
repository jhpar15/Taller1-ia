from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import  nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


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
    queue = utils.Queue()
    visited = set()

    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        state, actions = queue.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, _ in problem.getSuccessors(state):
                queue.push((successor, actions + [action]))

    return []

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # Cola de prioridad: ordena por f(n) = g(n) + h(n)
    frontier = utils.PriorityQueue()

    # Estado inicial
    startState = problem.getStartState()
    frontier.push((startState, [], 0), heuristic(startState, problem))

    # Diccionario de costos mínimos encontrados hasta cada estado
    bestCost = {}

    while not frontier.isEmpty():
        state, actions, costSoFar = frontier.pop()

        # Si llegamos al objetivo, devolvemos el plan
        if problem.isGoalState(state):
            return actions

        # Si ya llegamos a este estado con menor costo, ignoramos
        if state in bestCost and bestCost[state] <= costSoFar:
            continue

        bestCost[state] = costSoFar

        # Expandir sucesores
        for successor, action, stepCost in problem.getSuccessors(state):
            newCost = costSoFar + stepCost
            newActions = actions + [action]
            priority = newCost + heuristic(successor, problem)

            frontier.push((successor, newActions, newCost), priority)

    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
