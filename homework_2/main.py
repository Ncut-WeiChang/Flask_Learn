import random

num = []
print(len(num))
while len(num) != 8:
    if len(num) == 0:
        num.append(random.randint(1, 15))
    else:
        cache = random.randint(1, 15)
        count = 0
        for item in num:
            if item == cache: count += 1

        if count < 1:
            num.append(cache)

print(*num)
