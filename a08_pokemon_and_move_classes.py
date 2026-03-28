# Hunter Potter, Penina Strong, Eriko Peterson, Eugenie Son

#imports
import random

# Create Pokemon Class
class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"

    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")
        
#Create move class
class Move:
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name #store name of move
        self.elemental_type = elemental_type #store element type of move
        self.low_attack_points = low_attack_points #store minimum damage move can do
        self.high_attack_points = high_attack_points #store maximum damage move can do

    def get_info(self):
        #return string with move details
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"

    def generate_attack_value(self):
        #Generate and return a random attack value between the low and high points
        return random.randint(self.low_attack_points,self.high_attack_points)

    # I made a basic class Move so I could run my code and make sure it works, the additional attributes still need made for it. --Hunter

# 9 Move objects, list, and random selector
oTackle = Move("Tackle", "Normal", 5, 20)
oQuickAttack = Move("Quick Attack", "Normal", 6, 25)
oSlash = Move("Slash", "Normal", 10, 30)
oFlamethrower = Move("Flamethrower", "Fire", 5, 30)
oEmber = Move("Ember", "Fire", 10, 20)
oWaterGun = Move("Water Gun", "Water", 5, 15)
oHydroPump = Move("Hydro Pump", "Water", 20, 25)
oVineWhip = Move("Vine Whip", "Grass", 10, 25)
oSolarBeam = Move("Solar Beam", "Grass", 18, 27)

MovePool = [oTackle, oQuickAttack, oSlash, oFlamethrower, oEmber, oWaterGun, oHydroPump, oVineWhip, oSolarBeam]
# Randomly selects 3 moves
for move in range(3):
    randomMove = random.choice(MovePool)
    print(randomMove.get_info())
    print(f'Generated attack value: {randomMove.generate_attack_value()}')
    MovePool.remove(randomMove)
input("Press Enter to continue... ")

 # Create Pokemon objects
pikachu = Pokemon("Pikachu", "Electric", 60)
mudkip = Pokemon("Mudkip", "Water", 55)
magikarp = Pokemon("Magikarp", "Water", 65)

# Print Pikachu info
print(pikachu.get_info())
# Heal Pikachu
pikachu.heal()
# Print Pikachu info again
print(pikachu.get_info())

# Pokemon list
pokemon_list = [pikachu, mudkip, magikarp]
# Loop through and print the mons
for pokemon in pokemon_list:
    print(pokemon.get_info())