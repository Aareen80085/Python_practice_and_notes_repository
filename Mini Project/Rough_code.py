import random

# Classes
class Player:
    def __init_(self, name):
        self.name = name
        self.health = 100
        # Base attack power (small, but will be buffed later)
        self.attack_power = random.randint(5,10)

    def attack(self,enemy):
        damage = random.randint(5,10)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
    
class Dragon:
    def __init__(self, name):
        self.name = "Dragon"
        self.health = 120
        # Base attack power (small, but will be buffed later)
        self.attack_power = random.randint(50,100)

    def attack(self,player):
        damage = random.randint(10,15)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

# Game loop
print("Welcome to Dragon Slayer!")
name = input("Please enter your character's name:")
player = Player(name)
dragon = Dragon()

print("The battle begins!")
while player.health > 0 and dragon.health > 0:
    print(f"\nYour Health: {player.health} | Dragon Health: {dragon.health}")
    print("1. Attack")
    print("2. Run Away")

    choice = input("Choose an action: ")

    if choice == "1":
        player.attack(dragon)
        if dragon.health > 0:
            dragon.attack(player)

    elif choice == "2":
        print(" You ran away and reached a nearby village!")
        print("A villager approaches you and offers you a quest!")
        print("If you unlock this chest, you will receive magical powers to defeat the dragon!")

        secret = random.randint(10, 99)
        attempts = 5
        buff_unlocked = False

        while attempts > 0:
            print(f"\nYou have {attempts} attempts to guess the 2-digit number.")
            guess = input("Enter your guess: ")

            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            if len(guess) < 2:
                print("Hint: The number has 2 digits. You're missing the tens and hundreds places!")
                continue


