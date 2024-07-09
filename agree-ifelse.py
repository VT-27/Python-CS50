usr_input = input("Do you agree? ").lower()

if usr_input in ["y","yes"]:
    print("You agreed")
elif usr_input in ["n","no"]:
    print("You disagreed")
else:
    print("Incorrect selection")

for _ in range(3):
    print("loop", _)