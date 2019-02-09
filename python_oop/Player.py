import time
import random
import sys


class Player(object):
    def __init__(self, name, health_count=5, health=100):
        self.name = name
        self.health_count = health_count
        self.health = health
        self.hit = 0

    def display_current_data(self):
        print('can gucu', self.health_count)
        print('can', self.health)

    def attack(self, enemy):
        print("atak oldu..")
        print("saldırı bitti")
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        result = self.calculate_attack_prize()
        if result == 0:
            print("\nkazanan yok")
        if result == 1:
            self.hit(enemy)
            print("\ndusmani vurdun")
        if result == 2:
            enemy.hit(self)
            print("pis kaybeden")

    def calculate_attack_prize(self):
        return random.randint(0, 2)

    def escape(self):
        print("escaping from fight..")
        for i in range(10):
            time.sleep(.3)
            print("\n", flush=True)
        print("enemy catched you ..")

    def hit(self, hitten):
        hitten.hit += 1
        hitten.health -= 1
        if (hitten.hit % 5) == 0:
            hitten.health_count -= 1
        if hitten.health < 1:
            print("game  winner : {}".format(self.name))
            self.exit_game()

    def exit_game(self):
        sys.exit()


you = Player('angel')
enemy = Player('devil')

while True:
    print('ne yapmak istiyorsun :',
          'Saldırı :a',
          'Kcis  :e',
          'Cikis :q', sep='\n')
    movement = input('\n> ')
    if movement == 'a':
        you.attack(enemy=enemy)
        print("Dusman durumu")
        enemy.display_current_data()
        print("Senin duerumun")
        you.display_current_data()
    if movement == 'e':
        you.escape()

    if movement == 'q':
        you.exit_game()
