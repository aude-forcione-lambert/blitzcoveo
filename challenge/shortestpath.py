import numpy as np
from scipy import sparse

def norm(u,v):
	return np.abs(u[0]-v[0]) + np.abs(u[1] - v[1])
	
def inv(k, n):
	j = k%n
	i = np.floor((k - j)/n)
	return [i,j]
	
def valeur(symb):
	if symb==" ":
		return 4;
	elif symb=="%":
		return 4;
	elif symb=="$":
		return 1;
	elif symb=="C-" or symb=="%-":
		return 0;
	else:
		return 100;
	return 100;

game = [["W","W","W","W","W"],["W"," "," ", " ","W"],
["W", " ", "W", " ", "W"], ["W","W","W","W","W"]];

def poidsNN(mat):
	l = mat;
	n = len(mat);
	m = len(mat[0]);
	lf = [];
	poidsMat = [[100 for i in range(n*m)] for j in range(n*m) ]
	for i in range(n):
		for j in range(m):
			lf.append(l[i][j])
	for k in range(n*m):
		j1 = k%n
		i1 = np.floor((k - j1)/n)
		for l in range(n*m):
			j2 = l%n
			i2 = np.floor((l - j2)/n)
			if norm([i1, j1],[i2, j2]) != 1:
				continue
			else:
				poidsMat[k][l] = valeur(lf[l])
	return poidsMat

def petitChemin(u, v, game):
	n = len(game);
	m = len(game[0]);
	matrix = np.array(poidsNN(game))
	bigdad = sparse.csgraph.shortest_path(matrix, method='auto', directed=True, return_predecessors=True, unweighted=False, overwrite=False)[1]
	print(bigdad[11][13])
	print(bigdad[8][13])
	print(matrix)
	print(matrix[8][13])
	u0 = u[0]*n + u[1]
	chemin = [n*v[0] + v[1]]
	precedent = -1
	while precedent != u0:
		precedent = bigdad[u0][chemin[0]]
		chemin.insert(0,precedent)
	chemin.insert(0,u0)
	return [inv(x, n) for x in chemin]

print(petitChemin([2,1],[2,3],game))
