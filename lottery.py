import random

# powerball_main = [1, 69]
# powerball_number = [1, 25]

for j in range(10):
    full_set = []
    for i in range(5):
        num = random.randrange(1, 69, 1)
        while num in full_set:
            num = random.randrange(1, 69, 1)
        full_set.append(num)
    full_set.sort()
    full_set.append(random.randrange(1, 25, 1))

    print(full_set)
