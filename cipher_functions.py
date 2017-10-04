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


def read_messages(file_handle):
    '''
    (io.TextIOWrapper) -> list of str

    Returns the lines in a file as a list of messages. One message per line in
    the file

    REQ: File cannot be empty
    REQ: One message per line
    '''
  

def read_deck(file_handle):
    '''
    (io.TextIOWrapper) -> list of int

    Returns the numbers in a file as a list of ints.

    REQ: File cannot be empty
    '''

    
