#CRISTALINA NGUYEN
'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import heapq
import unittest

def get_sol(current):
    solution = []
    while current.parent is not None:
        solution.append(current.action)
        current = current.parent
    solution.reverse()
    return solution

# def goal_test(self, state):
#         for g in self.goals:
#             if state == g:
#                 return True
#         return False

def heuristic(s, g):
    vals = []
    for i in range(len(g)):
        distance = abs(s[0] - g[i][0]) + abs(s[1] - g[i][1])
        vals.append(distance)
    return min(vals)

def solve (problem, initial, goals):
    goalz = []

    for (col, row) in goals: #keeping track of goals visited
        goalz.append((col, row))

    frontier = []
    visited = set() #keeping track of nodes visited - (array of tuples ((x, y),(true/false)))

    heapq.heappush(frontier, SearchTreeNode(initial, None, None, 0, heuristic(initial, goalz)))

    while len(frontier) > 0:
        current = heapq.heappop(frontier)
        if current.state in goals:
            if current.state not in goalz:
                continue
            goalz.remove(current.state)
            for i in range(len(frontier)):
                heapq.heappop(frontier)

            heapq.heappush(frontier, current)
            if len(goalz) is 0:
                return get_sol(current)

        visited.add((current.state, current.action))

        for child in problem.transitions(current.state):
            child_cost = current.totalCost + child[1]
            child_heuristic = heuristic(child[2], goalz)
            if (child[2], child[0]) in visited:
                continue
            heapq.heappush(frontier, SearchTreeNode(child[2], child[0], current, child_cost, child_heuristic))
    return None

class PathfinderTests(unittest.TestCase):

    def test_maze1(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals   = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze2(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals   = [(3, 3),(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze3(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.MMX",
                "X...M.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals   = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze4(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals   = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln == None)

    def test_maze5(self):
        maze = ["XXXXXXX",
                "X..M..X",
                "XXXXXXX",
                "X.M...X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 3)
        goals   = [(1, 1), (4, 2)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln == None)

    def test_maze6(self):
        maze = ["XXXXXXX",
                "X...XXX",
                "X.XX..X",
                "X.....X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (4, 3)
        goals   = [(1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 5)

    def test_maze7(self):
        maze = ["XXXXXXX",
                "X.....X",
                "XX.XXXX",
                "X.....X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 3)
        goals   = [(1, 1),(2, 1),(3, 1),(5, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln == None)

    def test_maze7(self):
        maze = ["XXXXXXXXXXXX",
                "X...MMMM...X",
                "XX.XXXXXXXXX",
                "X.....MMXXXX",
                "XXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 3)
        goals   = [(7, 1),(2, 2)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 18)

    def test_maze9(self):
        maze = ["XXXXX",
                "X...X",
                "XXXXX",
                "X...X",
                "XXXXX"]
        problem = MazeProblem(maze)
        initial = (2, 3)
        goals   = [(1, 1),(2, 1),(3, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln == None)

    def test_maze10(self):
        maze = ["XXXXXXXX",
                "X..MMM.X",
                "XX....XX",
                "X..M.M.X",
                "XXXXXXXX"]
        problem = MazeProblem(maze)
        initial = (6, 1)
        goals   = [(2, 1),(2, 3),(4, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze11(self):
        maze = ["XXXXX",
                "XMXMX",
                "XMXXX",
                "XMMMX",
                "XXXXX"]
        problem = MazeProblem(maze)
        initial = (3, 3)
        goals   = [(1, 1),(1, 2)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze12(self):
        maze = ["XXXXX",
                "XM.MX",
                "XXXXX",
                "XM.MX",
                "XXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(2, 3)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln == None)

    def test_maze13(self):
        maze = ["XXXXXXXXXXX",
                "XM..X...XMX",
                "XMMMMMMMXXX",
                "XMMMMMMM.MX",
                "XXXXXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(8, 3),(5, 2)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 21)


if __name__ == '__main__':
    unittest.main()
