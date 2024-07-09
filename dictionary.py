def main():
    people = [
        {"name":"Vivek", "number":"099787676878"},
        {"name":"Tiwari", "number":"123456789"},
        {"name":"Garvisha", "number":"08876767834"},
        {"name":"Verma", "number":"8978768797897"},
    ]

    name = input("Enter Name: ")

    for person in people:
        #here, person is assigned with people dictionary automatically.
        # So for comparison and pringing we use person variable rather than people
        
        if person["name"] == name:
            print(f"Found {person["number"]}")
            break
    else:
        print("Not Found") 

main()


