########--RENPY INIITIALISE--############
init:
    #To scale the background to fit the game size, 1280 x 720
    image white = im.Scale("white.jpg", 1280, 720)

    #Another world: On an island
    image bg beach = im.Scale("bg beach.jpg", 1280, 720)
    image bg cave = im.Scale("bg cave.jpg", 1280, 720)
    image bg forest = im.Scale("bg forest.jpg", 1280, 720)

    #Another world: In the apopcalypse
    image bg destroyedcity = im.Scale("bg destroyedcity.jpg", 1280, 720)
    image bg shop = im.Scale("bg shop.jpg", 1280, 720)
    image bg hideout = im.Scale("bg hideout.jpg", 1280, 720)

    #Another world: Time travel to a medieval fantasy
    image bg castlefaraway = im.Scale("bg castlefaraway.jpg", 1280, 720)
    image bg fantasyforest = im.Scale("bg fantasyforest.jpg", 1280, 720)
    image bg town = im.Scale("bg town.jpg", 1280, 720)

########--PYTHON INITIALISE--##########
init python:
    me = Character("[name]") #Your character's name

    cashier = Character("Cashier")
    customerOne = Character("Fast Food Customer")
    money = 10
    happinessIndex = 100

###########--TRANSFORMATIONS--################
transform center:
    xalign 0.5 yalign 1.0

transform left:
    xalign 0.25 yalign 1.0

transform right:
    xalign 0.75 yalign 1.0
