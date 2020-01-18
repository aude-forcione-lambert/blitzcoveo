function norme(u,v):
    return abs(u.x-v.x)+abs(u.y-v.y);

class dist:
    def __init__(self):

    def danger(self,queue,ennemis):
        min = 100;
        for q in queue:
	    for e in ennemis
		candidat = norme(q,e);
		if candidat<min:
		    min=candidat;
	return min;

    def surete(self,vaisseau,maison):
	min = 100;
	for m in maison:
	    candidat = norme(vaisseau,m)
	    if candidat<min:
		min=candidat;
	return min;
