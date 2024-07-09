def main():
    
    replace()

def replace():
     txt = input("Enter text : ")
     face = txt.replace(":)", "🙂").replace(":(", "😕")
     print(face)

main()