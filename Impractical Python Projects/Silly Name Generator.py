# Impractical Python Projects problem 1, silly name generator

import sys, random

# lists of names taken from book
first_names = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
                   "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
                   'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
                   'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
                   'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
                   'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
                   'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
                   'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
                   'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
                   'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
                   'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
                   "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
                   'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
                   'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

last_names = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                  'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                  'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
                  'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
                  'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
                  'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
                  'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
                  'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                  'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                  'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                  'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
                  'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
                  'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
                  'Woolysocks')

print("Welcome to the silly name Generator.")
choice = "y"
while choice != "n":
    first = random.choice(first_names)
    last = random.choice(last_names)
    print("Your silly name is " + first + " " + last)
    choice = input("Would you like to play again? Enter Y for yes and N for no.").lower()
    while choice != "y" and choice != "n":
        choice = input("Your choice was not valid please enter Y or N").lower()

print("Thank you for playing. Goodbye.")
