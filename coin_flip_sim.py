import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

flip = coin_flip()

print(flip)

# a trial consists of at least two coin flips
# the coin is flipped repeatedly until it lands on heads
# or tails at least one time each
# after first flip cotinuing flipping until lands on the other side
# each flip is an independent event
# it is the same as flipping several coins at the same time
# we want an average, a sum divided by total
# what is the average number of flips where this condition is true
# condition one: you have to flip at least twice, the smallest number of
# flips must be two
# probability decreases of having a run of a particular set of flips
# landing on the same side 1/2 x 1/2 etc.
# we have a function that does flips
# we use for loop to run 10,000 trials, not 10,000 flips like before
# 10,000 trials where each trial has at least two flips
# we need to design a loop that repeatedly flips the coin until it lands
# on the other side
# when we flip the coin it will be heads or tails
# then flip again
# if first flip was heads and the second flip was heads flip again
# if the first flip was heads and second flip was tails stop
# initialize the trial counter at 0 and increment only one after the first fliop
# if first flip was tails and second flip was tails continue
# if first flip was tails and second flip was heads stop
# continue if the flip is same as first flip
# break if flip is different from first flip



flip_num = 0
heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if coin_flip() == "heads":
        flip_num = flip_num + 1
    else:
        break


print(flip_num)
