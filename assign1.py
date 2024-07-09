# write a program that recreates a half-pyramid using hashes (#) for blocks,

def get_int(prompt):    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            

def main():
    sizeofbricks = get_int("Enter the size: ")


    # print("Reverse Pyramid")
    # for i in range(sizeofbricks,0,-1):
    #     for j in range(i,0,-1):
    #         print("#", end="")
    #     print()

    # print("Forward Pyramid")
    # for k in range(1, sizeofbricks+1, 1):
    #     for l in range(k):
    #         print("#", end="")
    #     print()

    print("Trial Pyramid 1")
    for k in range(1,sizeofbricks+1):
        space = " " * (sizeofbricks - k)
        hash = "#" * k
        print(space + hash + " " + hash + space)

    # print("Trial Pyramid 2")
    # for j in range(1,sizeofbricks+1):
    #     space = " " * (sizeofbricks - j)
    #     hash = "#" * j
    #     print(hash + space)

main()