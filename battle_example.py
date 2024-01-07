from simplefight import Character, fight, gameover

hero = Character("Sonic", 100, 5, 10, 'Spin Attack')
enemy = Character("Robotnik", 80, 7, 12, "Big Laser")

fight(hero, enemy)