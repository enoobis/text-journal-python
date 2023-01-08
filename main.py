def main():
    # Display menu to user
    while True:
        print("Welcome to your journal!")
        print("What would you like to do?")
        print("(A)dd a new entry")
        print("(V)iew journal")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()
        
        # Add a new entry
        if choice == "A":
            add_entry()
        
        # View journal
        elif choice == "V":
            view_entries()
        
        # Quit
        elif choice == "Q":
            break
        
        # Invalid input
        else:
            print("Invalid input. Please try again.")

def add_entry():
    # Get journal entry from user
    entry = input("Enter your journal entry: ")
    
    # Write entry to file
    with open("journal.txt", "a") as f:
        f.write(entry + "\n")

def view_entries():
    # Read journal entries from file and print them to the screen
    with open("journal.txt", "r") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    main()