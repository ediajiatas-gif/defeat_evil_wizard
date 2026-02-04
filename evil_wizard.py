import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = int(attack_power)
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def heal (self):
        self.health += 10
        print(f"{self.name} used healing. Health is now: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def attack(self, opponent):
        random_attack_power = random.randint(15, self.attack_power)
        opponent.health -= random_attack_power
        print(f"{self.name} slashes {opponent.name} for {random_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special1(self, opponent):
        special_damage = self.attack_power * 1.3
        opponent.health -= special_damage
        print(f"{self.name} uses reckless charge on {opponent.name} dealing {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special2(self, opponent):
        special_damage = self.attack_power * 1.5
        opponent.health -= special_damage
        print(f"{self.name} uses flame sword! {opponent.name} bursts on fire and takes {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    '''Healing method: Cannot exceed Character's max health'''    
    def heal (self):
        if self.health >= self.max_health:
            print(f"Already max HP. Cannot exceed maximum health")
        else: 
            self.health += 10
            print(f"{self.name} used healing. Health is now: {self.health}")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)
        
    def attack(self, opponent):
        random_attack_power = random.randint(20, self.attack_power)
        opponent.health -= random_attack_power
        print(f"{self.name} casts spell toward {opponent.name} dealing {random_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special1(self, opponent):
        special_damage = self.attack_power * 1.5
        opponent.health -= special_damage
        print(f"{self.name} uses fireball! {opponent.name} bursts into flames taking {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special2(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} uses life drain on {opponent.name} and deals {self.attack_power} damage!")
        if self.health < self.max_health:
            self.health += 5 
            print(f"{self.name} gained 5 HP. Total health: {self.health}")
            
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    '''Healing method: Cannot exceed Character's max health'''    
    def heal (self):
        if self.health >= self.max_health:
            print(f"Already max HP. Cannot exceed maximum health")
        else: 
            self.health += 10
            print(f"{self.name} used healing. Health is now: {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 10
        print(f"{self.name} regenerates 10 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health = 180, attack_power = 20)

    def attack(self, opponent):
        random_attack_power = random.randint(15, self.attack_power)
        opponent.health -= random_attack_power
        print(f"{self.name} shoots arrow at {opponent.name} for {random_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special1(self, opponent):
        special_damage = self.attack_power * 1.8
        opponent.health -= special_damage
        print(f"{self.name} used headshot {opponent.name} causing {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special2(self, opponent):
        special_damage = self.attack_power * 1.5
        opponent.health -= special_damage
        print(f"{self.name} used poison arrow on {opponent.name} and takes {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    '''Healing method: Cannot exceed Character's max health'''    
    def heal (self):
        if self.health >= self.max_health:
            print(f"Already max HP. Cannot exceed maximum health")
        else: 
            self.health += 10
            print(f"{self.name} used healing. Health is now: {self.health}")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health = 150, attack_power = 30)

    def attack(self, opponent):
        random_attack_power = random.randint(20, self.attack_power)
        opponent.health -= random_attack_power
        print(f"{self.name} charges at {opponent.name} with his sword for {random_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special1(self, opponent):
        special_damage = self.attack_power * 1.5
        opponent.health -= special_damage
        print(f"{self.name} uses Holy Strike on {opponent.name} causing {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def special2(self, opponent):
        special_damage = self.attack_power * 1.3
        opponent.health -= special_damage
        print(f"{self.name} uses shield bash on {opponent.name} dealing {special_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    '''Healing method: Cannot exceed Character's max health'''    
    def heal (self):
        if self.health >= self.max_health:
            print(f"Already max HP. Cannot exceed maximum health")
        else: 
            self.health += 10
            print(f"{self.name} used healing. Health is now: {self.health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            special_attack = int(input("Choose a special attack to use (1-2): "))
            if special_attack == 1:
                player.special1(wizard)
            elif special_attack == 2:
                player.special2(wizard)
            else: 
                print("Invalid Choice")
        elif choice == '3':
                player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()