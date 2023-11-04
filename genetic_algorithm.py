import random, sys, copy
from optparse import OptionParser
import numpy as np

class Board:
  def __init__(self, list=None):
    #if list==None:
    self.board = [[0 for i in range(4)] for j in range(4)]
    #print(self.board)
    for i in range(4):
      while 1:
        rand_row=random.randint(0,4-1)
        # rand_col=random.randint(0,4-1)
        if self.board[rand_row][i]==0:
          self.board[rand_row][i]="Q"
          break
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
        self.population=population
        print("=================")
        print("Board: ")
        print("=================")
        self.mboard = passed_board
        print(self.mboard)
        self.cost = self.calc_cost(self.mboard)
        print("self.cost: ", self.cost)
        #self.hill_solution()

    def calc_cost(self, tboard):

        total_hcost=0
        total_dcost=0

        for i in range(4):
            for j in range(4):
                if tboard[i][j] == "Q":
                #to cancel counting self during horizontal and vertical run
                    total_hcost -=2
                    for k in range(4):
                    #count horizontally
                        if tboard[i][k] == "Q":
                            total_hcost +=1
                            #count vertically
                        if tboard[k][j] == "Q":
                            total_hcost +=1
                    #count diagonally downwards to the right
                    k, l = i+1, j+1
                    while k<4 and l<4:
                        if tboard[k][l] == "Q":
                            total_dcost +=1
                        k+=1 
                        l+=1
                    #count diagonally downwards to the left
                    k, l = i+1, j-1
                    while k<4 and l>=0:
                        if tboard[k][l] == "Q":
                            total_dcost +=1
                        k+=1
                        l-=1
                    #count diagonally upwards to the right
                    k,l = i-1, j+1
                    while k>=0 and l<4:
                        if tboard[k][l] == "Q":
                            total_dcost +=1
                        k-=1
                        l+=1
                    #count diagonally upwards to the left
                    k,l = i-1, j-1
                    while k>=0 and l>=0:
                        if tboard[k][l] == "Q":
                            total_dcost+=1
                        k-=1
                        l-=1
        return((total_hcost+total_dcost)/2)

    def fitness(self, chromosome):
        fit=int(self.maxFitness -self.calc_cost(chromosome))
        print("fitness: ", fit )
        return fit
    
    def probability(self, chromosome):
        return self.fitness(chromosome)/self.maxFitness

    def random_pick(self, population, probabilities):
        population_with_probability=zip(list(population), probabilities)
        total=sum(pr for p, pr in population_with_probability)
        r=random.uniform(0, total)
        upto = 0
        for p, pr in zip(list(population), probabilities):
            if upto + pr>=r:
                return p 
            upto+=pr 

    def reproduce(self,x,y):
        n=len(x)
        c=random.randint(1,4)
        print("c: ", c)
        x=np.array(x)
        y=np.array(y)
        t=np.hsplit(x,[c,])
        p=np.hsplit(y,[c,])
        return(np.concatenate((t[0],p[1]),axis=1))

    def mutate(self, x):
        n=len(x)
        counter=0
        c1=random.randint(0, n-1)
        c2=random.randint(0, n-1)
        m1=random.randint(0,n-1)
        m2=random.randint(0,n-1)
        for i in range(4):
            for j in range(4):
                if x[i][j]=="Q":
                    if counter==c1:
                        if x[m1][j] != "Q":
                            x[i][j]=0
                            x[m1][j] = "Q"
                    counter+=1
        return x

    def genetic_queen(self, population):
        mutation_probability = 0.03
        new_population = []
        probabilities = [self.probability(n) for n in population]
        for i in range(len(population)):
            x = self.random_pick(population, probabilities)
            print("picked x:",x) #best chromosome 1
            y = self.random_pick(population, probabilities)
            print("picked y:", y) #best chromosome 2
            child = self.reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
            if random.random() < mutation_probability:
                child = self.mutate(child)
            print("child: ",child )
            new_population.append(child)
            if self.fitness(child) == self.maxFitness:
                print("max fitness reached in population generation")

                break
        return new_population


if __name__ == "__main__":
    #nq = int(input("Enter Number of Queens: ")) #say N = 8
    fitdict= {}
    maxFitness = 6 
    population = [Board().board for _ in range(20)]
    #for i in range(100):
        #print("Board :",i, "\n", population[i].board)
        #population[i]=population[i].board 
     #   fitness=queens(population[i]).fitness(population[i])
      #  fitdict[fitness]=population[i]
        #print(population[i])
    print("entire pop : ", population)
    generation = 0
    print("generation: ", generation)
    new_population=queens(population[0]).genetic_queen(population)

       
    while not maxFitness in [queens(chromosome).fitness(chromosome) for chromosome in new_population]:
        print("=== Generation {} ===".format(generation))
        # population = [Board() for _ in range(100)]
        # i=random.randint(0,100)
        # chromosome=population[i]
        new_population=queens(new_population[0]).genetic_queen(new_population)
        print("new population: ", new_population)
        for i in new_population:
        #print("Board :",i, "\n", population[i].board)
        #population[i]=population[i].board 
            fit=queens(i).fitness(i)
            print("fitness found: ", fit)
            fitdict[fit]=i
            print("fitdict: ", fitdict[fit] )
        # print("chromosome:", i, new_population[i])
        print("population")
        print("")
        print("Maximum Fitness = {}".format(max([queens(n).fitness(n) for n in new_population])))
        generation += 1
    
    chrom_out = []
    print("Solved in Generation {}!".format(generation))
    print(fitdict[maxFitness])
        #randomly changing the index value of queen



        







