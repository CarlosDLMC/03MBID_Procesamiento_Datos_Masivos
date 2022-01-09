from random import randint

with open('users2.txt', 'w') as users:
    lines = list()
    for i in range(20, 56):
        for j in range(randint(1, 10)):
            lines.append(f"{i},{randint(50, 250)}\n")
    users.writelines(lines)