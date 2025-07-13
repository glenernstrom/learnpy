# Coint Toss Simulation

# On average, how many flips are needed for
# sequence of coin flips to contain both heads and tails?

from random import randint

# Create a function for one experiment

def coin_flip():
    """ Randomly return 'heads' or tails'."""
    if randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

flips = 0
num_trials = 10_000

for trial in range(num_trials):
    if coin_flip() == "heads":
        flips = flips + 1
        while coin_flip() == "heads":
            # keep doing coin_flip until "tails" is
            # returned
            flips = flips + 1
        # Once coin_flip() returns "tails", the loop will exit,
        # but we need to add one more to flips to track the
        # last flip that generated "tails"
        flips = flips + 1
    else:
        # if coin_flip() returned "tails" on the first flip.
        # Increment the number of flips by 1
        flips = flips + 1
        while coin_flip() == "tails":
            # keep flipping the coin until "heads" is
            # returned
            flips = flips + 1
            # Once coin_flip() returns "heads", the loop will exit,
            # but we need to add one more to flips to track the
            # last flip that generated "heads"
        flips = flips + 1

avg_flips_per_trial = flips /num_trials
print(f"The total number of flips were {flips} in {num_trials} trials.")
print(f"The average number of flips per trial is {avg_flips_per_trial}.")
        
