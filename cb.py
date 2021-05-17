import sys

list_hello = []
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X','Y','Z',]

def start():
    print("What kind of value would you like to sort? (String or Integer)")
    answer = input("> ")
    if answer == "String" or answer == "string":
        string_sorting()
    elif answer == "Integer" or answer == "integer":
        integer_sorting()
    else:
        print("Come on! That's not one of the options")
        start()


def integer_sorting():
    global done
    done = False
    print("Which number would you like to input?")
    action = input("> ")
    if not action.isnumeric():
        print("That's not a number!")
        integer_sorting()
    else:
        list_hello.append(int(action))
    while done == False :
        repeat_integer()


def repeat_integer():
    print("OK! Please enter your next number! (At any time type 'sort' to sort the numbers!)")
    action_2 = input("> ")
    if action_2 == "sort" or action_2 == "Sort":
        global done
        done = True
        end_integer()
    elif not action_2.isnumeric():
        print("That's not a number!")
        repeat_integer()
    else:
        list_hello.append(int(action_2))

def string_sorting():
    global check
    check = False
    print("Which letter/word would you like to input?")
    action = input("> ")
    if action.isnumeric():
        print("That's not a letter/word!")
        string_sorting()
    list_hello.append(str(action))
    while check == False :
        repeat_string()

def repeat_string():
    print("OK! Please enter your letter/string! (At any time type 'sort' to sort the numbers!)")
    action_2 = input("> ")
    if action_2 == "sort" or action_2 == "Sort":
        global check
        check = True
        end_string()
    elif action_2.isnumeric():
        print("That's not a letter/word!")
        repeat_string()
    list_hello.append(str(action_2))

# Algorithm
def bubble_Sort_String(backwards, string_to_sort):
    if backwards:
        for j in range(0, len(string_to_sort)):
            for i in range(0, len(string_to_sort)):
                _s = False
                if i != len(string_to_sort)-1:
                    for k in range(0,len(string_to_sort[i])):
                        if not _s:
                            if k != (len(string_to_sort[i]) and len(string_to_sort[i+1])):
                                if Alphabet.index(string_to_sort[i][k]) < Alphabet.index(string_to_sort[i+1][k]):
                                    string_to_sort[i], string_to_sort[i+1] = string_to_sort[i+1], string_to_sort[i]
                                    _s = True
                                elif Alphabet.index(string_to_sort[i][k]) > Alphabet.index(string_to_sort[i+1][k]):
                                    _s = True
                                else:
                                    if len(string_to_sort[i+1]) > len(string_to_sort[i]):
                                        string_to_sort[i], string_to_sort[i+1] = string_to_sort[i+1], string_to_sort[i]
                                        _s = True
            print(f'Iteration: {abs(j - len(string_to_sort))}', string_to_sort)
    else: #code inspired by stack overflow post
        for j in range(0, len(string_to_sort)):
            for i in range(0, len(string_to_sort)):
                _s = False
                if i != len(string_to_sort)-1:
                    for k in range(0,len(string_to_sort[i])):
                        if not _s:
                            if k != (len(string_to_sort[i]) and len(string_to_sort[i+1])):
                                if Alphabet.index(string_to_sort[i][k]) > Alphabet.index(string_to_sort[i+1][k]):
                                    string_to_sort[i], string_to_sort[i+1] = string_to_sort[i+1], string_to_sort[i]
                                    _s = True
                                elif Alphabet.index(string_to_sort[i][k]) < Alphabet.index(string_to_sort[i+1][k]):
                                    _s = True
                                else:
                                    if len(string_to_sort[i+1]) < len(string_to_sort[i]):
                                        string_to_sort[i], string_to_sort[i+1] = string_to_sort[i+1], string_to_sort[i]
                                        _s = True
            print(f'Iteration: {abs(j - len(string_to_sort))}', string_to_sort)

def Convert_String(arr):
    for j in range(0, len(arr)):
        arr[j] = arr[j].upper()


def bubble_Sort_Integer(backwards, integer_to_sort):
    if backwards:
        for o in range(len(integer_to_sort) - 1, 0, -1):
            for x in range(o):
                if integer_to_sort[x] < integer_to_sort[x + 1]:
                    t = integer_to_sort[x]
                    integer_to_sort[x] = integer_to_sort[x + 1]
                    integer_to_sort[x + 1] = t

            print(f'Iteration: {abs(o - len(integer_to_sort))}', integer_to_sort)
    else:
        for o in range(len(integer_to_sort) - 1, 0, -1):
            for x in range(o):
                if integer_to_sort[x] > integer_to_sort[x + 1]:
                    t = integer_to_sort[x]
                    integer_to_sort[x] = integer_to_sort[x + 1]
                    integer_to_sort[x + 1] = t

            print(f'Iteration: {abs(o - len(integer_to_sort))}', integer_to_sort)

def end_integer():
    print("Would you like a reversed list? (Yes or No)")
    reverse = input("> ")
    if reverse == "Yes" or reverse == "yes":
        print('Original List: ', list_hello)
        bubble_Sort_Integer(True,list_hello)
        print('Sorted List: ', list_hello)
        sys.exit
    elif reverse == "No" or reverse == "no":
        print('Original List: ', list_hello)
        bubble_Sort_Integer(False,list_hello)
        print('Sorted List: ', list_hello)
        sys.exit
    else:
        print("Please enter either Yes or No.")
        end_integer()

def end_string():
    print("Would you like a reversed list? (Yes or No)")
    reverse = input("> ")
    if reverse == "Yes" or reverse == "yes":
        print('Original List: ', list_hello)
        bubble_Sort_Integer(True,list_hello)
        print('Sorted List: ', list_hello)
        sys.exit
    elif reverse == "No" or reverse == "no":
        print('Original List: ', list_hello)
        bubble_Sort_Integer(False,list_hello)
        print('Sorted List: ', list_hello)
        sys.exit
    else:
        print("Please enter either Yes or No.")
        end_string()
start()