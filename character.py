import random

class Character:

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.initial_attack_power = attack_power

    def attack(self, other):
        min_damage = self.initial_attack_power * 0.3
        max_damage = self.initial_attack_power * 0.9

        damage = random.uniform(min_damage, max_damage)
        other.hp -= damage

        print(
            f"{self.name} attacks {other.name} "
            f"for {damage:.1f} damage!"
        )

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.1f} HP"