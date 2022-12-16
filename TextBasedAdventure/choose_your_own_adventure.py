name = input('Enter your name: ')
print(f'Greetings {name}! Welcome to your adventure!')
start = input('Would you rather play thee game or perish? ')
if start == 'play':
    print("Great! Let's play the game")
    setting = input('Want to go to the jungle,dungeon or desert? ')
else:
    print("Lame, Okay you\'re dead now...")
    quit()
    
if setting == 'jungle':
    print('Welcome to the mighty Amazon rainforest! Your tour guide told you to wait here....L')
    response = input('But he has been gone a long time.... Follow him or wait her? ')
    if response == 'follow':
        print('You follow him into the trees...')
        response = input('You walk a long time  and you find a wolf! Run or attack? ')
        if response == 'Run':
            print('The wolf run behind you and he bite you!')
            quit()
        elif response == 'attack':
            print('You fight with him but the wolf escaped.')
            response('You rest and walk again...Now you find a coat and you think the coat appurtenece for the guide! What you do? take or left')
        if response == 'left':
            print('You find the guide but he need\'s her coat')
            quit()
        elif response ==  'take':
            print('You take the coat and put in your bag')
            response('It\' raining and you have the coat. Use or no? ')
        if response == 'Use':
            print('You take de coat but the wind pushed her!')
            quit()
        elif response == 'no':
            print('You got a sick...')
            response('You find a medicinal plant. Use or no? ')
        if response == 'Use':
            print('You use the plant and nothing heapend.')
            print('Later you find the guide and give her coat')
        elif response == 'no':
            print('Later you dead!')
            
    elif response == 'wait':
        print("You wait another ten minutes, and he still isn't here!")
    else:
        print('Invalid response! you lose!')
        quit()