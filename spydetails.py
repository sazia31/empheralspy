from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        #constructor with parameters
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = [] #we can add this entry later
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('sherlock','Mr.',24,9.4)
#calling class objects and giving values to the parameters + it's better than dictionary
friend_one = Spy('watson', 'Mr.', 28,8.2)
friend_two = Spy('mary', 'Miss', 28,7.2)
friend_three = Spy('hudson', 'Mrs.', 4.95, 37)
friend_four=Spy('stephan','Mr.',30,6.4)
friend_five=Spy('damon','Mr.',29,7.5)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five]


