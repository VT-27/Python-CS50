def get_int(prompt):    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def main():
    user_input = []
    cc_no = get_int("Enter the card number: ")

    ccnostr = str(cc_no)
    
    if (len(ccnostr) == 16):
        print("Valid Card number")
    else:
        print("Invalid Card number")

    for i in range(0,len(ccnostr),2):
        odd_string = int(ccnostr)
        #multiply by 2
        odd_string[i] *= 2
    
    print(odd_string)
    



main()
# incomplete Code
#4003600000000014