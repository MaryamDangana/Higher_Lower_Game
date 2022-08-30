from game_data import data
from art import logo
print(logo)
import random

score = 0
x = True
while x == True:

    compare_A = random.choice(data)
    against_B = random.choice(data)

    if compare_A == against_B:
        against_B = random.choice(data)

    print("compare_A", compare_A)
    print("against_B", against_B)

    A_key = compare_A['follower_count']
    B_key = against_B['follower_count']

    statement_A = (
        f"{list(compare_A.values())[0]}, a {list(compare_A.values())[2]}, from {list(compare_A.values())[3]}")
    statement_B = (
        f"{list(against_B.values())[0]}, a {list(against_B.values())[2]}, from {list(against_B.values())[3]}.")

    ### part 2: Allow user to choose which key has highest value

    determinant = input(f"who has more followers {statement_A} or {statement_B}?\n")

    A_final = 0
    B_final = 0
    max_values = max([A_key, B_key])


    def find_key(input_dict):
        for i in ([list(compare_A.values())[0] for k, v in input_dict.items() if v == A_key]):
            global A_final
            A_final = i


    find_key(input_dict=compare_A)


    def find_key2(input_dict):
        for i in ([list(against_B.values())[0] for k, v in input_dict.items() if v == B_key]):
            global B_final
            B_final = i


    find_key2(input_dict=against_B)

    print(A_final, B_final, "A_final, B_final")

    print(max_values, "max values")

    if max_values in list(compare_A.values()) and determinant == A_final:

        score += 1
        print(f"Your score is {score}, you passed")
    elif max_values in list(against_B.values()) and determinant == B_final:

        score += 1
        print(f"Your score is {score}, you passed")
    else:
        x = False
        print(f"Your lose, your score is {score}")



