from random import randint

class Fighter:
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

def fight(hero: Fighter,enemy: Fighter, print_output =  True): 
    print(hero.name, "Encounters a wild", enemy.name)
    fight_log = []
    while not hero.dead and not enemy.dead:
        
        hero_attack = randint(hero.min_dmg, hero.max_dmg)
        print ()
        print(f"{hero.name} Hits {enemy.name} for {hero_attack} dmg with {hero.attack_name}")
        enemy.take_dmg(hero_attack)
        print(f"{enemy.name} has {enemy.hp} hp left.")

        enemy_attack = randint (enemy.min_dmg, enemy.max_dmg)
        print ()
        print(f"{enemy.name} Hits {hero.name} for {enemy_attack} dmg with {enemy.attack_name}")
        hero.take_dmg(enemy_attack)
        print(f"{hero.name} has {hero.hp} hp left")

    if hero.dead:
        print ()
        gameover (hero)

    else:
        print ()
        print (f"enemy.name is dead. {hero.name} Level Up.")

def gameover(hero):
    #got rid of emoji here. It looked weird with monospaced fonts in terminal.
    end_text=["","RIP",hero.name,"GAME OVER"]
    for i in end_text:
        print (f'{i:-^50}')
           
