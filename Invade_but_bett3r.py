__author__ = "Victor K. Chan"
import random
import copy

#resources#
food = 50 #1 person consumes 1 food every turn#
civilians = 10 #people who can complete tasks#
working_civilians = 0 #working people#
water = 200 #use to grow crops#
max_water = 200 #uh oh it's pee pee time#
energy = 100 #used to power machinery, won't be needed until later#
max_energy = 100 #Piii... Kaaa... Chuuuuuuuuuu! UwU#
wood = 100 #worth 1 weight/space each#
stone = 50 #worth 2 weight/space each#
iron = 10 #worth 5 weight/space each#
max_storage = 300 #resource = no. of wood + no. of stone x 2 + no. of iron x 5#
weight = wood + (stone * 2) + (iron * 5)
monies = 100 #money.#
income = 10 #gained through taxes#
windmills = 3 #energy per windmill is 5#
happiness = 5 #happiness affects how much work civilians can do. 5 happiness = 100% work#

#non-npc hp stuff#
resource_wood_life = 10 #how many hits to break a tree#
resource_stone_life = 20 #how many hits to break a rock#
resource_iron_life = 50 #how many hits to break an iron vein#
resource_gold_life = 25 #how many hits to break a gold vein#
wood_wall_life = 20 #how much damage the wood wall can sustain#
stone_wall_life = 50 #etc.#
iron_wall_life = 120 #dmg to walls is equivalent to 1/2 of dmg (if not explosive dmg)#
concrete_wall_life = 200
steel_wall_life = 500
bresist_wall_life = 350 #Blast Resistant Walls take less explosive damage#
town_hall_life_1 = 1000 #Protecc at all costs#
town_hall_life_2 = 1500
town_hall_life_3 = 2750
town_hall_life_4 = 5000
town_hall_life_GOD = 30000 #For the GOD, in whom we trust#

#npc stuff#
civilian_hp = 1 #real weak ni[B][B]a#
civilian_atk = 1 #One-Puuuuuuuuuunch!!!#
soldier_hp = 3 #less weak#
soldier_atk = 5 #base ATK for soldiers#
soldier2_hp = 5 #lvl 2!#
soldier2_atk = 8 #base ATK for soldiers#
soldier3_hp = 9 #STRONK#
soldier3_atk = 12 #hahahahahahahahaha#
soldier4_hp = 15 #EXTRA STRONK#
soldier4_atk = 23 #ahahahahahahahahahaha#
monster1_hp = 10 #bring on the sauce#
monster1_atk = 2 #shine, ningen!#
monster2_hp = 20 #bonus! bonus!#
monster2_atk = 5 # aaaaaaaa #
boss1_hp = 100 #LVL 1 boss#
boss1_atk = 50 #Enough to destroy a wood wall#
boss2_hp = 750 #Harder now!#
boss2_atk = 250 #rip walls#
bossfinal_hp = 16000 #H A R D E R !   H A R D E R !#
bossfinal_atk = 1000 #H e  f i n n a  s m a c c  r e a l  h a r d#

#you stuff#
you_hp = 10 #Your HP when you're QUESTing#
you_atk = 4 # sans. #
you_lvl = 1 # gained through adventuring and doing stuff. #
you_exp = 0
archery = False #Skill.#
swordsmanship = False #nope.#
negotiation = 1 #negotiation level#
you_dead = False #sadly.#
#On beautiful days like this, kids like you . . .  #
available_names = ["Mikey", "Ikey", "Ikea", "Gandondorf", "Lonk", "Lank",
    "Zoldo", "Kitti", "Katti", "Jerry", "CHAD"]
available_lnames = ["Muzushashi"]
town_name = "ErrOr"
you_name = input("Please insert your name! >> ")
input("That... That is a nice name. >> ")
input("Now... With that wonderful name... >> ")
input("It will be deleted. >> ")
temp_name = available_names[random.randrange(0, len(available_names))]
you_name = temp_name
sieged = False
print("Your name will be " + you_name + ".")
input("No one can change their fate. Nor can you. >> ")

#Time and Stuff#
turn = 0
year = 120
seasons = ["Spring", "Summer", "Autumn", "Winter"]
current_season = 0
season = seasons[current_season]

#Size#
IsCity = False
IsKingdom = False

loop = True
while loop:
    intro = True
    print("        I N V A D E  B U T  B E T T 3 R       ")
    print("                    V 0.0.1                   ")
    print("                  A) New Game                 ")
    print("                  X) Exit                     ")
    choice = input("      Choose an action: >> ").lower()
    if choice == "a" and intro:
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("Welcome... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("To this world, where you are the owner of a town... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("Your goal is to upgrade you town and city... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("Until you achieve the power of Gods... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("You can never age... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("But you can be killed... >> ")
        input("... >> ")
        input("... >> ")
        input("Learn. Upgrade. Attack. Defend... >> ")
        input("... >> ")
        input("And most importantly... >> ")
        input("... >> ")
        input("... >> ")
        input("... >> ")
        input("Get better with every death... >> ")
        input("... >> ")
        input("... >> ")
        input("*Bright light surrounds you...* >> ")
        input("*It's getting brighter...* >> ")
        input("*Brighter...* >> ")
        input("*BRIGHTER...* >> ")
        input("*BRIGHT-* >> ")
        input("*You awoke in your town...* >> ")
        town_name = input("What should the Town be called? >> ")
        input("Neat. >> ")
        intro = False
        while not intro:
            if weight <= max_storage:
                wood += working_civilians * random.randrange(15, 20)
                weight = wood + (stone * 2) + (iron * 5)
            elif weight <= max_storage:
                stone += working_civilians * random.randrange(5, 7)
                weight = wood + (stone * 2) + (iron * 5)
            elif weight <= max_storage:
                iron += working_civilians * random.randrange(1, 2)
                weight = wood + (stone * 2) + (iron * 5)
            else:
                print("Storage at max capacity, civilians cannot gather any more!")
            weight = wood + (stone * 2) + (iron * 5)
            if IsCity:
                print("Welcome to your city, " + you_name + "!")
            elif IsKingdom:
                print("Welcome to your kingdom, " + you_name + "!")
            else:
                print("Welcome to your town, " + you_name + "!")
            print("Available Actions: ")
            if working_civilians < civilians and weight < max_storage:
                print("A)Gather Resources")
            if working_civilians < civilians and not sieged:
                print("B)Build Something")
            if soldiers > 0 and not sieged:
                print("C)Attack Something")
            if sieged:
                print("D)DEFEND YOUR TOWN!")
            print("E)Check Stats")
            choice2 = input("Pick Something! >> ").lower()
            if choice2 == "a" and working_civilians < civilians and weight < max_storage:
                chosen = input("Assign how many people? >> ")
                if chosen.isdigit() and :
# TODO: aaaaaaaaaaaaaaaaaaa#


    exit("Sequence Complete.")
