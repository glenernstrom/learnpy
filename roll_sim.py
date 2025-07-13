from random import randint

def roll():
    return randint(1, 6)
    
num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total = total + roll()

avg_roll = total / num_rolls

print(f"For a six-sided die, the average result of {num_rolls} rolls is {avg_roll:.1f}.")
