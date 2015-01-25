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

def what_style_drink():
 """function to ask user what drink they would like"""
 print "Welcomes Yer To Thee Pirate Bar\n"
 print "What drink would yer like?"
 for types in questions:
     print questions[types]



if __name__ == '__main__':
    what_style_drink()
 