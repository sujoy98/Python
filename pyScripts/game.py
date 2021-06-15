import random


def win_logic(comp, your):
    if comp == your:
        return None
    elif comp == 'R':
        if your == 'P':
            return True
        elif your == 'S':
            return False
    elif comp == 'P':
        if your == 'S':
            return True
        elif your == 'R':
            return False
    elif comp == 'S':
        if your == 'R':
            return True
        elif your == 'P':
            return False


print('Comp turn choosing among Rock(R), Paper(P), Scissors(S)')
randNum = random.randint(1, 3)
if randNum == 1:
    comp = 'R'
elif randNum == 2:
    comp = 'P'
elif randNum == 3:
    comp = 'S'
your = input("Yours turn choosing among\n\n Rock(R)\n Paper(P)\n Scissors(S)\n")
gameResult = win_logic(comp, your)
print(f"Comp choose {comp}")
print(f"You choose {your}")
if gameResult is None:
    print("Game is a tie")
elif gameResult:
    print("You win!")
else:
    print("Comp win!")
