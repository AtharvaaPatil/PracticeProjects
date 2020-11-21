
from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import Items



# Create Black Magic
fire = spell("Fire", 25, 600, "black")
thunder = spell("Thunder", 25, 600, "black")
blizzard = spell("Blizzard", 25, 600, "black")
meteor = spell("Meteor", 40, 1200, "black")
quake = spell("Quake", 32, 140, "black")

# Create White Magic
cure = spell("Cure", 25, 620, "white")
cura = spell("Cura", 32, 1500, "white")

# Create some Items
potion = Items("Potion", "potion", "Heals 50 HP", 50)
hipotion = Items("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Items("Super Portion", "potion", "Heals 1000 HP", 1000)
elixer = Items("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Items("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Items("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos:", 1260, 65, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 2160, 65, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 1060, 65, 288, 34, player_spells, player_items)

enemy = Person("Magus", 11200, 100, 525, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0 

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("======================")

    print("\n\n")
    print("NAME                     HP                                   MP")
    for player in players:
        player.get_stats()

    print("\n")


    for player in players:

        player.choose_actions()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough Hp\n" + bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC )
            elif spell.type == "black":
                player.reduce_mp(spell.cost)
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE +"\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left.." + bcolors.ENDC)
                continue
            
            player.items[item_choice]["quantity"] -= 1
            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" +  item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks for " + str(enemy_dmg) + bcolors.ENDC)

    print("==============================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" +str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:# problem
        print( bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC )
        running = False