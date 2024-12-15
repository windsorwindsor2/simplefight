from random import randint

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
    #got rid of emoji here. It looked weird with monospaced fonts in terminal.
    end_text=["","RIP",hero.name,"GAME OVER"]
    for i in end_text:
        print (f'{i:-^50}')
           
if __name__ == "__main__":
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

    
    def randchar(char_list: list) -> Character:
        char_id = randint(0,len(char_list)-1)
        return Character(*char_list[char_id])

    #Load Hero
    hero = randchar(hero_list)

    enemy = randchar(enemy_list)
    
    fight (hero,enemy)
