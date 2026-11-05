from character import Character


def main():
    hero = Character("Knight", 30, 5)

    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)

    enemies = [enemy1, enemy2]

    print(hero)

    for enemy in enemies:
        print(enemy)

    print()

    for enemy in enemies:
        print(f"Battle against {enemy.name} begins!")

        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)

            if enemy.is_alive():
                enemy.attack(hero)

            print(hero)
            print(enemy)
            print()

        if not hero.is_alive():
            break

    print("Battle over!")

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()