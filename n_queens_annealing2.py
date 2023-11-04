import random, sys, copy
from optparse import OptionParser
from math import exp
try:
  import psyco
  psyco.full()
except ImportError:
  pass

temperature = 4000

class board:
  def __init__(self, list=None):
    #if list==None:
    self.board = [[0 for i in range(4)] for j in range(4)]
    #print(self.board)
    for i in range(4):
      while 1:
        rand_row=random.randint(0,4-1)
        rand_col=random.randint(0,4-1)
        if self.board[rand_row][rand_col]==0:
          self.board[rand_row][rand_col]="Q"
          print("Initial board: ", self.board)
          break

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

  def get_lower_cost_board(self, Board):
    lowcost = self.calc_cost(Board)
    print("came to lowcost with board: ")
    print(Board)
    lowest_available= Board
    #move one queen at a time
    for q_row in range(4):
      for q_col in range(4):
        if Board.board[q_row][q_col] == "Q":
          print("Q found at :", q_row, q_col)
          #get the lowest cost by moving the queen
          for m_row in range(4):
            for m_col in range(4):
              if Board.board[m_row][m_col] != "Q":
                tryboard=copy.deepcopy(Board)
                tryboard.board[q_row][q_row]=0
                tryboard.board[m_row][m_col]= "Q"
                print("Q replaced from: ", q_row, q_col, "to :", m_row, m_col)
                thiscost = self.calc_cost(tryboard)
                print("cost after replacement: ", thiscost)

                if thiscost<lowcost:
                  lowcost=thiscost
                  lowest_available = tryboard
                  print("replacement passed after comparison. proceeding..")

    low_board = lowest_available
    low_cost = lowcost
    print("lowest_available board: ", low_board, "with cost: ", low_cost)

    return low_board, low_cost


  def hill_solution(self):
    t=temperature
    sch = 0.99
    curr_attacks = self.cost 
    curr_board = self.mboard
    while t>0:
      t*=sch
      
      low_board, low_cost  = self.get_lower_cost_board(curr_board)
      print("curr_attacks:", curr_attacks, "low_cost:", low_cost)
      delta=curr_attacks-low_cost
      p=random.uniform(0,1)
      if low_cost == 0:
        print("solution found")
        print(low_board)
        self.total_success +=1
        return
      if delta>0 or p<exp(delta/t):
        print("delta: ", delta, "random: ", p, "t: ",t, "exp function: ", exp(-delta/t))
        curr_board = low_board
        curr_attacks = low_cost
        print("Board changed to :", curr_board)
      self.total_steps +=1
      if self.verbocity == True:
        print("Current attacking queens: ", curr_attacks)
        print(curr_board)
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
















