# Uninformed-Any-Path-Search-Algorithms
Implements Depth-First and Breadth-First Search Algorithms for the N-Queens and Farmers Problems.

Sample Runs:
>>> depth_first_search(NQueensProblem(8)).solution()
[7, 3, 0, 2, 5, 1, 6, 4]
>>> breadth_first_search(NQueensProblem(8)).solution()
[0, 4, 7, 5, 2, 6, 1, 3]
>>> f = FarmerProblem((True, True, True, True), (False, False, False, False))
>>> d = depth_first_search(f); d.solution()
['FC', 'F', 'FX', 'FC', 'FG', 'F', 'FC']
>>> b = breadth_first_search(f); b.solution()
['FC', 'F', 'FG', 'FC', 'FX', 'F', 'FC']
>>> g = GraphProblem('Arab', 'Bucharest', romania_map)
>>> d = depth_first_search(g); d.solution()
['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
>>> b = breadth_first_search(g); b.solution()
['Sibiu', 'Fagaras', 'Bucharest']
