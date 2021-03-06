##  Pirate Bartender Application
##  will serve drinks based on the preferences of user input

##  Version 1.0
##  January 2015


import random

# 1. Dictionaries of questions and ingredients for bartender:

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["Glug of rum", "Slug of whisky", "Splash of gin"],
    "salty": ["Olive on a stick", "Salt-dusted rim", "Rasher of bacon"],
    "bitter": ["Shake of bitters", "Splash of tonic", "Twist of lemon peel"],
    "sweet": ["Sugar cube", "Spoonful of honey", "Splash of cola"],
    "fruity": ["Slice of orange", "Dash of cassis", "Cherry on top"]
}

# additional alcohol to add to the drinks (because they seem a bit weak):
alcohol = {
    "strong":"Two parts gin to one part vodka.",
    "salty": "A big mug o' gin for yer.",
    "bitter": "Whiskey all the way, yer hearty mate.",
    "sweet": "Like a young lass I did once marry, a nice tall glass of rum.",
    "fruity": "Ahh, lots a fruity rum."
}

# extension exercise one - name the drinks:
# two lists - adjectives and nouns
adj = ["salty", "prickly", "sweet", "tasty"]
nouns = ["sea-dog", "peg-leg", "capn's-parrot", "first-mate"]


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
   user_drink[flavours] = user_response.lower() in ['y', 'yes']
 return user_drink

# 3. Function to construct a drink:

def drink_constructor(preferences):
 """Construct a drink from the users preferences.

 Map users preferences.
 Select ingredients from the 'ingredients' dictionary to
 construct drink.
 Return drink.
 
 Arguments:
 preferences -- the dictionary returned by 'what_drink_like'
 """
 # drink is list of ingredients:
 drink = []
 # map through preferences argument:
 for types in preferences:
  if preferences[types] == True:
  # add the base alcohol to the  drink:
   drink.append(
       alcohol[types]
   )
  # then add the random ingredients:
   drink.append(
       random.choice(ingredients[types])
     )   
 print "Ay, I did make yer a tidy drink. Here tis': "
 for items in drink:
  print items
 print "How'd you like that fair drink? I call it the {0} {1}".format(random.choice(adj), random.choice(nouns))
 
# 4. Use '__main__' method to call function from command line:
if __name__ == '__main__':
    preferences = what_drink_like()
    drink_constructor(preferences)