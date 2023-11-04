##4 Queens problem for a 4x4 board. 
##The queen can move in any direction (up and down) in the same column and can 
##Each queen can attack in all directions including the diagonals.
##The movement of each queens is deterministic (i.e. you can move a queen to a specific row)

import random

graph={"Q1" : ["Q2", "Q3", "Q4"],
	   "Q2" : ["Q1", "Q3", "Q4"],
	   "Q3" : ["Q1", "Q2", "Q4"],
	   "Q4" : ["Q1", "Q2", "Q3"]
	   }

positions= [1,2,3,4]
#position={i:[1,2,3,4] for i in graph}

def generate_arcs(graph):
	arcs=[]
	for i in graph:
		#print ("i: ", i)
		for neighbour in graph[i]:
			#print("Neighbour of" ,i, "is: ", neighbour)
			if (neighbour,i) not in arcs:
				arcs.append([i,neighbour])
				print(arcs)
	return arcs

def constraint(x,y,i,j):
	print("x: ",x, "y: ",y,"queen1: ", i, "queen2: ",j," row of queen1: ",list(position.keys()).index(i), "row of queen2: ", list(position.keys()).index(j))
	if (x==y) or (abs(x-y)/(list(position.keys()).index(i)-list(position.keys()).index(j))==1):
		print("constraint detected")
		return True
	else:
		print("No constraint. Okay")
		return False

def revise(i,j):
	revised=False
	print("i,j in revise:", i,j)
	for x in position[i]:
		print("x", x)
		print("position[",i,"]", position[i])
		if len(position[j])==1:
			y=position[j][0]	
			print("y",y)
			if constraint(x,y,i,j):
				print("constraint detected")
				position[i].remove(x)
				print("now position[",i,"]", position[i])
				revised=True
	return revised

def arc_consistency(graph):
	arcs=generate_arcs(graph)
	#global position
	#position= {i:[1,2,3,4] for i in graph}
	queue=[]
	for arc in arcs:
		queue.append(arc)
	index=0
	while 1:
		global position
		position= {i:[1,2,3,4] for i in graph}
		position["Q1"]=[positions[random.randint(0,3)]]
		position["Q2"]=[positions[random.randint(0,3)]]
		print("Initialized Q1 as: ", position["Q1"])
		print("Initialized Q2 as: ", position["Q2"])

		#queue.append(["SA","NT"])
		#queue.append(["SA", "WA"])
		print("queue", queue)

		while queue:
			pair=queue.pop(0)
			i=pair[0]
			j=pair[1]
			print("i,j", i,j)
			print("positions of ", i, "and ", j, "are ", position[i], position[j])
			if revise(i,j):
				if not position[i]:
					print("DOMAIN NULLIFIED!!!! Reinitializing....")
					arc_consistency(graph)
				for neighbour in graph[i]:
					queue.append([neighbour,i])
				print("now queue", queue)
		return True


arc_consistency(graph)
print(position)