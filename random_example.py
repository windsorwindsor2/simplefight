from simplefight import Fighter, fight
from random import randint

#name, max_hp, min_dmg, max_dmg, attack_name

#removed Nintendo references from example,
#because nobody hates their fans like Nintendo :-(
enemy_list=[
        ['Crab People',50,5,10,'Crab Claw'],
        ['Wolf Spider',30,3,7,'Scary Bite'],
        ['ManBearPig',200,5,30,'ManBearPigBite'],
        ['Nozzlo',100,7,15,'Zoldathian Blunderbuss'],
        ['Cutman',175,6,12,'Rolling Cutter']]

hero_list = [
        ['Ryu',175,6,12,'HADOUKEN!!!'],
        ['Saitama',175,9000,9001,'Punch'],
        ['Master Chief',120,7,15,'M6D Pistol'],
        ['Megaman',100,13,17,'Mega Buster']]

    
def randchar(char_list: list) -> Fighter:
        char_id = randint(0,len(char_list)-1)
        return Fighter(*char_list[char_id])

    #Load Hero
hero = randchar(hero_list)

enemy = randchar(enemy_list)
    
fight (hero,enemy)
