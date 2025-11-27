import random

p = 0.5 # fair coin
N = int(input("Number of Trials "))

game = [] # empty list
win = 0 # accumulator

for i in range(N):
    coin = 0
    while coin != 1:
        r = random.uniform(0, 1)
        if r >= p:
            coin = 0
        else:
            coin = 1
        game.append(coin)
    L = len(game)
    if L % 2 == 1:
        win += 1
    game = []
    print(win/N)
