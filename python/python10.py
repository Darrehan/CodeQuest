# coding for random module
import random
names=["rehan","arman","sultan",  "khan","arif"]
total_size=len(names)
# here list index start from 0 to 4
random_number=random.randint(0,total_size-1)
print(f"{names[random_number]} is going to buy the meal today!")
for name in range(0,total_size):
    print(name)