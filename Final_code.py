from game_data import data
from art import logo, vs
import random

print(logo)
score = 0
x = Truecd Py
while x == True:

    compare_A = random.choice(data)
    against_B = random.choice(data)

    while compare_A == against_B:
        against_B = random.choice(data)

    print(f"Compare A\n{vs}\nAgainst_B\n", )

    A_key = compare_A['follower_count']
    B_key = against_B['follower_count']

    statement_A = (
        f"{list(compare_A.values())[0]}, a {list(compare_A.values())[2]}, from {list(compare_A.values())[3]}")
    statement_B = (
        f"{list(against_B.values())[0]}, a {list(against_B.values())[2]}, from {list(against_B.values())[3]}.")


    determinant = input(f"who has more followers: {statement_A} or {statement_B}?\n")

    A_final = 0
    B_final = 0
    max_values = max([A_key, B_key])

    if max_values in list(compare_A.values()) and determinant == "A".lower():
        score += 1

        print(f"Your score is {score}, you passed")
    elif max_values in list(against_B.values()) and determinant == ("B".lower()):
        score += 1
        print(f"Your score is {score}, you passed")
    else:

        x = False
        print(f"You lose, your final score is {score}")



