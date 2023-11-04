import random, sys, copy
from optparse import OptionParser
try:
  import psyco
  psyco.full()
except ImportError:
  pass



class board:
  def __init__(self, list=None):
    #if list==None:
    self.board = [["Q", 0, "Q", 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, "Q", "Q", 0]]
    #print(self.board)
    #for i in range(4):
    #  while 1:
    #    rand_row=random.randint(0,4-1)
    #    rand_col=random.randint(0,4-1)
    #    if self.board[rand_row][rand_col]==0:
    #      self.board[rand_row][rand_col]="Q"
    #      break

  def __repr__(self):
    mstr = ""
    for i in range(4):
      for j in range(4):
        mstr=mstr+str(self.board[i][j])+ " "
      mstr = mstr + "\n"
    return mstr

class queens:
  def __init__(self, numruns, verbocity, passed_board=None):
    self.total_runs=numruns
    self.total_success= 0
    self.total_steps=0
    self.verbocity=verbocity
    for i in range(4):
      if self.verbocity == True:
        print("=================")
        print("Board: ", i)
        print("=================")
      self.mboard = board(passed_board)
      self.cost = self.calc_cost(self.mboard)
      self.hill_solution()


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

  def get_lower_cost_board(self):
    lowcost = self.calc_cost(self.mboard)
    lowest_available= self.mboard
    #move one queen at a time
    for q_row in range(4):
      for q_col in range(4):
        if self.mboard.board[q_row][q_col] == "Q":
          #get the lowest cost by moving the queen
          for m_row in range(4):
            for m_col in range(4):
              if self.mboard.board[m_row][m_col] != "Q":
                tryboard=copy.deepcopy(self.mboard)
                tryboard.board[q_row][q_col]=0
                tryboard.board[m_row][m_col]= "Q"
                thiscost = self.calc_cost(tryboard)
                if thiscost<lowcost:
                  lowcost=thiscost
                  lowest_available = tryboard
    self.mboard = lowest_available
    self.cost = lowcost


  def hill_solution(self):
    while 1:
      curr_attacks = self.cost 
      self.get_lower_cost_board()
      if curr_attacks == self.cost:
        break
      self.total_steps +=1
      if self.verbocity == True:
        print("Current attacking queens: ", self.cost)
        print(self.mboard)
    if self.cost !=0:
      if self.verbocity == True:
          print("No solution found")
    else:
      if self.verbocity==True:
        print("Solution found")
        self.total_success +=1
    return self.cost 

  def printstats(self):
    print ("Total Runs: ", self.total_runs)
    print ("Total Success: ", self.total_success)
    print ("Success Percentage: ", float(self.total_success)/float(self.total_runs))
    print ("Average number of steps: ", float(self.total_steps)/float(self.total_runs))


if __name__ == "__main__":

  mboard = queens(100000, verbocity=True)
  mboard.printstats()
















