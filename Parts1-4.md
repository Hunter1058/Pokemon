:busts_in_silhouette: Team Breakdown (4 People)
:technologist: Person 1: Move Class Developer
Main responsibility: Build the Move class
Tasks:
Create the Move class
Implement the __init__ constructor with:
move_name
elemental_type
low_attack_points
high_attack_points
Write the get_info() method:
Must return:
Tackle (Type: Normal): 5 to 20 Attack Points

Write the generate_attack_value() method:
Use random.randint(low, high)
Return the value (don’t print inside the method)
Deliverable:
Fully working Move class
Tested with at least 1 sample object

:technologist: Person 2: Move Objects + Loop Logic
Main responsibility: Use the Move class
Tasks:
Create all 9 Move objects with correct values:
Tackle, Quick Attack, Slash, Flamethrower, Ember, Water Gun, Hydro Pump, Vine Whip, Solar Beam
Store them in a list
Write the loop that runs 3 times:
Randomly select a move (random.choice)
Print get_info()
Print generated attack value
Remove the move from the list (list.remove())
Also:
Add:

input("Press enter to continue...")

Deliverable:
Clean working loop with no duplicate moves
Proper formatting output

:technologist: Person 3: Pokemon Class Developer
Main responsibility: Build the Pokemon class
Tasks:
Create the Pokemon class
Implement the __init__ constructor:
name
elemental_type
hit_points
Write the get_info() method:
Format:
Charmander - Type: Fire - Hit Points: 55

Write the heal() method:
Add 15 to hit_points
Print:
Charmander has been healed to 70 hit points.

Do NOT return anything
Deliverable:
Fully working Pokemon class
Tested with at least 1 object

:technologist: Person 4: Pokemon Objects + Integration
Main responsibility: Use Pokemon class + finalize program
Tasks:
Create 3 Pokemon objects:
Bulbasaur (Grass, 60)
Charmander (Fire, 55)
Squirtle (Water, 65)
Then:
Print Charmander info
Call heal() on Charmander
Print Charmander info again
Then:
Put all 3 Pokémon into a list
Loop through and print get_info() for each
Final Responsibilities:
Combine everyone’s code into ONE file
Make sure:
Classes are at the top
No duplicate code
Everything runs in correct order

:scales: Why This Is Fair
Person 1 & 3 → each build a class (equal difficulty)
Person 2 & 4 → each handle object creation + program flow (equal workload)
Everyone writes meaningful code (no “easy” or “filler” roles)
