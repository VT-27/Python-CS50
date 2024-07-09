def main():
    x = get_input("Enter fuel: ")
    

def get_input(prompt):
    while True:
        try:
            x = str(input(prompt))
            parts = x.split('/')
            numerator = int(parts[0])
            denominator = int(parts[1])
            res = int((numerator/denominator) * 100)
                        
            if (res == 100):
                return print('F')
            elif (res == 0):
                return print('E')
            elif (numerator > 4):
                raise invalidNumerator
            else:
                return print(res,'%')

        except ZeroDivisionError:
            print("Denominator cannot be 0")

        except ValueError:
             print("Only Integer expected")

        except invalidNumerator:
            print("Numerator cannot be greater than 4")

class invalidNumerator(Exception):
    pass

main()