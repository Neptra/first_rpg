def main():
    from time import sleep
    boy=1
    girl=2
    gender=int(input("Are you a boy or a girl?(write 1 or 2):"))
    if gender==2:
        print ('''???:Zzzzz...Zzzzz..Mh? MH!?! Oh a new player! *And a gorgeous one!* Hello my name is "The Game" I think I should ask my dev to change it. It's not a cool name. ''')
        print('''The game:Anyway what's yours my beauty?''')
        playername = input("Choose a name:")
        print("The game:Alright {} ,what a beautiful name for a beautiful girl nice to meet you.\nI think you don't know where we are right?(Girls don't know anything about games) Or do you just want to talk with me because i'm a strong, young and beautiful artificial intelligence??".format(playername))
    else:
        print('''???:Zzzzz...Zzzzz..Mh? MH!?! Oh a new player! Arh another random nerd as i see.Could you just go back to something more interesting? I'm tired. Goodbye.\n...\n...''')
        print("The game:What are you still doing here? You really want to play this game?\nAlright,alright my name is 'The game'\nblah blah blah dungeon blah blah blah permadeath blah blah blah. \nWhat's your name?")
        playername = input("Choose a name:")
        print("The game:Nerd name for a nerdy guy that's what i was sayin' but okay we're gonna play follow me.")
    print("This world is actually a video game ")
    print("We have everything: Adventurer guild, Shop, Magic shop, Town hall, Blacksmith etc.\nLet's go to the adventurers guild you'll choose a class.")
    RPGclass = None
    wallet = 0
    while not RPGclass in ['1', '2', '3']:
        RPGclass = input('What do you want to be? Mage(1), Warrior(2), ChickenCurry(3)?')
        if RPGclass != 1,2,3:
            print("Please")
        elif RPGclass=1:
            print("You are now a mage! You receive a spellbook and 1000G")
            wallet += 1000
        elif RPGclass=2:
            print("You are now a Warrior! You receive a spellbook and 1000G")
            wallet += 1000
        elif RPGclass=3:
            print("You turn into a ChickenCurry the other adventurers around ate you. END (please restart the game)")



if __name__ == '__main__':
    main()