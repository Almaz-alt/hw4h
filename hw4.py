class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = health > 0

class SomeHero(Hero):
    def some_method(self):
        if not self.is_alive:
            return

dead_heroes = [hero for hero in heroes if not hero.is_alive and hero != self]

boss.invisible_damage = boss.damage
boss.damage = 0

class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = health > 0

    def check_alive(self):
        self.is_alive = self.health > 0

    def sacrifice_to_revive(self, heroes):
        if not self.is_alive:
            return

        dead_heroes = [hero for hero in heroes if not hero.is_alive and hero != self]
        if dead_heroes:
            target = dead_heroes[0]
            target.health = 100
            target.is_alive = True
            self.health = 0
            self.is_alive = False
            print(f"{self.name} пожертвовал собой, оживив {target.name}.")

class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.invisibility_used = False
        self.invisibility_start_round = 0

    def use_ability(self, heroes, boss, round_number):
        if not self.invisibility_used and self.is_alive:
            self.invisibility_used = True
            self.invisibility_start_round = round_number
            boss.invisible_damage = boss.damage
            boss.damage = 0
            print(f"{self.name} вошла в невидимость на 2 раунда.")
        elif self.invisibility_used and round_number == self.invisibility_start_round + 2:
            boss.damage = boss.invisible_damage
            print(f"{self.name} вышла из невидимости.")
