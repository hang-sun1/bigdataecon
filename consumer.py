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

  def __init__(self):
    print(self.q_table)

  def consume(self, price1, price2, price3, ben1, ben2, ben3, step):
    range1 = range(0, price1, step) #range of the demand
    range2 = range(0, price2, step)
    range3 = range(0, price3, step)

    for i in range(500): #number of iterations at each price set
      if(epsilon > random()): #should we explore or not
        if i % 2 == 0:
          self.sell(random.randint(0,len(q_table[0])-1))
        else:
          self.buy_rand(ben1, ben2, ben3)
      else:
        if i % 2 == 0:
          self.sell(max(q_table[0]))
        else:
          self.buy(ben1, ben2, ben3)

      epsilon -= .001
      learning_rate -= .002
      discount_rate -= .002
      print(q_table)

  def sell(self, col):
    daily_effort -= col
    wealth += col
    q_table[0][col] = q_table[0][col] + learning_rate \
      * (daily_effort*(1 - discount_rate) + discount_rate \
      * q_table[1][max(q_table[1][max(q_table[1]):(wealth + 1)])] - q_table[0][col]) #mightbe broke

  def buy_rand(b1, b2, b3):
    if wealth == 0:
        q_table[1][0] = q_table[1][0] + learning_rate*(-1000 + \
        discount_rate*(q_table[2][max(q_table[2]):(wealth + 1)]) - q_table[1][0])
    else:
        x = random.randint(0, wealth)
        wealth -= x
        q_table[1][x] = q_table[1][x] + learning_rate*(x * b1 + \
        discount_rate*(q_table[2][max(q_table[2]):(wealth + 1)]) - q_table[1][x])

        x = random.randint(0, wealth)
        wealth -= x
        q_table[2][x] = q_table[2][x] + learning_rate*(x * b2 + \
        discount_rate*(q_table[3][max(q_table[3]):(wealth + 1)]) - q_table[2][x])

        x = random.randint(0, wealth)
        wealth -= x
        q_table[3][x] = q_table[3][x] + learning_rate*(x * b3 + \
        discount_rate*(q_table[1][max(q_table[1]):(q_table[0]\
        [max(q_table[0])] + wealth + 1)]) - q_table[1][x])

  def buy(b1, b2, b3):
    if wealth == 0:
        q_table[1][0] = q_table[1][0] + learning_rate*(-1000 + \
        discount_rate*(q_table[2][max(q_table[2]):(wealth + 1)]) - q_table[1][0])

    x = q_table[1][max(q_table[1]):wealth]
    wealth -= x
    q_table[1][x] = q_table[1][x] + learning_rate*(x * b1 + \
    discount_rate*(q_table[2][max(q_table[2]):(wealth + 1)]) - q_table[1][x])

    if wealth >= 0:
        x = q_table[2][max(q_table[2]):wealth]
        wealth -= x
        q_table[2][x] = q_table[2][x] + learning_rate*(x * b2 + \
        discount_rate*(q_table[3][max(q_table[3]):(wealth + 1)]) - q_table[2][x])

    if wealth >= 0:
        x = q_table[3][max(q_table[3]):wealth]
        wealth -= x
        q_table[3][x] = q_table[3][x] + learning_rate*(x * b3 + \
        discount_rate*(q_table[1][max(q_table[1]):(q_table[0]\
        [max(q_table[0])] + wealth + 1)]) - q_table[1][x])
