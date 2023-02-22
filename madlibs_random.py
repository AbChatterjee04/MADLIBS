# MAD LIBS Generator in Python

from random import randint
import copy

story = (
    "one day my friend {} and i decided to go to the {} game in {}."  + 
    "we really wanted to see our favorite player {} in action."   +
    "so we took {} and {} with us to cheer our favorite player."  +
    "We got into the game and it was lot of fun."   +
    "We ate some {},{} and drink {},{}."+
    "we had a great time! we plan to go ahead and explore more amazing stadiums like {} to catch more exciting games from next year!"
)

#creating a dictionary to see words by type

word_dict = {
    "noun":['Alex','Steve','Swaminathan','Joseph','Lucifer','Jonna'],
    "sports":['Ipl','T20 World cup','Cpl','Bbl','T10','Test Championship'],
    "city name":['Kolkata','Mumbai','jameca','sydney','London'],
    "players":['Virat','Rohit','Warner','Butler','Rusell','Boult','Bumrah','Archer','stark'],
    "action verb":['shout Board','flag','jersey',],
    "stadium":['Eden Gardens','Wankhede','Kingstown','Melbourne'],
    "food":['popcorn','Badapow','chips','chowmin','burger','kfc'],
    "drink":['Sprite','pepsi','coke','red bull','beers']
}

def get_word(type, local_dict):
    words = local_dict[type]
    count = len(words) - 1 #since counting start from 0
    index = randint(0, count) #ends according count
    return local_dict[type].pop(index) #removing the one already selected

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('noun', local_dict),
        get_word('sports', local_dict),
        get_word('city name', local_dict),
        get_word('players', local_dict),
        get_word('action verb', local_dict),
        get_word('action verb', local_dict),
        get_word('food', local_dict),
        get_word('food', local_dict),
        get_word('drink', local_dict),
        get_word('drink', local_dict),
        get_word('stadium', local_dict)
    )

print("Story1 : ")
print(create_story())
print()
print("Story2 : ")
print(create_story())
