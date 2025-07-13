from random import randint

def coin_flip():
    if randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

flips_taken = 0

for trial in range (10_000):
    # a trial requires at least two flips
    flip_counter = 0
    found_heads = False
    fount_tails = False
    found_both = False

    while found_both == False:
        flip_counter = flip_counter + 1
        flip = coin_flip()

print(flip_counter)

