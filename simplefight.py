from random import randint
from emoji import emojize

class Character:
    def __init__(self,name, max_hp, min_dmg, max_dmg, attack_name):
        self.name = name
        self.hp = max_hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg        
        self.attack_name = attack_name
        self.dead = False

    def take_dmg(self,dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.dead = True

def fight(hero,enemy):
    print(hero.name, "Encounters a wild", enemy.name)
    
    while not hero.dead and not enemy.dead:

        hero_attack = randint(hero.min_dmg, hero.max_dmg)
        print ()
        print(hero.name, "Hits", enemy.name, "for", hero_attack, "dmg with", hero.attack_name)
        enemy.take_dmg(hero_attack)
        print(enemy.name, "has", enemy.hp,"hp left")

        enemy_attack = randint (enemy.min_dmg, enemy.max_dmg)
        print ()
        print(enemy.name, "Hits", hero.name, "for", enemy_attack, "dmg with", enemy.attack_name)
        hero.take_dmg(enemy_attack)
        print(hero.name, "has", hero.hp,"hp left")

    if hero.dead:
        print ()
        gameover (hero)

    else:
        print ()
        print (enemy.name, "is dead.", hero.name,"Level Up")

def gameover(hero):
    end_text=["","RIP",hero.name,"GAME OVER",emojize(":crying_face:"),""]
    for i in end_text:
        print (f'{i:-^50}')
           
if __name__ == "__main__":
    enemy_list=[
        ['Crab People',50,5,10,'Crab Claw'],
        ['Wolf Spider',30,3,7,'Scary Bite'],
        ['ManBearPig',200,5,30,'ManBearPigBite'],
        ['Bowser',100,7,15,'Bowser Fire'],
        ['Ridley',175,6,12,'Spike Tail']]

    hero_stats = ['Ryu',175,6,12,'HADOUKEN!!!']

    #Load Hero
    hero = Character(*hero_stats)

    #Load Random Enemy
    enemy_id = randint(0,len(enemy_list)-1)
    enemy=Character(*enemy_list[enemy_id])

    fight (hero,enemy)
