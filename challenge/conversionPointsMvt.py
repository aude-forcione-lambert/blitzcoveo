def convert(liste,dirInit):
	mvt=[];
	n = len(liste)-1;
	dir = dirInit;
	for i in range(n):
		u=liste[i];
		v=liste[i+1];
		vect=[v[0]-u[0],v[1]-u[1]];
		if vect==[1,0]:
			if dir==0:
				mvt.append("FORWARD");
			elif dir==1:
				mvt.append("TURN_RIGHT");
			elif dir==3:
				mvt.append("TURN_LEFT");
		if vect==[0,1]:
			if dir==1:
				mvt.append("FORWARD");
			elif dir==2:
				mvt.append("TURN_RIGHT");
			elif dir==0:
				mvt.append("TURN_LEFT");
		if vect==[-1,0]:
			if dir==2:
				mvt.append("FORWARD");
			elif dir==3:
				mvt.append("TURN_RIGHT");
			elif dir==1:
				mvt.append("TURN_LEFT");
		if vect==[0,-1]:
			if dir==3:
				mvt.append("FORWARD");
			elif dir==0:
				mvt.append("TURN_RIGHT");
			elif dir==2:
				mvt.append("TURN_LEFT");
	return mvt;