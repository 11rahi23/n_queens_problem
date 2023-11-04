import random, sys, copy
from optparse import OptionParser
import numpy as np
from math import exp

class Board:
  def __init__(self, list=None):
    #if list==None:
    self.board= [[0,0,0,0],[0,0,0,0], [0,0,0,0], ["Q", "Q", "Q", "Q"]]
    # self.board = [[0 for i in range(4)] for j in range(4)]
    #print(self.board)
    # for i in range(4):
    #   while 1:
    #     rand_row=random.randint(0,4-1)
    #     rand_col=random.randint(0,4-1)
    #     if self.board[rand_row][rand_col]==0:
    #       self.board[rand_row][rand_col]="Q"
    #       break
    def __repr__(self):
        mstr = ""
        for i in range(4):
            for j in range(4):
                mstr=mstr+str(self.board[i][j])+ " "
            mstr = mstr + "\n"
        return mstr

class queens:
    def __init__(self, passed_board):
        #self.total_runs=numruns
        self.total_success= 0
        self.total_steps=0
        #self.verbocity=verbocity
        self.maxFitness=4*3/2
        #self.population=population
        print("=================")
        print("Board: ")
        print("=================")
        self.mboard = Board(passed_board)
        print(self.mboard.board)
        self.cost = self.calc_cost(self.mboard)
        print("self.cost: ", self.cost)
        #self.hill_solution()

    def calc_cost(self, tboard):
        total_hcost=0
        total_dcost=0

        for i in range(4):
            for j in range(4):
                if tboard.board[i][j] == "Q":
                #to cancel counting self during horizontal and vertical run
                    total_hcost -=2
                    for k in range(4):
                    #count horizontally
                        if tboard.board[i][k] == "Q":
                            total_hcost +=1
                            #count vertically
                        if tboard.board[k][j] == "Q":
                            total_hcost +=1
                    #count diagonally downwards to the right
                    k, l = i+1, j+1
                    while k<4 and l<4:
                        if tboard.board[k][l] == "Q":
                            total_dcost +=1
                        k+=1 
                        l+=1
                    #count diagonally downwards to the left
                    k, l = i+1, j-1
                    while k<4 and l>=0:
                        if tboard.board[k][l] == "Q":
                            total_dcost +=1
                        k+=1
                        l-=1
                    #count diagonally upwards to the right
                    k,l = i-1, j+1
                    while k>=0 and l<4:
                        if tboard.board[k][l] == "Q":
                            total_dcost +=1
                        k-=1
                        l+=1
                    #count diagonally upwards to the left
                    k,l = i-1, j-1
                    while k>=0 and l>=0:
                        if tboard.board[k][l] == "Q":
                            total_dcost+=1
                        k-=1
                        l-=1
        return((total_hcost+total_dcost)/2)

    def fitness(self, chromosome):
        fit=int(self.maxFitness -self.calc_cost(chromosome))
        print("fitness: ", fit )
        return fit
    
    # def probability(self, chromosome):
    #     return self.fitness(chromosome)/self.maxFitness

    # def random_pick(self, population, probabilities):
    #     population_with_probability=zip(list(population), probabilities)
    #     total=sum(p for pr, p in population_with_probability)
    #     r=random.uniform(0, total)
    #     upto = 0
    #     for p, pr in zip(list(population), probabilities):
    #         if upto + pr>=r:
    #             return p 
    #         upto+=pr 

    # def reproduce(self,x,y):
    #     n=len(x.board)
    #     c=random.randint(1,4)
    #     print("c: ", c)
    #     x=np.array(x.board)
    #     y=np.array(y.board)
    #     t=np.hsplit(x,[c,])
    #     p=np.hsplit(y,[c,])
    #     return(np.concatenate((t[0],p[1]),axis=1))

    # def mutate(self, x):
    #     n=len(x.board)
    #     counter=0
    #     c1=random.randint(0, n-1)
    #     c2=random.randint(0, n-1)
    #     m1=random.randint(0,n-1)
    #     m2=random.randint(0,n-1)
    #     for i in len(4):
    #         for j in len(4):
    #             if x.board[i][j]=="Q":
    #                 if counter==c1:
    #                     if x.board[m1][m2] != "Q":
    #                         x.board[i][j]=0
    #                         x.board[m1][m2] = "Q"
    #                 counter+=1
    #     return x

    # def genetic_queen(self, population):
    #     mutation_probability = 0.03
    #     new_population = []
    #     probabilities = [self.probability(n) for n in population]
    #     for i in range(len(population)):
    #         x = self.random_pick(population, probabilities)
    #         print("picked x:",x.board) #best chromosome 1
    #         y = self.random_pick(population, probabilities)
    #         print("picked y:", y.board) #best chromosome 2
    #         child = self.reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
    #         if random.random() < mutation_probability:
    #             child = self.mutate(child)
    #         print("child: ",child )
    #         new_population.append(child)
    #         if self.fitness(child) == self.maxFitness: break
    #     return new_population


    def get_random_children(self, Board):
        lowcost = self.calc_cost(Board)
        lowest_available= Board
        #move one queen at a time
        q_row =random.randint(0,3)
        q_col =random.randint(0,3)

        while Board.board[q_row][q_col] != "Q":
            q_row =random.randint(0,3)
            q_col =random.randint(0,3)

        if Board.board[q_row][q_col] == "Q":
            print("found queen. It's in :", q_row, ",", q_col)
            m_row =random.randint(0,3)
            m_col =random.randint(0,3)
            while Board.board[m_row][m_col] != 0:
                m_row =random.randint(0,3)
                m_col =random.randint(0,3)
    
        
            child_board=copy.deepcopy(Board)
            child_board.board[q_row][q_col]=0
            child_board.board[m_row][m_col]= "Q"
            child_cost = self.calc_cost(child_board)
            fitness = self.fitness(child_board)
            print("random child of board:", child_board.board)
            print("cost: ", child_cost, "and fitness: ", fitness)

            
        return child_board,child_cost
    




if __name__ == "__main__":
    #nq = int(input("Enter Number of Queens: ")) #say N = 8
    t=4000
    sch=0.99
    #init_board=[[0,0,0,0], [0,0,0,0], [0,0,0,0],["Q", "Q", "Q", "Q"]]
    init_board=Board()
    Queens=queens(init_board)
    init_cost = Queens.calc_cost(init_board)
    #lowest_available= init_board
    fitdict= {}
    maxFitness = 6
    fitness=Queens.fitness(init_board) 
    curr=init_board
    curr_cost=init_cost
    generation = 0

    while t>0:
        print("Generation: ", generation)
        t *=sch
        child_board, child_cost = Queens.get_random_children(curr)

        delta = curr_cost-child_cost
        #if delta>0:
        # lowcost=thiscost
        # lowest_available = tryboard
        print("board :", child_board.board)
        print("cost :", child_cost)


        p=random.uniform(0,1)
        print("chance value: ",p)
        print("t value: ", t)
        #if thiscost==0:
        #  print("solution found")
        #  self.total_success +=1
        #  return tryboard, self.total_success

        if child_cost == 0:
            print("Solution found!!")
            print(child_board.board)
            break

        if delta>0 or p < exp(delta/t):
            print("delta: ", delta, "random: ", p, "exp function: ", exp(-delta/t))
            #lowcost=thiscost
            curr = child_board
            generation+=1     




        #population = [Board() for _ in range(100)]
        #i=random.randint(0,3)
        #chromosome=population[i]
        #for i in range(100):
        #print("Board :",i, "\n", population[i].board)
        #population[i]=population[i].board 
        #    fitness=queens(population[i]).fitness(population[i])
        #   fitdict[fitness]=population[i]
        #print("chromosome:", i, population[i].board)
        #print("population")
        #print("")
        #print("Maximum Fitness = {}".format(max([queens(chromosome).fitness(n) for n in population])))
        
    
    #chrom_out = []
    #print("Solved in Generation {}!".format(generation-1))
    #print(fitdict[6].board)
        #randomly changing the index value of queen



        







