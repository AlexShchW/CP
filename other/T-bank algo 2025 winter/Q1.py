rsm_string = input()
R_met = False

for letter in rsm_string:
    if letter == "R":
        R_met = True
    if letter == "M":
        if R_met:
            print("Yes")
        else:
            print("No")