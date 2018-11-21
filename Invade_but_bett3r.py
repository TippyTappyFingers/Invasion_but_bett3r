__author__ = "Victor K. Chan"
import random
import copy

#resources#
food = 50 #1 person consumes 1 food every turn#
civilians = 10 #people who can complete tasks#
water = 200 #use to grow crops#
max_water = 200 #uh oh the bladder's full#
energy = 100 #used to power machinery, won't be needed until later#
max_energy = 100 #Piii... Kaaa... Chuuuuuuuuuu! UwU#
wood = 100 #worth 1 weight/space each#
stone = 50 #worth 2 weight/space each#
iron = 10 #worth 5 weight/space each#
max_storage = 250 #resource = no. of wood + no. of stone x 2 + no. of iron x 5#
monies = 100 #money.#
income = 10 #gained through taxes#
windmills = 3 #energy per windmill is 5#
happiness = 5 #happiness affects how much work civilians can do. 5 happiness = 100% work#

#non-npc hp stuff#
resource_wood_life = 10 #how many hits to break a tree#
resource_stone_life = 20 #how many hits to break a rock#
resource_iron_life = 50 #how many hits to break an iron vein#
resource_gold_life = 25 #how many hits to break a gold vein#
wood_wall_life = 15
stone_wall_life = 50
iron_wall_life = 120
concrete_wall_life = 200
steel_wall_life = 500
bresist_wall_life = 350
town_hall_life_1 = 1000
town_hall_life_2 = 1500
town_hall_life_3 = 2750
town_hall_life_4 = 5000
town_hall_life_GOD = 30000
