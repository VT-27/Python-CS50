
def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    
    if ans == '42' or ans.upper()== "FORTY TWO" or ans.upper() == "FORTY-TWO":
        print("Yes")
    else:
        print("No")
main()