import random    


"""
Name: Joaquin Urrutia
Description: Example of a string function(s)
Bugs: None known
Date: 9/29/2026
Bonuses: Return full-name as a sorted array of characters, build a menu, return bollean if name contains a title/distinction, subtotals of each consonant
Log: Initial version: 9/29/2026
"""


list_firstname = []
list_lastname = []                                                    #empty name of list_last anem


def add_user_name_list(list_firstname, list_lastname):
    '''
    Adds the first name and last name into an empty list list_firstname and list_last name

    Args
        list_firstname: The empty list
        list_lastname: The empty list

    Returns
        Names are Saved
    '''

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    list_firstname.append(first_name)
    list_lastname.append(last_name)

    print("Names are saved!")


def display_names(list_firstname, list_lastname):
    '''
    Displays all saved names in list_firstname and list_lastname

    Args:
        list_firstname: A list that may have a firstname depending if the user initially added their name to the list
        list_lastname: A list that may have a lastname depending if the user initially added their name to the list

    Returns:
        Prints saved names
    '''
    if len(list_firstname) == 0:                                        #if the the length of whats inside list_firstname, 
        print("No names have been saved.")                              #print no names detected
    else:                                                               #if there is a value that is not 0
        print("Saved names:")                                           #print saved names:
        print("|First Names| |Last Names|")                             #print |First Names| |Last Names|
        for first, last in zip(list_firstname, list_lastname):          #Zip pairs last name and first name together
            print(f"{first}       {last}")


def count_vowels(user_word):
    '''
    Counts the amount of vowels in user_word while also showing the frequency

    Args:
        user_word: the users full name 

    Returns
        The frequency of vowels and the sum of vowels
    '''
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}                  #lists all the values of vowels while setting their individual counter to 0

    for letter in user_word.lower():                                    #converts user_word to only lowercase letters to make the letters match with vowels list
        if letter in vowels:                                            #if their is a letter in user_word for vowels
            vowels[letter] += 1                                         #add to counter of the individual letter counter

    print(f"Total vowels: {sum(vowels.values())}")                      #gets the num of the intesgers only. Values excludes the letters so the computer doesnt add letters.


def uppercase(text):
    '''
    Prints user_word in all capital letters

    Args:
        text: the users full name

    Returns:
        the user_word in capital letters
    '''
    result = ""                                                          #creates an empty list
    for char in text:                                                    #goes throuhg each indivudal letter
        if 'a' <= char <= 'z':                                           #checks if the letters in text is lowercase from a to z
            result = result + chr(ord(char) - 32)                        #Gets all the version of the uppcases using the ASCII number. Subracting 32 is to flip lowercase to uppercase. (interesting to learn that binary code in ASCII represents all the keys on a keyboard, making it be used as a universal language)
        else:
            result = result + char                                       #adds the name in uppercase to the empty result string
    return result                                                        #saves result


def lowercase(text):
    '''
    Converts user_word into lowercase letters

    Args:
        text: the users full name

    Returns:
        the user_word in lowercase letters
    '''
    result = ""                                                           #creates an empty list
    for char in text:                                                     #goes throuhg each indivudal letter
        if 'A' <= char <= 'Z':                                            #checks if the letters in text is lowercase from a to z 
            result = result + chr(ord(char) + 32)                         #Gets all the version of the uppcases using the ASCII number. Subracting 32 is to flip lowercase to uppercase. (interesting to learn that binary code in ASCII represents all the keys on a keyboard, making it be used as a universal language)
        else:
            result = result + char                                        #adds the name in uppercase to the empty result string
    return result                                                         #saves result

                                                                             
def reverse(user_word):
    '''
    Reverses the user_word

    Args:
        user_word: the users full name
    
    Returns:
        prints the reversed user_word
    '''
    print(user_word[::-1])                                               #reverses usre_word printing it in reverse


def non_vowels(user_word):
    '''
    Counts all the non vowels of user_word  and shows the frequency

    Args:
        user_word: the users full name

    Returns:
        the non vowels of user_word and the frequency of user_word
    '''
    consonants = {'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0,
                  'h': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
                  'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
                  't': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}        #lists all the values of consonants while setting their individual counter to 0

    user_word = lowercase(user_word)

    for letter in user_word:                                             #converts user_word to only lowercase letters to make the letters match with vowels list
        if letter in consonants:                                         #if their is a letter in user_word for vowels
            consonants[letter] += 1                                      #add to counter of the individual letter counter

    print(f"Total non-vowels: {sum(consonants.values())}")               #gets the num of the intesgers only. .values excludes the letters so the computer doesnt add letters together which would cause an error.


def middle_name(full_name):
    '''
    Checks if the full_name of user has a possbility of middle Name. If they do, it will take the middle name and print it, even if there are multiple middle names

    Args:
        full_name: an input of user that ansers the question: "What is your full name"
    
    Returns:
        the middle name of the inputed name by user
    '''
    names = full_name.split()

    if len(names) > 2:                                                     #if length of names is greater then 2, continue to next session.
        middle_names = names[1:-1]                                         #sets the boundary from the 1st bite and last bite so that eveything in between is considered a middle name
        print("Middle name(s):", *middle_names)                            #prints "Middle names(s): *middles_names". The * take everything inside this list and give it to the function separately
    else:
        print("No middle name detected")                                   #if no middle name is prensnet, the computer will print "no middle name detected"

    

def split_name(user_word):
    '''
    Splits the user_word, and saves it

    Args:
        user_word: the users full name

    Returns:
        split and saves the split of user_word
    '''
    return user_word.split()                                                #Saves the split name                        


def initials(names):
    '''
    Gets the intitals of strings while inputing it in the insitials strings quotations. Searches the first letter of first and last anme and printing it in capital letters

    Args:
        names
            full_name split
        
    Returns:
        the intitials
    '''
    if len(names) > 0:                                                      #if the length of the letters in names is greater then 0
        initials_string = ""                                                #creates a storace for the two letters of intials to go in

        for name in names:                                                  #name equals first name and name = last name
            first_letter = name[0]                                          #takes the first letter of each name

            if 'a' <= first_letter <= 'z':                                  #checks if the first letter is lowercase
                first_letter = chr(ord(first_letter) - 32)                  #converts lowercase letter to uppercase without .upper()

            initials_string += first_letter                                 #adds the first letter to the initials string

        print(f"Initials: {initials_string}")                               #prints whatever is inside the initials_string list
    else:
        print("No name entered.")                                           # if length of names is not greater then 0, print no name entered.


def sort_name_characters(user_word):
    '''
    Uses the .sort function to sort the letters of user_word in alphabetical order form first to last.

    Args:
        user_word:
    '''
    characters = []                                                         #new list

    user_word = lowercase(user_word)                                        #sets all of user_word to lowercase using the lowercase function

    for letter in user_word:                                                #checks each letter in user_word
        if letter == " ":                                                   #if the letters are already in the form
            continue                                                        #continues to final line
        characters.append(letter)                                           #adds all the individual letters in the form 'x' in a saved characters list

    characters.sort()                                                       #.sort is sorting the individual characters from highest to lowest in alphabetical order
    print(f"Alphabetical order: {characters}")                              #prints every character indisvidually from first to last in accordance to alphabet



def first_name_palindrome(user_word):
    '''
    Checks if the first name is a palindrome

    Args:
        user_word: the users full name

    Returns:
        True or False depending on whether the first name is a palindrome
    '''
    names = user_word.split()                                               #sets the variable names equal to the user_word split in two

    if len(names) == 0:                                                     #checks if the user entered no name
        print("No name entered.")
        return

    first_name = lowercase(names[0])                                        #sets the first name to lowercase using the lowercase function

    if first_name == first_name[::-1]:                                      #Reverses the first name to see if it is the same as first_name
        print("True - The first name is a palindrome.")                     #if firstname = first name reversed, the computer will print "the first name is a palindrome"
    else:
        print("False - The first name is not a palindrome.")                #if firstname is not equal to first name reversed, the computer will print "the first name is not a palindrome"


def check_title(user_word):
    titles = ["dr.", "sir", "esq", "phd"]                                  #sets variable titles equal to a list with all different titles words

    words = lowercase(user_word).split()                                    #sets the variable words equal to user_word using the lowercase function and split

    for word in words:                                                      #for words in both the first name and last name
        if word in titles:                                                  #if user_word has a title from the title list
            print("True - The name contains a title or distinction.")       #computer will print "The name contains a title of distinction"
            return                                                          #saves the title in the list

    print("False - The name does not contain a title or distinction.")      #if the name doesnt contain a title the computer will print "The name does not contain a title or distinction"

def random_name_generator(user_word):
    '''
    Randomly shuffles the characters in the user's name.

    Args:
        user_word: the user's full name

    Returns:
        Prints the name with its characters randomly shuffled.
    '''
    random_name_list = list(user_word)                                       #converts user_word to a list (ex. Joaquin to 'j', 'o', 'a' ....)
    shuffled_text = ""                                                       #makes shuffle_text the varbile name for the list that will soon hold the random name

    while len(random_name_list) > 0:                                         #while the length of random_name_list is greater then 0
        random_number = random.randint(0, len(random_name_list) - 1)         #chooses a random index based on all of the letters in user_word
        shuffled_text += random_name_list[random_number]                     #radnomly adds one of t eh letters based on the position chosen from random.randit
        random_name_list.pop(random_number)                                  #randomly removes an item off the list                  

    print(shuffled_text)                                                     #print random_name_list with random_name_generator inside the previously empty string.

def main():
    '''
    A function that organizes/calls all the functions in the program, giving the user serveral options to choose what they want to do with the name they give.

    Args:
        none
    
    Returns:
        calls all the functions
    '''
    user_word = input("Give me your first and last name: ")                 #sets user_word as a global varibale to the input Give m your first and last name
    print(f"Okay, so your name is {user_word}. We can do a lot with that information.") #prints "ok so your name is (previous user input from last prompt). WE can do a lot with that information"

    while True:
                                                                            #list of options for user
        choice = input('''                                          
Which would you like to do? Type 'done' if you are finished.

2. Count the vowels in your name
3. Print your name in uppercase
4. Print your name in lowercase
5. Reverse your name
6. Get the initials of your name
7. How many non-vowels are in your first and last name
8. Add your name to a saved list
9. Display the names
10. Find the middle name
11. Turn your name into a list of characters
12. See if your name is a Palindrome
13. Check if name contains a title/distinction
14. Generate a random name using th eletters in your name

> ''')

        if choice == '2':
            count_vowels(user_word)

        elif choice == '3':
            print(uppercase(user_word))

        elif choice == '4':
            print(lowercase(user_word))

        elif choice == '5':
            reverse(user_word)

        elif choice == '6':
            initials(split_name(user_word))

        elif choice == '7':
            non_vowels(user_word)

        elif choice == '8':
            add_user_name_list(list_firstname, list_lastname)

        elif choice == '9':
            display_names(list_firstname, list_lastname)

        elif choice == '10':
            middle_name(user_word)

        elif choice == '11':
            sort_name_characters(user_word)

        elif choice == '12':
            first_name_palindrome(user_word)

        elif choice == '13':
            check_title(user_word)

        elif choice =='14':
            random_name_generator(user_word)

        elif choice.lower() == 'done':
            print("Great! Have a nice rest of your day.")
            break

        else:
            print("Invalid choice, please try again.")


main()