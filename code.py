

compare_A={'w': 1, "s": 24, 'wx': 33}
against_B={'on': 10, "bs": 2, 'ef': 330}

## part 1: creating a function that returns shufled list
import random
def key_returner(A):
    return(random.choice(list(A.keys())))
A_key=key_returner(compare_A)
B_key=key_returner(against_B)



### part 2: Allow user to choose which key has highest value
determinant=input(f"who has more followers {A_key} or {B_key}?\n")

##part 3: comparison to know which key has highest value

my_list=[]
max_value2=0
def max_checker():
    A1_value=compare_A.get(A_key)
    B1_value=against_B.get(B_key)
    my_list.append(A1_value)
    my_list.append(B1_value)
    global max_value2
    max_value2=(max(my_list))

max_checker()
print(max_value2)
print(my_list)


def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)
A_final=find_key(input_dict=compare_A, value=max_value2)
B_final=find_key(input_dict=compare_A, value=max_value2)

if determinant==A_final or determinant==B_final:
    print("you win")
else:
    print("You lose")

    # return(x for x, y in against_B.items() if y==max_value)

