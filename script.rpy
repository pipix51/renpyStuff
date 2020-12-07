#############--GAME BEGINS HERE--##############

label start:
    scene black

    #This is how to display a narrator's voice in RenPy
    "Do you want to play as a girl or a guy?"

    menu:
        "A girl":
            show girl 1 at center
            $ male = False

        "A guy":
            show boy 1 at center
            $ male = True

    "So this will be your character."

    "What is your character's name?"

    hide girl 1
    hide boy 1

    python:
        name = renpy.input("Input name.")

        if not name:
            name = "Inno Challenge"

    #"[Python variable]" can be used to reference variables
    "So your character's name is [name]? What a nice name."

    "Alright let's start!"

    jump scene0

label scene0:
    play music 'audio/illurock.opus'

    scene white
    with dissolve

    if male:
        show boy 1 at center
    else:
        show girl 1 at center

    #The character tag "me" gives a name to who's talking
    #Check the "init_file" script to see what the character tags are.
    me "Wait, where am I? This feels strange, like I'm being
        transported..."

    me "Argh the light hurts--"

    scene black
    with dissolve

    "The light shone brightly on [name]. Before they knew it, they
     were transported into a new world."

    jump prologueScene1

label prologueScene1:
    scene bg town
    with dissolve

    stop sound
    stop music fadeout 1.0

    alarmClock "RING!!!!"

    "Wake up! Wake up!"

    scene black
    with dissolve

    jump prologueScene2

label prologueScene2:
    scene bg shop
    with dissolve




    return
    #game ends here
