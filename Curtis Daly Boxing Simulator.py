import random

#Thomas (or player name) (p) Starting Stat Variables
#Right now Thomas and opponent have random stats within a range.
#Stats can be changed to make results of matches more lopsided.

player_name = input("\nYou've done got yourself in a lot of trouble. What is your name?: ") #Thomas by default
p_action_points =random.randint(4,6) # This is how many turns / stamina you get per fight - slaps or misses.
p_hp = random.randint(30,40) # The amount of damage you can withstand before being knocked out
p_power = random.randint(7,13) # This modifier adds to damage inflicted
p_defense = random.randint (9,12) # This increases the chance that your opponent will miss you.
p_accuracy= random.randint(6, 9) # This is a modifier that helps get through defenses
p_action_points_recharge=random.randint(4,6) # This is how many action points get recharged before the next fight.

#Opponent (o) Starting Stat Variables - Eventually hope to have these altered by user preferences
# or different "opponents" come in preset varying types and strengths, weaknesses

opponent_name = input("\nWho's after you now?: Enter your opponents name: ")
o_action_points = random.randint(4,6)
o_hp = random.randint(30,40)
o_power = random.randint(7,13)
o_defense = random.randint (9,12)
o_accuracy = random.randint(6, 9)
o_action_point_recharge = random.randint(4,6)

#Thomas Attacking Opponent part 1 - this function is for determining if Thomas connects with his slaps.
# If random integer + accuracy stat is greater than opponent defense a hit was scored.

def p_hit_or_miss(p_defensefunc, p_accuracyfunc):
    p_hit = p_accuracyfunc + random.randint(0, 8)
    if p_hit > p_defensefunc:
        return True
    else:
        return False

#Thomas Attacking Opponent part 2 - this function is for determining how much damage Thomas does with his slaps.
# Damage = random integer + Thomas power.
def p_hit_damage(p_powerfunc):
    p_damage = p_powerfunc + random.randint(0, 8)
    return p_damage

#Thomas Attacking Opponent part 3 - this function is for updating opponent current health after damage inflicted
def damage_to_o(o_hpfunc, p_damagefunc):
    o_current_hp = o_hpfunc - p_damagefunc
    return o_current_hp

#Opponent Attacking Thomas - same fucntions and considerations are applied as per Thomas
def o_hit_or_miss(p_defensefunc, o_accuracyfunc):
    o_hit = o_accuracyfunc + random.randint(0, 8)
    if o_hit > p_defensefunc:
        return True
    else:
        return False

def o_hit_damage(o_powerfunc):
    o_damage = o_powerfunc + random.randint(0, 8)
    return o_damage

def damage_to_p(p_hpfunc, o_damagefunc):
    p_current_hp = p_hpfunc - o_damagefunc
    return p_current_hp


#Variables to keep track of fight number and fight statistics and starting values:

p_current_hp = p_hp #current health starts at player starting health, but will change due to damage incurred during a fight.

o_current_hp = o_hp

fights=1

player_victories=0.0000000001 # A tally of all a character's wins: knockouts, decisions -not set exactly 0 to prevent divide by 0 error later, done to other variables as needed

opponents_victories=0.0000000001

draws=0 # both characters standing, 0 action points left, and identical life(hp) remaining

p_slaps_landed = 0

p_slaps_total = 0.0000000001

o_punches_landed = 0

o_punches_total = 0.0000000001

# Character Attack Order is randomized in the combat loop.
# Each character's action is assigned a specific number
# If roll a 0, Check if Thomas scored a hit , if roll a 1, Check if Opponent Scored a hit
# If roll a 2, Thomas deals damage if scored a hit, if roll a 3 Opponent deals damage if scored a hit
#I tried embedding this in the functions - but the actions were not as random
attack_order = (0,1,2,3)

player_decisions = 0 # If both characters are still standing with 0 action points the one with more remaining life wins

opponents_decisions = 0

player_knockouts = 0 # A character brought the other to 0 or below hp and still has hp.

opponents_knockouts = 0


#Background Story
print(input(f"\n{opponent_name} is going to be hard to take down.  We'd better start the training simulator. Press ENTER to continue: "))

while fights <1001: #1000 fights being conducted - could be made user input eventually

    print(f"\nTHIS IS FIGHT {fights}") #fights is a variable to keep updating the number for each turn through the loop

    while o_current_hp> 0 and p_current_hp > 0: # as long as both are standing - both have hp

        attack_first = random.choice(attack_order)#added this to make sure characters attack in random sequence,
        # otherwise first attacker in the code gets a slight edge - throws about 20% more attacks, and gets more wins

        if p_hit_or_miss(o_defense,p_accuracy) == False and int(attack_first)==0 and p_action_points >0:
            p_action_points -= 1
            print(f"{player_name} missed! {player_name} has {p_action_points} remaining action points")
            p_slaps_total += 1

        if o_hit_or_miss(p_defense, o_accuracy) == False and int(attack_first)==1 and o_action_points > 0:
            o_action_points -= 1
            print(f"{opponent_name} missed! {opponent_name} has {o_action_points} remaining action points")
            o_punches_total += 1

        if p_hit_or_miss(o_defense, p_accuracy)== True and int(attack_first)==2 and p_action_points > 0:
            p_action_points -= 1
            p_damage_done = p_hit_damage(p_power)
            o_current_hp = damage_to_o(o_current_hp, p_damage_done,)
            print(f"{player_name} slapped and did {p_damage_done} damage to {opponent_name}! {player_name} has {p_action_points} remaining action points")
            print(f"{opponent_name} has {o_current_hp} health remaining")
            p_slaps_landed +=1
            p_slaps_total +=1

        if o_current_hp <= 0:
            print(f"{opponent_name} got knocked out!")
            player_victories += 1
            player_knockouts +=1
            break #A Knockout breaks the loop and a new fight starts

        if o_hit_or_miss(p_defense, o_accuracy)== True and int(attack_first)==3 and o_action_points >0:
            o_action_points -=1
            o_damage_done = o_hit_damage(o_power)
            p_current_hp = damage_to_p(p_current_hp, o_damage_done)
            print(f"{opponent_name} hit and did {o_damage_done} damage to {player_name}! {opponent_name} has {o_action_points} remaining action points")
            print(f"{player_name} has {p_current_hp} health remaining")
            o_punches_landed += 1
            o_punches_total += 1

        if p_current_hp <= 0:
            print(f"{player_name} got knocked out!")
            opponents_victories += 1
            opponents_knockouts +=1
            break

        if  p_current_hp < o_current_hp and o_action_points == 0 and p_action_points == 0:
            print(f"{opponent_name} wins by Decision!")
            opponents_victories += 1
            opponents_decisions +=1
            break# A decision breaks the loop and a new fight starts

        if  p_current_hp > o_current_hp and o_action_points == 0 and p_action_points == 0:
            print(f"{player_name} wins by Decision!")
            player_victories += 1
            player_decisions +=1
            break

        if  p_current_hp == o_current_hp and o_action_points == 0 and p_action_points == 0:
            print("It's a draw!")
            draws += 1
            break # A draw breaks the loop and a new fight starts - no character gets "credit"

# Reset variables to starting values, add +1 to fight tally
    fights += 1
    p_current_hp = p_hp
    o_current_hp = o_hp
    p_action_points = p_action_points_recharge
    o_action_points = o_action_point_recharge





# Fight Statistics
player_slaps_percentage = round(p_slaps_landed / p_slaps_total *100,0)

opponent_punch_percentage = round(o_punches_landed / o_punches_total *100,0)

player_victory_percentage = round(player_victories / fights * 100,1)

total_fight_check = player_victories + opponents_victories + draws

player_knockout_percentage = round((player_knockouts / player_victories*100),0)

opponent_knockout_percentage = round(opponents_knockouts/ opponents_victories*100,0)


# Convert things subject to decimal points to integers to make final chart look nice
# This may compromise tally accuracy a little bit from truncation.!
player_victories = int(player_victories)
opponents_victories = int(opponents_victories)
p_slaps_total = int(p_slaps_total)
o_punches_total = int(o_punches_total)
total_fight_check = int(total_fight_check)

# Simulation Summary
print("==============================================================================================================================================")
print(f"Congratulations {player_name}, you won {player_victory_percentage}% of your fights!")

print(f"\n{player_name} / Wins: {player_victories} / Knockouts {player_knockouts} / Knockout % {player_knockout_percentage} / Wins by Decision {player_decisions} / Draws {draws}")

print(f"\n{opponent_name} / Wins: {opponents_victories} / Knockouts {opponents_knockouts} / Knockout % {opponent_knockout_percentage} / Wins by Decision {opponents_decisions} / Draws {draws}")


print(f"\n{player_name} / Total Slaps Thrown: {p_slaps_total} / Total Slaps Landed {p_slaps_landed} / % Slaps Landed: {player_slaps_percentage}%")

print(f"\n{opponent_name} / Total Punches Thrown: {o_punches_total} / Total Punches Landed {o_punches_landed} / % Punches Landed: {opponent_punch_percentage}%")

print(f"\nTotal fights {total_fight_check}")

print(f"\nHey {player_name}, here is how I rank the current capabilities of you and {opponent_name}.")
print(f"\n{player_name} hp: {p_hp} / power: {p_power} / defense:{p_defense} / Accuracy: {p_accuracy} / Action Points:{p_action_points}")
print(f"\n{opponent_name} hp: {o_hp} / power: {o_power} / defense:{o_defense} / Accuracy: {o_accuracy} / Action Points:{o_action_points}")
print("\nScroll up to review your video footage, fight statistics, and stats to help guide your training before the real fight!")
print("==============================================================================================================================================")

continue_option =input("\nPress ENTER to run the simulation again or enter no to quit: ").lower()

# This is a duplicate fighting loop without background story and names being asked again to repeat the simulation as many times as wanted:
# I have a feeling there is a more efficient way to do this - since this is identical to the first half of the code.

while continue_option != "no":

        p_action_points = random.randint(4, 6)
        p_hp = random.randint(30, 40)
        p_power = random.randint(7, 13)
        p_defense = random.randint(9, 12)
        p_accuracy = random.randint(6, 9)
        p_action_points_recharge = random.randint(4,6)

        o_action_points = random.randint(4, 6)
        o_hp = random.randint(30, 40)
        o_power = random.randint(7, 13)
        o_defense = random.randint(9, 12)
        o_accuracy = random.randint(6, 9)
        o_action_point_recharge = random.randint(4, 6)

        p_current_hp = p_hp

        o_current_hp = o_hp

        fights = 1

        player_victories = 0.0000000001

        opponents_victories = 0.0000000001

        draws = 0

        p_slaps_landed = 0

        p_slaps_total = 0.0000000001

        o_punches_landed = 0

        o_punches_total = 0.0000000001

        attack_order = (0, 1, 2, 3)

        player_decisions = 0

        opponents_decisions = 0

        player_knockouts = 0

        opponents_knockouts = 0

        while fights <1001: #1000 fights being conducted - could be made user input eventually

            print(f"\nTHIS IS FIGHT {fights}")

            while o_current_hp> 0 and p_current_hp > 0: # as long as both are standing

                attack_first = random.choice(attack_order)#added this to make sure actions follow in random sequence, otherwise first attacker gets a slight edge

                if p_hit_or_miss(o_defense, p_accuracy) == False and int(attack_first) == 0 and p_action_points > 0:
                    p_action_points -= 1
                    print(f"{player_name} missed! {player_name} has {p_action_points} remaining action points")
                    p_slaps_total += 1

                if o_hit_or_miss(p_defense, o_accuracy) == False and int(attack_first) == 1 and o_action_points > 0:
                    o_action_points -= 1
                    print(f"{opponent_name} missed! {opponent_name} has {o_action_points} remaining action points")
                    o_punches_total += 1

                if p_hit_or_miss(o_defense, p_accuracy) == True and int(attack_first) == 2 and p_action_points > 0:
                    p_action_points -= 1
                    p_damage_done = p_hit_damage(p_power)
                    o_current_hp = damage_to_o(o_current_hp, p_damage_done, )
                    print(
                        f"{player_name} slapped and did {p_damage_done} damage to {opponent_name}! {player_name} has {p_action_points} remaining action points")
                    print(f"{opponent_name} has {o_current_hp} health remaining")
                    p_slaps_landed += 1
                    p_slaps_total += 1

                if o_current_hp <= 0:
                    print(f"{opponent_name} got knocked out!")
                    player_victories += 1
                    player_knockouts += 1
                    break  # A Knockout breaks the loop and a new fight starts

                if o_hit_or_miss(p_defense, o_accuracy) == True and int(attack_first) == 3 and o_action_points > 0:
                    o_action_points -= 1
                    o_damage_done = o_hit_damage(o_power)
                    p_current_hp = damage_to_p(p_current_hp, o_damage_done)
                    print(
                        f"{opponent_name} hit and did {o_damage_done} damage to {player_name}! {opponent_name} has {o_action_points} remaining action points")
                    print(f"{player_name} has {p_current_hp} health remaining")
                    o_punches_landed += 1
                    o_punches_total += 1

                if p_current_hp <= 0:
                    print(f"{player_name} got knocked out!")
                    opponents_victories += 1
                    opponents_knockouts += 1
                    break

                if p_current_hp < o_current_hp and o_action_points == 0 and p_action_points == 0:
                    print(f"{opponent_name} wins by Decision!")
                    opponents_victories += 1
                    opponents_decisions += 1
                    break  # A decision breaks the loop and a new fight starts

                if p_current_hp > o_current_hp and o_action_points == 0 and p_action_points == 0:
                    print(f"{player_name} wins by Decision!")
                    player_victories += 1
                    player_decisions += 1
                    break

                if p_current_hp == o_current_hp and o_action_points == 0 and p_action_points == 0:
                    print("It's a draw!")
                    draws += 1
                    break  # A draw breaks the loop and a new fight starts - no character gets credit

            fights += 1
            p_current_hp = p_hp
            o_current_hp = o_hp
            p_action_points = p_action_points_recharge
            o_action_points = o_action_point_recharge




        player_slaps_percentage = round(p_slaps_landed / p_slaps_total *100,0)

        opponent_punch_percentage = round(o_punches_landed / o_punches_total *100,0)

        player_victory_percentage = round(player_victories / fights * 100,1)

        total_fight_check = player_victories + opponents_victories + draws

        player_knockout_percentage = round(player_knockouts / player_victories*100,0)

        opponent_knockout_percentage = round(opponents_knockouts/ opponents_victories*100,0)

        player_victories = int(player_victories)
        opponents_victories = int(opponents_victories)
        p_slaps_total = int(p_slaps_total)
        o_punches_total = int(o_punches_total)
        total_fight_check = int(total_fight_check)

        print("==============================================================================================================================================")
        print(f"Congratulations {player_name}, you won {player_victory_percentage}% of your fights!")

        print(f"\n{player_name} / Wins: {player_victories} / Knockouts {player_knockouts} / Knockout % {player_knockout_percentage} / Wins by Decision {player_decisions} / Draws {draws}")

        print(f"\n{opponent_name} / Wins: {opponents_victories} / Knockouts {opponents_knockouts} / Knockout % {opponent_knockout_percentage} / Wins by Decision {opponents_decisions} / Draws {draws}")


        print(f"\n{player_name} / Total Slaps Thrown: {p_slaps_total} / Total Slaps Landed {p_slaps_landed} / % Slaps Landed: {player_slaps_percentage}%")

        print(f"\n{opponent_name} / Total Punches Thrown: {o_punches_total} / Total Punches Landed {o_punches_landed} / % Punches Landed: {opponent_punch_percentage}%")

        print(f"\nTotal fights {total_fight_check}")

        print(f"\nHey {player_name}, here is how I rank the current capabilities of you and {opponent_name}.")
        print(f"\n{player_name} hp: {p_hp} / power: {p_power} / defense:{p_defense} / Accuracy: {p_accuracy} / Action Points:{p_action_points}")
        print(f"\n{opponent_name} hp: {o_hp} / power: {o_power} / defense:{o_defense} / Accuracy: {o_accuracy} / Action Points:{o_action_points}")
        print("\nScroll up to review your video footage, fight statistics, and stats to help guide your training before the real fight!")
        print("==============================================================================================================================================")

        continue_option =input("\nPress ENTER to run the simulation again or enter no to quit: ").lower()

#Sentinel word to end program
        if  continue_option == "no":
            break