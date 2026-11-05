# Simple Battle Simulator

This is a Python battle simulation using object-oriented programming.
A Knight fights against two enemies: a Goblin and an Orc.

## File Structure

- `character.py`: Defines the Character class.
- `main.py`: Runs the battle simulation.

## Character Class

### Attributes

- `name`: The character's name.
- `hp`: The character's health points.
- `attack_power`: The character's attack power.
- `initial_attack_power`: The original attack power set at object creation.

### Methods

- `attack(other)`: Attacks another character with random damage between 30% and 90% of the initial attack power.
- `is_alive()`: Checks whether the character's HP is greater than zero.
- `__str__()`: Returns the character's name and current HP.

## How the Battle Works

1. Create a Knight, a Goblin, and an Orc.
2. Display their initial HP.
3. The Knight fights the Goblin first.
4. If the Knight survives, the Knight fights the Orc.
5. Each character attacks in turns until one side is defeated.
6. Display the battle result.

## Running the Game

Run the following command:

```bash
python3 main.py