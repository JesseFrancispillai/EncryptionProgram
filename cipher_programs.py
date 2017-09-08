"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'secret4.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """

    # Create the file handle for opening the deck file
    # Then set the deck_cards list by calling read_deck function
    deck_file_handle = open(DECK_FILENAME, "r")
    deck_cards = cipher_functions.read_deck(deck_file_handle)
    # Create the file handle for opening the message file
    # Then set the messages list by calling read_messages function
    message_file_handle = open(MSG_FILENAME)
    messages = cipher_functions.read_messages(message_file_handle)

    # If MODE is 'e' then encrypt, if not then decrypt
    if(MODE == 'e'):
        action = 'e'
    else:
        action = 'd'

    # Create a list to store the encrypted/decrypted messages. This uses the
    # main function: process_messages
    output_list = cipher_functions.process_messages(deck_cards,
                                                    messages, action)
    # Go through each message in the list to print on a new line
    for element in output_list:
        print(element)
    # Close the file handles
    deck_file_handle.close()
    message_file_handle.close()

    pass
