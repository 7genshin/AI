from sys import maxsize 
from itertools import permutations
V = 4
def tsp(graph, s): 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 
	mp = maxsize 
	np=permutations(vertex)
	for i in np:
		cp = 0
		k = s 
		for j in i: 
			cp += graph[k][j] 
			k = j 
		cp += graph[k][s] 

		mp = min(mp, cp) 
		
	return mp
 
if __name__ == "__main__": 
	graph = [[0, 5, 15, 20], [15, 0, 35, 25], 
			[15, 20, 0, 30], [35, 25, 30, 0]] 
	s = 0
	print(tsp(graph, s))

