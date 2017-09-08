# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(inputted_string):
    '''
    (str) -> str

    Returns a copy of the inputted string but with only the alphabetical
    characters and converted to uppercase.

    REQ: None

    >>>clean_message('CSCA08 class')
    'CSCACLASS'
    >>>clean_message('')
    ''
    >>>clean_message('12345'
    ''
    '''
    # Create variable to hold the cleaned string
    cleaned_string = ""
    # For loop to loop through each character in string
    for element in inputted_string:
        # If the (character.isalpha equals true) then it means alphabetic
        if(element.isalpha() == True):
            # Add character to cleaned string variable
            cleaned_string += element
    # Convert to upper case and return
    return cleaned_string.upper()


def encrypt_letter(character, keystream):
    '''
    (str, int) -> str

    Input the character that needs to be encrypted along with it's
    corresponding keystream value and return the encrypted value.
    Convert character to number, add with keystream value (modulo 26) then
    convert number to letter

    REQ: character is required to be uppercase
    REQ: len(character) = 1
    REQ: keystream <= 26

    >>>encrypt_letter('L', 12)
    'X'
    >>>encrypt_letter('Z', 26)
    'Z'
    >>>encrypt_letter('A', 0)
    'A'
    '''
    # String with all the letters of the alphabet in uppercase
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Empty dictionaries to hold keys for converting letter to/from numbers
    dict_letter_to_num = {}
    dict_num_to_letter = {}
    count = 0
    # Go through each letter in the alphabet for letter-to-num conversion
    for letter in string:
        # Use letter as key and count number is the value. Ex: {'A':0}
        dict_letter_to_num[letter] = count
        count += 1
    # Reset counter to loop again
    count = 0
    # Go through each letter in the alphabet for num-to-letter conversion
    for letter in string:
        # Use number as key and letter as the value. Ex: {0:'A'}
        dict_num_to_letter[count] = letter
        count += 1
    # Now we have two dictionaries made. One with the letters as keys and one
    # with the numbers as keys

    # Using the created dictionary, find the number using the character as key
    number = dict_letter_to_num[character]
    # Add the number and keystream value
    total_sum = number + keystream
    # If the sum is greater than 25, subtract 26 from it
    if(total_sum > 25):
        total_sum = (total_sum - 26)
    # Find total_sum in the number-to-letter dictionary and return
    return str(dict_num_to_letter[total_sum])


def decrypt_letter(character, keystream):
    '''
    (str, int) -> str

    Input the character that needs to be decrypted along with it's
    corresponding keystream value and return the decrypted value.
    Convert character to number, subtract with keystream value (modulo 26) then
    convert number to letter

    REQ: character is required to be uppercase
    REQ: len(character) = 1
    REQ: keystream <= 26

    >>>decrypt_letter('X', 12)
    'L'
    >>>decrypt_letter('Z', 26)
    'Z'
    >>>decrypt_letter('A', 0)
    'A'
    '''
    # String with all the letters of the alphabet in uppercase
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Empty dictionaries to hold keys for converting letter to/from numbers
    dict_letter_to_num = {}
    dict_num_to_letter = {}
    count = 0
    # Go through each letter in the alphabet for letter-to-num conversion
    for letter in string:
        # Use letter as key and count number is the value. Ex: {'A':0}
        dict_letter_to_num[letter] = count
        count += 1
    # Reset counter to loop again
    count = 0
    # Go through each letter in the alphabet for num-to-letter conversion
    for letter in string:
        # Use number as key and letter as the value. Ex: {0:'A'}
        dict_num_to_letter[count] = letter
        count += 1
    # Now we have two dictionaries made. One with the letters as keys and one
    # with the numbers as keys

    # Using the created dictionary, find the number using the character as key
    number = dict_letter_to_num[character]
    # subtract the number and keystream value
    subtraction = number - keystream
    # If the answer is greater than 25, subtract 26 from it
    if(subtraction < 0):
        subtraction = (subtraction + 26)
    # Find subtraction number in the number-to-letter dictionary and return
    return str(dict_num_to_letter[subtraction])


def swap_cards(deck_cards, index):
    '''
    (list of int, int) -> NoneType

    Return none, instead mutate the inputted list at the index given. Swap the
    number at the index with the card in front of it. If the card is at the
    bottom then swap with first number.

    REQ: len(deck_cards) > 0
    REQ: Index cannot be negative
    REQ: (index + 1) <= len(deck_cards)

    >>>list1 = [1,2,3,4,5,6,7,8,9]
    >>>swap_cards(list1, 2)
    >>>list1
    [1, 2, 4, 3, 5, 6, 7, 8, 9]

    >>>list1 = [1,2,3,4,5,6,7,8,9]
    >>>swap_cards(list1, 8)
    >>>list1
    [9, 2, 3, 4, 5, 6, 7, 8, 1]
    '''
    # If card is at bottom of list
    if((index + 1) == len(deck_cards)):
        # Create a temporary variable to value at index [0]
        temp = deck_cards[0]
        # Set value at index [0] to value at (index)
        deck_cards[0] = deck_cards[index]
        # Now let original index be the temp value stored to switch values
        deck_cards[index] = temp
    # If card is not at bottom of list
    else:
        # Create a temporary variable to value at (index + 1)
        temp = deck_cards[index + 1]
        # Set value at (index + 1) to value at (index)
        deck_cards[index + 1] = deck_cards[index]
        # Now let original (index) be the temp value stored to switch values
        deck_cards[index] = temp


def move_joker_1(deck_cards):
    '''
    (list of int) -> NoneType

    Return none, instead mutate the inputted list. Find and swap the JOKER1(27)
    with the card in front of it. If the JOKER1 is at the bottom then swap
    with first number.

    REQ: Inputted list MUST have JOKER1 somewhere in it
    REQ: len(deck_cards) > 0

    >>>list1 = [1,2,3,4,5,27,6,7,8,9]
    >>>move_joker_1(list1)
    >>>list1
    [1, 2, 3, 4, 5, 6, 27, 7, 8, 9]

    >>>list1 = [1,2,3,4,5,6,7,8,9,27]
    >>>move_joker_1(list1)
    >>>list1
    [27, 2, 3, 4, 5, 6, 7, 8, 9, 1]

    >>>list1 = [27]
    >>>move_joker_1(list1)
    >>>list1
    [27]
    '''
    # Find the index that JOKER1 is at in the deck_cards
    index = deck_cards.index(JOKER1)
    # Once we know the index, we can simply use swap_cards with JOKER1's index
    swap_cards(deck_cards, index)


def move_joker_2(deck_cards):
    '''
    (list of int) -> NoneType

    Return none, instead mutate the inputted list. Find and swap the JOKER2(28)
    with the two card in front of it. If the JOKER2 is at the bottom then swap
    with first two numbers

    REQ: Inputted list MUST have JOKER2 somewhere in it
    REQ: len(deck_cards) > 0

    >>>list1 = [1,2,3,4,5,28,6,7,8,9]
    >>>move_joker_2(list1)
    >>>list1
    [1, 2, 3, 4, 5, 6, 7, 28, 8, 9]

    >>>list1 = [1,2,3,4,5,6,7,8,9,28]
    >>>move_joker_2(list1)
    >>>list1
    [2, 28, 3, 4, 5, 6, 7, 8, 9, 1]

    >>>list1 = [28]
    >>>move_joker_2(list1)
    >>>list1
    [28]
    '''
    # Find the index that JOKER2 is at in the deck_cards
    index = deck_cards.index(JOKER2)
    # Once we know the index, we can simply use swap_cards with JOKER2's index
    # We need to do this twice because it is swapping positions with the card
    # two places down the list
    swap_cards(deck_cards, index)
    # We need to refresh the index at which the JOKER2 is at
    index = deck_cards.index(JOKER2)
    # And swap again using swap_cards
    swap_cards(deck_cards, index)


def triple_cut(deck_cards):
    '''
    (list of int) -> NoneType

    Returns none but mutates the inputted list. FInd the two JOKERS (27 and 28)
    and do a triple cut with them. Everything above the first joker goes to the
    bottom  of the list, everything below the second joker goes to top.

    REQ: len(deck_cards) >= 2
    REQ: deck_cards MUST have JOKER1 and JOKER2 somewhere in it

    >>>list1 = [1,2,3,27,4,5,6,28,7,8,9]
    >>>triple_cut(list1)
    >>>list1
    [7, 8, 9, 27, 4, 5, 6, 28, 1, 2, 3]

    >>>list1 = [1,2,3,27,4,5,6,7,8,9,28]
    >>>triple_cut(list1)
    >>>list1
    [27, 4, 5, 6, 7, 8, 9, 28, 1, 2, 3]

    >>>list1 = [27,1,2,3,4,5,6,28,7,8,9]
    >>>triple_cut(list1)
    >>>list1
    [7, 8, 9, 27, 1, 2, 3, 4, 5, 6, 28]

    >>>list1 = [27,1,2,3,4,5,6,7,8,9,28]
    >>>triple_cut(list1)
    >>>list1
    [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 28]

    >>>list1 = [1,2,3,28,4,5,6,7,27,8,9]
    >>>triple_cut(list1)
    >>>list1
    [8, 9, 28, 4, 5, 6, 7, 27, 1, 2, 3]

    '''
    # Find the indexes at which both of the jokers are at
    joker_1_index = deck_cards.index(JOKER1)
    joker_2_index = deck_cards.index(JOKER2)
    # If joker1 comes before joker2
    if(joker_1_index < joker_2_index):
        # Split the parts before, after and between the jokers into slices
        first_slice = deck_cards[:joker_1_index]
        middle_slice = deck_cards[joker_1_index:joker_2_index + 1]
        last_slice = deck_cards[joker_2_index + 1:]
        # Mutate the parts of the deck
        # Last slice goes first, then middle, then first slice goes last
        deck_cards[:len(last_slice)] = last_slice
        deck_cards[len(last_slice):(len(last_slice) +
                                    len(middle_slice))] = middle_slice
        deck_cards[len(last_slice) + len(middle_slice):len(last_slice) +
                   len(middle_slice) + len(first_slice)] = first_slice
    # Else if joker2 comes before joker1
    else:
        # Split the parts before, after and between the jokers into slices
        first_slice = deck_cards[:joker_2_index]
        middle_slice = deck_cards[joker_2_index:joker_1_index + 1]
        last_slice = deck_cards[joker_1_index + 1:]
        # Mutate the parts of the deck
        # Last slice goes first, then middle, then first slice goes last
        deck_cards[:len(last_slice)] = last_slice
        deck_cards[len(last_slice):(len(last_slice) +
                                    len(middle_slice))] = middle_slice
        deck_cards[len(last_slice) + len(middle_slice):len(last_slice) +
                   len(middle_slice) + len(first_slice)] = first_slice


def insert_top_to_bottom(deck_cards):
    '''
    (list of int) -> NoneType

    Returns none but mutates the deck_cards. Take value of bottom card of the
    deck, move that many cards from the top of the deck to the bottom, and put
    them just above the last card. If bottom card is JOKER1 or JOKER2 then
    nothing changes

    REQ: len(deck_cards) > deck_cards[-1]

    >>>list1 = [9,8,7,6,5,1,2,3,4]
    >>>insert_top_to_bottom(list1)
    >>>list1
    [5, 1, 2, 3, 9, 8, 7, 6, 4]

    >>>list1 = [1,2,3,4,5,6,7,7]
    >>>insert_top_to_bottom(list1)
    >>>list1
    [1, 2, 3, 4, 5, 6, 7, 7]
    '''
    # Find value of last index in the deck of cards
    num = deck_cards[-1]
    # If the numbers are 27 or 28 then don't mutate the deck
    if((num != 27) and (num != 28)):
        # Split the parts of the deck in to slices
        # Top slice is the first (n) values in the deck
        top_slice = deck_cards[:num]
        # Second value is what's leftover in the middle up to the last value
        middle_slice = deck_cards[num:len(deck_cards) - 1]
        # Create the mutated deck by putting middle then top slice with the
        # last number remaining at the end
        deck_cards[:len(middle_slice)] = middle_slice
        deck_cards[len(middle_slice): (len(middle_slice) +
                                       len(top_slice))] = top_slice


def get_card_at_top_index(deck_cards):
    '''
    (list of int) -> int

    Looking at the first number in the list, take that value and return the
    value at that index in the list. If the top card is JOKER2, use JOKER1 as
    the index value.

    REQ: len(deck_cards) >= 28

    >>>list1 = [4,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    >>>get_card_at_top_index(list1)
    5

    >>>list1 = [27,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6]
    >>>get_card_at_top_index(list1)
    6

    >>>list1 = [28,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6]
    >>>get_card_at_top_index(list1)
    6

    >>>list1 = [0,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6]
    >>>get_card_at_top_index(list1)
    0
    '''
    # Top card is the first index of the deck
    top_card = deck_cards[0]
    # If top card is JOKER1 then simply use JOKER2 as top card
    if(top_card == JOKER2):
        top_card = JOKER1
    # We need to return the value of the top card index
    return deck_cards[top_card]


def get_next_value(deck_cards):
    '''
    (list of int) -> int

    Return the potential keysteam value after doing all five steps of the
    entire algorithm.

    REQ: len(deck_cards) = 28
    REQ: deck_cards must have JOKER1 and JOKER2 inside somewhere

    >>>list1 = [18,5,7,10,26,28,15,22,25,16,3,6,9,12,19,1,21,24,27,2,4,8,
    11,14,17,20,23,13]
    >>>get_next_value(list1)
    4

    >>>list1 = [27,5,7,10,26,28,15,22,25,16,3,6,9,12,19,1,21,24,18,2,4,8,
    11,14,17,20,23,13]
    >>>get_next_value(list1)
    20

    >>>list1 = [27,5,7,10,26,13,15,22,25,16,3,6,9,12,19,1,21,24,18,2,4,8,
    11,14,17,20,23,28]
    >>>get_next_value(list1)
    16
    '''
    # We are doing all five steps of the algorithm
    # First moving joker1 and joker2 using the functions we made
    move_joker_1(deck_cards)
    move_joker_2(deck_cards)
    # Next is triple cut using the function
    triple_cut(deck_cards)
    # Then take bottom card and take that many cards from the top and put
    # at bottom before bottom card
    insert_top_to_bottom(deck_cards)
    # Finally, return the value of the top card
    return get_card_at_top_index(deck_cards)


def get_next_keystream_value(deck_cards):
    '''
    (list of int) -> int

    Returns the keytream value after repeating the algorithm to make the range
    is 1-26. Repeats algorithm by calling get_next_value in a loop.

    REQ: len(deck_cards) = 28
    REQ: deck_cards must have JOKER1 and JOKER2 inside somewhere

    >>>list1 = [19,1,21,24,26,28,15,22,25,16,3,6,9,12,18,5,7,17,27,2,4,8,
    11,14,10,20,23,13]
    >>>get_next_keystream_value(list1)
    21

    >>>list1 = [19,1,7,17,27,2,4,8,11,16,3,6,9,12,18,5,21,24,26,22,25,15,
    28,14,10,20,23,13]
    >>>get_next_keystream_value(list1)
    24

    >>>list1 = [19,13,7,15,28,14,10,20,23,5,21,24,26,22,25,17,27,2,4,8,11,
    16,3,6,9,12,18,1]
    >>>get_next_keystream_value(list1)
    10
    '''
    # Setting keystream to 27 so it will do the while loop once
    keystream = 27
    # Keep checking until the keystream is not 27 or 28
    while((keystream == 27) or (keystream == 28)):
        # Get the keystream by calling function get_next_value
        keystream = get_next_value(deck_cards)
    return keystream


def process_message(deck_cards, message, action):
    '''
    (list of int, str, str) -> str

    Returns the encrypted or decrypted message. First parameter is the deck of
    cards, second parameter is the message, third is the action to either
    encrypt or decrypt.

    REQ: len(deck_cards) = 28
    REQ: deck_cards must have JOKER1 and JOKER2 inside somewhere
    REQ: len(message) > 0
    REQ: action can only be 'e' for encrypt or 'd' for decrypt

    >>>process_message([19,13,7,15,28,14,10,20,23,5,21,24,26,22,25,17,27,2,
    4,8,11,16,3,6,9,12,18,1], "Hello", 'e')
    'ROLYI'

    >>>process_message([19,13,7,15,28,14,10,20,23,5,21,24,26,22,25,17,27,2,4,
    8,11,16,3,6,9,12,18,1], "rolyi", 'd')
    'HELLO'
    '''
    # Clean the message by using clean_message function
    message = clean_message(message)
    output_message = ""
    # Go through each letter in the message
    for letter in message:
        # Get the keystream
        keystream = get_next_keystream_value(deck_cards)
        # Two possible actions: encrypt or decrypt
        # Put the letter through the encrypt or decrypt function
        # Add the modified letter to the output_message string
        if(action is 'e'):
            output_message += encrypt_letter(letter, keystream)
        else:
            output_message += decrypt_letter(letter, keystream)
    return output_message


def process_messages(deck_cards, messages, action):
    '''
    (list of int, list of str, str) -> list of str

    Returns the list of encrypted or decrypted messages. First parameter is the
    deck of cards, second parameter is the list of messages, third is the
    action to either encrypt or decrypt.

    REQ: len(deck_cards) = 28
    REQ: deck_cards must have JOKER1 and JOKER2 inside somewhere
    REQ: len(messages) > 0
    REQ: len(messages[x]) > 0
    REQ: action can only be 'e' for encrypt or 'd' for decrypt

    >>>process_messages([19,13,7,15,28,14,10,20,23,5,21,24,26,22,25,17,27,2,
    4,8,11,16,3,6,9,12,18,1], "Hello", 'e')
    ['ROLYI', 'NYG', 'MKT']

    >>>process_messages([19,13,7,15,28,14,10,20,23,5,21,24,26,22,25,17,27,2,
    4,8,11,16,3,6,9,12,18,1], ['ROLYI', 'NYG', 'MKT'], 'd')
    ['HELLO', 'DOG', 'CAT']
    '''
    # Create a copy list of deck_cards for use later
    original_deck_cards = deck_cards[:]
    # Empty list to put the final messages into
    output_list = []
    # Go through each message in the messages list
    for message in messages:
        # Put the mesage through clean_message
        message = clean_message(message)
        output_message = ""
        # Go through each letter in the message
        for letter in message:
            # Get the keystream
            keystream = get_next_keystream_value(deck_cards)
            # Two possible actions: encrypt or decrypt
            # Put the letter through the encrypt or decrypt function
            # Add the modified letter to the output_message string
            if(action is 'e'):
                output_message += encrypt_letter(letter, keystream)
            else:
                output_message += decrypt_letter(letter, keystream)
        # Add the modified word to the list to return
        output_list.append(output_message)
        # Set deck_cards back to  the original list so it can be used again
    return output_list


def read_messages(file_handle):
    '''
    (io.TextIOWrapper) -> list of str

    Returns the lines in a file as a list of messages. One message per line in
    the file

    REQ: File cannot be empty
    REQ: One message per line
    '''
    # Create an emptry list to hold the messages
    messages_list = []
    # Go through each line in the file and strip of "\n" and add the line to
    # messages_list
    for line in file_handle:
        line = line.rstrip()
        messages_list.append(line)
    # We now have a list that contains all the messages in the file
    return messages_list


def read_deck(file_handle):
    '''
    (io.TextIOWrapper) -> list of int

    Returns the numbers in a file as a list of ints.

    REQ: File cannot be empty
    '''
    # Create an empty list to hold the numbers of the deck
    deck_list = []
    # Go through each line in the file and strip the line of "\n"
    for line in file_handle:
        line = line.rstrip()
        # Split the numbers into a list and add this list to deck_list
        line_list = line.split()
        deck_list += line_list[:]
    count = 0
    for element in deck_list:
        deck_list[count] = int(deck_list[count])
        count += 1

    # Now we have one list that contains all the numbers in the file
    return deck_list
