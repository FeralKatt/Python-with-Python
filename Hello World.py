import time


def hello(): # We start here obviously
    print('Once upon a time it was a dark and stormy night.') # Spooky? No cliched.
    time.sleep(5)  # I just googled how to do that
    print("You wake up somewhere and don't remember anything at all")
    time.sleep(3) # if you don't know by now this is a comment and has no effect on code
    quest = input('Traveler! You have reached the land of PYTHON!!! Are you sure this is a quest you want to endure? ')
    if quest.lower() not in ['y', 'yes']:

        '''
        if you are reading this then that is basically asking if you say Y, y, or Yes, Yes
        any other option defaults to the next line
        '''

        # also ''' or """ like above lets you make multi line comments.

        print('Okay fine then begone!!!')

        return  # ie quit this function
    print("I'll let that one slide traveller but here in PYTHON most of us do not speak your native tongue")

    print("We only speak the master language of snakes, PYTHON")

    '''
        There are better ways of doing multi line printing than this but I'm keeping it simple for now 
    '''

    name = input('Traveller what is your name? ')

    if name == ('name = (input)'): # thanks Etherlord on discord cause I forgot how to use == there and needed a hand
        print('Okay smartass I see you have more than the basics down but you still have to live here for now')
        name = input('Just speak your name so we can move on')

    print('Okay ' + name + ' You have obviously lost your memory, you used to rule here')
    print('In order to help you we will need to unlock your memory_modules')
    input('Do you know what a module is?')
    print("That's good cause I'm going to ignore your answer for now regardless") # I really just need to get to it here
    print('A module is another file and we can call one now, lets call your speech module')
    input('Do you know how to do that?')

    """
    This is intentional, if you know how to to fix the above 
    then do so to the best of your ability :) 
    Otherwise lets move on
    """

    print('first we should create a language module so you can learn to speak, I promise you are not a robot')
    print('or are you...')
    time.sleep(3)
    print('The ghost transports to your earliest memories on how to speak PYTHON, aka print')

    """
    I'll index this later hopefully
    """


def talk():  # we won't call talk print cause you want to use print when talking
    print('The Ghost looks at you')
    time.sleep(3)
    print('You look at the ghost')
    time.sleep(3)
    print('You: Can we just get on with this please?')
    print('Ghost: Look bud we are in a different function now, if you want to know more check the comments')
    """
    good luck to me, a million people can teach you better than me
    but I learn by doing so if you do too I hope this helps 
    also a million people can teach you better than me 
    """
    basic = input("Can you say 'hello world?'")

hello()
