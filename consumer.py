import random

class consumer:
  effort = 4 #amount they could work
  daily_effort = effort
  wealth = 0

  q_table = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]] #holds the benefit of any given decision

  epsilon = 1 #rate at which it randomly explores
  learning_rate = .8 #rate at which it values new data
  discount_rate = .2 #rate at which it values future benefit

  priceg1 = 1
  priceg2 = 1
  priceg3 = 1

  curve1 = []
  curve2 = []
  curve3 = []

  def __init__(self):
    print(self.q_table)

  def consume(self, price1, price2, price3, ben1, ben2, ben3, step):
    range1 = range(0, price1, step) #range of the demand
    range2 = range(0, price2, step)
    range3 = range(0, price3, step)

    for i in range1:
      for j in range2:
        for k in range3:
          self.priceg1 = i
          self.priceg2 = j
          self.priceg2 = k
          for i in range(500): #number of iterations at each price set
            if(self.epsilon > random.random()): #should we explore or not
              if i % 2 == 0:
                self.sell(random.randint(0,len(self.q_table[0])-1))
              else:
                self.buy_rand(ben1, ben2, ben3)
            else:
              if i % 2 == 0:
                self.sell(self.max_col(self.q_table[0]))
              else:
                self.buy(ben1, ben2, ben3)
            self.curve1.append((i, max_col(q_table[1])))
            self.curve2.append((j, max_col(q_table[2])))
            self.curve3.append((k, max_col(q_table[3])))
            self.epsilon -= .001
            self.learning_rate -= .002
            self.discount_rate -= .002
            print(self.q_table)
            print()

  def sell(self, col):
    self.daily_effort -= col
    self.wealth += col
    self.q_table[0][col] = self.q_table[0][col] + self.learning_rate * (self.daily_effort*(1 - self.discount_rate) + self.discount_rate * self.q_table[1][self.max_col(self.q_table[1][:(self.wealth + 1)])] - self.q_table[0][col]) #mightbe broke
    return 0

  def buy_rand(self, b1, b2, b3):
    if self.wealth == 0:
        self.q_table[1][0] = self.q_table[1][0] + self.learning_rate*(-1000 + \
        self.discount_rate*(self.q_table[2][self.max_col(self.q_table[2][:(self.wealth + 1)])] - self.q_table[1][0]))
    else:
        x = random.randint(0, self.wealth)
        if x > 4:
            x = 4
        self.wealth -= x*self.priceg1
        print("line 57", x, self.wealth)
        self.q_table[1][x] = self.q_table[1][x] + self.learning_rate*(x * b1 + \
        self.discount_rate*(self.q_table[2][self.max_col(self.q_table[2][:(self.wealth + 1)])] - self.q_table[1][x]))

        if x == 0:
            return

        x = random.randint(0, self.wealth)
        if x > 4:
            x = 4
        self.wealth -= x*self.priceg2
        self.q_table[2][x] = self.q_table[2][x] + self.learning_rate*(x * b2 + \
        self.discount_rate*(self.q_table[3][self.max_col(self.q_table[3][:(self.wealth + 1)])] - self.q_table[2][x]))

        if x == 0:
            return

        x = random.randint(0, self.wealth)
        if x > 4:
            x = 4
        self.wealth -= x*self.priceg3
        print("wealth",self.wealth)
        self.q_table[3][x] = self.q_table[3][x] + self.learning_rate*(x * b3 + \
        self.discount_rate*(self.q_table[1][self.max_col(self.q_table[1][:\
        self.max_col(self.q_table[0]) + self.wealth + 1])]) - self.q_table[1][x])

  def buy(self, b1, b2, b3):
    if self.wealth == 0:
        self.q_table[1][0] = self.q_table[1][0] + self.learning_rate*(-100 + \
        self.discount_rate*(self.q_table[2][self.max_col(self.q_table[2][:(self.wealth + 1)])] - self.q_table[1][0]))

    print(self.wealth)
    x = self.max_col(self.q_table[1][:self.wealth + 1])
    self.wealth -= x*self.priceg1
    self.q_table[1][x] = self.q_table[1][x] + self.learning_rate*(x * b1 + \
    self.discount_rate*(self.q_table[2][self.max_col(self.q_table[2][:(self.wealth + 1)])] - self.q_table[1][x]))

    if self.wealth >= 0:
        x = self.max_col(self.q_table[2][:self.wealth + 1])
        self.wealth -= x*self.priceg2
        self.q_table[2][x] = self.q_table[2][x] + self.learning_rate*(x * b2 + \
        self.discount_rate*(self.q_table[3][self.max_col(self.q_table[3][:(self.wealth + 1)])] - self.q_table[2][x]))

    if self.wealth >= 0:
        x = self.max_col(self.q_table[3][:self.wealth + 1])
        self.wealth -= x*self.priceg3
        print("line 101: ", x,self.wealth)
        self.q_table[3][x] = self.q_table[3][x] + self.learning_rate*(x * b3 + \
        self.discount_rate*(self.q_table[1][self.max_col(self.q_table[1][:\
        self.max_col(self.q_table[0]) + self.wealth + 1])]) - self.q_table[1][x])

  def max_col(self, stuff):
    max = stuff[0]
    max_col_index = 0
    for i in range(1, len(stuff)):
      if stuff[i] > max:
        max = stuff[i]
        max_col_index = i

    return max_col_index

    def get_curve1(self):
        pass
