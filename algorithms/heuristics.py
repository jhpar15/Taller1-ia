from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    
    x1, y1 = state
    x2, y2 = problem.goal 
    return abs(x1 - x2) + abs(y1 - y2)



def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    x1, y1 = state
    x2, y2 = problem.goal
    
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    position, survivors_grid = state

    survivors = survivors_grid.asList()

    # Revisamos si quedan sobrevivientes en el mapa
    if not survivors:
        return 0

    x, y = position

    #Buscamos el subreviviente mas cercano segun la distancia manhatan 
    min_distance = min(
        abs(x - sx) + abs(y - sy)
        for sx, sy in survivors
    )

    return min_distance
