##  Pirate Bartender Application
##  will serve drinks based on the preferences of user input

##  Version 1.0
##  January 2015

# 1. Dictionaries of questions and ingredients for bartender:

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

# 2. Function to ask what style of drink a customer likes:

def what_drink_like():
 """Ask user what drink they would like.

 Welcome user.
 Map 'questions' dictionary.
 Return 'user_drink' dictionary.
  - keys: flavours in 'questions' dictionary
  - values: True or False
 """
 
 print "Welcome Yer To The Pirate Bar"
 print "What drink would yer like?\n"
 user_drink = {}
 for flavours in questions:
   user_response = raw_input(questions[flavours] + ": ") # ask all questions in dictionary
   if user_response == 'y':  # test if response is yes
         user_drink[flavours] = True # and add response to user_drink dictionary
   else:
         user_drink[flavours] = False 
 print user_drink



if __name__ == '__main__':
    what_drink_like()
    
 