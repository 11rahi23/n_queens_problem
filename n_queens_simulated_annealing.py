import random, sys, copy
from optparse import OptionParser
from math import exp
try:
  import psyco
  psyco.full()
except ImportError:
  pass


Temperature=4000

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
          print ("initial board: ", self.board)
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
      print("passed mboard")
      #self.predecessor = None
      self.cost = self.calc_cost(self.mboard)
      print("self.cost:", self.cost)
      self.solution()


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
    tracker=0

    t=Temperature
    sch=0.99

    lowcost = self.calc_cost(Board)
    lowest_available= Board
    while lowcost !=0:

      lowcost = self.calc_cost(Board)
      #lowest_available= Board
      print("tracker count: ", tracker)
      t *=sch
      #move one queen at a time
      for q_row in range(4):
        for q_col in range(4):
          if Board.board[q_row][q_col] == "Q":
            print("found queen. It's in :", q_row, ",", q_col)
            #get the lowest cost by moving the queen
            for m_row in range(4):
              for m_col in range(4):
                if Board.board[m_row][m_col] != "Q":
                  tryboard=copy.deepcopy(Board)
                  tryboard.board[q_row][q_col]=0
                  tryboard.board[m_row][m_col]= "Q"
                  print("Q replace from: ", q_row, q_col, "to: ", m_row,m_col)
                  thiscost = self.calc_cost(tryboard)
                  delta = lowcost-thiscost
                  #if delta>0:
                  # lowcost=thiscost
                  # lowest_available = tryboard
                  print("board :", tryboard)
                  print("cost :", thiscost)


                  p=random.uniform(0,1)
                  print("chance value: ",p)
                  print("t value: ", t)
                  #if thiscost==0:
                  #  print("solution found")
                  #  self.total_success +=1
                  #  return tryboard, self.total_success

                  if delta>0 or p < exp(delta/t):
                    print("delta: ", delta, "random: ", p, "exp function: ", exp(-delta/t))
                    #lowcost=thiscost
                    Board =tryboard
                  tracker+=1

    print("Success!")
    print(tryboard)

    predecessor = self.mboard
    predecessor_cost = self.cost
    self.mboard = lowest_available
    self.cost = lowcost


  # def solution(self):


  #   while 1:
  #     curr_attacks = self.cost 
  #     curr_board = self.mboard
  #     self.get_lower_cost_board()
  #     if curr_attacks == self.cost:
  #       break
  #     self.total_steps +=1
  #     if self.verbocity == True:
  #       print("Current attacking queens: ", self.cost)
  #       print(self.mboard)
  #   if self.cost !=0:
  #     if self.verbocity == True:
  #         print("No solution found")
  #   else:
  #     if self.verbocity==True:
  #       print("Solution found")
  #       self.total_success +=1
  #   return self.cost 

  # def printstats(self):
  #   print ("Total Runs: ", self.total_runs)
  #   print ("Total Success: ", self.total_success)
  #   print ("Success Percentage: ", float(self.total_success)/float(self.total_runs))
  #   print ("Average number of steps: ", float(self.total_steps)/float(self.total_runs))

  def solution(self):
    tryboard, total_success = self.get_lower_cost_board(self.mboard)

    print("solution: ", tryboard)
    print("total_success: ", total_success)

if __name__ == "__main__":

  mboard = queens(10, verbocity=True)
  mboard.printstats()
















