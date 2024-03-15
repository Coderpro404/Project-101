import random
response = input("Do you want to roll a dice?")
if response == "yes":
    response = "y"
if response == "no":
    response = "n"    

while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[-----]")
    output=input("enter yes to continue or enter no to exit")
    if output == "yes":
        response ="y"
    else:
        response ="n"                                 