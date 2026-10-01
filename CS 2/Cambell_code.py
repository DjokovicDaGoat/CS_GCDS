
"""
Name: G.Campbell
Description: Example of a string function(s)
Bugs: None known
Date: 9/17/2026
Bonuses:
Log: Initial version: 9/10/2026
     9/17/2026 Updated to include a menu and character search functionality


"""

def my_index(data, char):
    """
    Description: Return the index of the first occurrence of char in data.
    If char is not found or char is empty, return -1.
    Uses a while loop and does not raise errors.

    Parameters:
    - data: the string to search in
    - char: a single-character string to look for

    Returns:
    - int: index of first match, or -1 if not found
    """
   
    if not char:
        return -1
    i = 0
    while i < len(data):
        if data[i] == char:
            return i
        i += 1
    return -1

def main():
   
    while True:
       
        data = input("Enter the data string: ")
       
        print("\nMenu:")
        print("1) Search for a character")
        print("X) Quit")
        choice = input("Choose an option: ")
        if choice == "X":
            print("Goodbye.")
            break
        if choice == "1":
           
            char = input("Enter the character to look for: ")
            idx = my_index(data, char)
            print(f"Result: {idx}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()