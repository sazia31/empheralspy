from spydetails import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
import colorama
from termcolor import *
from datetime import datetime
import string#Imported for avoiding invalid characters
import getpass



STATUS_MESSAGES = ['Life learnings from Holmes', 'Not Available', 'On the art of Deduction', 'You do not observe','Busy']
#Pre-Existing statuses
print "Hey! Let\'s get started"
colorama.init()

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


def add_status():
    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (Y/N)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 2:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
# 0 is the base index
        message_selection = int(raw_input("\nChoose your status from above status "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
#in this we take the list index-1 as the elements are taken in this order
    else:
        print 'The option you selected is not valid! Press either Y or N '

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'Please see! You current don\'t have a status update!'

    return updated_status_message
#this function would return the updated status


def add_friend():
    new_friend = Spy('','',0,0.0)
#added in the spy class
    new_friend.name = raw_input("Please add your friend's name: ")
    if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(new_friend):
        print "Invalid entry."
    else:
        print new_friend

    new_friend.salutation = raw_input("Formal Salutation: Mr. or Ms. or Mrs. ")
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 2 and new_friend.age > 15 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'New Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided!!'

    return len(friends)
#this function would return the number of friends you have!


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name, friend.age,friend.rating)
        #string formatting done
        item_number = item_number + 1

    friend_choice = raw_input('Choose your friend!')

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    if len(text) == 0:
        print 'Try next time with a valid message!'
    elif text == 'SOS' or 'Save Me' or 'Save me Please':
        print 'Hold on!'
    elif text == 'False' or 'Hack' or '#' or '&' or '@' or '##' or '??':
        print 'SpyChat isnt meant for passing time!'
#no such symbols should be accepted
    else:
        print 'You are good to go!'

    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():
    sender = select_a_friend()

    output_path = raw_input('What is the name of the file?')

    secret_text = Steganography.decode(output_path)
    print secret_text

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)
#this function will add chats to the chat list
    words=secret_text.split(' ')
    #avg=sum(len(word)for word in words)/ len(words)
    print 'The number of wors in the secret message is : ' + str(len(words))
    print 'Your secret message has been saved! ;)'


def read_chat_history():

    read_for = select_a_friend()

    print '\n'
#it will show number of friends you have!
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            cprint (chat.time.strftime("%d %B %Y"), 'blue')
            cprint ('Your said:', 'red')
            print chat.message
        else:
            cprint (chat.time.strftime("%d %B %Y"), 'blue')
            cprint (friends[read_for].name + ' said: ', 'red')
            print chat.message


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + "Welcome to the spy squad."

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry! You are not of the correct age to be a spy!'

if existing.upper() == "Y":
    
    pswd = getpass.getpass('Password:')

    if pswd == 'admin':
        start_chat(spy)

    else:
        print 'Password Incorrect!'
else:

    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        invalidchar = set(string.punctuation.replace('_', ' '))
        if any(char in invalidchar for char in spy.name):
            print 'invalid name'
        else:

            spy.salutation = raw_input("Should I call you Mr. or Mrs. or Ms.?: ")

            spy.age = raw_input("What is your age?")
            spy.age = int(spy.age)

            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)

        start_chat(spy)

