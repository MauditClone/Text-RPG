import random
from clocks3 import Clock
import replit

#i have no clue how to add an internal clock system that resests when time reaches 24:00

clock = Clock(6,0)


#hero stats
hp = 30
hpmax = 60
lstAttack = [0,15]

tKill = 0

#add weapons with specific stats, that you can find in looting, instead of just numbering weapons
# def sword():
#   sDamage = 

def game():
  hp = 30
  hpmax = 60
  lstAttack = [0,15]
  
  print(f"""\n\tThe hero woke up like they did every other morning, a horrid nightmare lingering just out of reach. It was 6:00am, the sun was shinning and the birds were singing.
  \n\n\t{hero} got out of their bed and remembered that they had forgotten about one of their trades due today in the nearby town.
  \n\n\tAnd so the hero packed their things and embarked on their journey!""")
  
  print("\n------------------------------------")
  print("\nYou have exited your home and are now outside. What do you want to do?")
  
  play = True
  
  #time = 8:00
  #inventory:
  steps = 0
  rocks = 0
  coins = 0
  armor = 0
  weapon = 0
  herbs = 0
  meat = 0
  kill = 0
  
  while play == True:
    global tKill
    
    if hp > 50:
      print(f"\nSuddenly, the world around you sharpens. {hero} feels as though their senses are about to explode. The agony is sky rocketing! Your hp is too high!")
      dangerH = input("\nStab yourself to save yourself from eternal pain! Hurry! \n\t\t[stab/suffer] : ").lower()
      if dangerH == "suffer":
        print("\nYour vision explodes and blood bursts out of all your orrifices. Your high hp was too much for your bodily essence to handle.")
        
        print("\n\t[GAME OVER]")
        input("\nYou died. Press enter to play again.")
        replit.clear()
        hp = 30
        game()
      elif dangerH == "stab":
        print(f"""\n{hero} shakily grabs a sharp rock on the ground. You take a deep breath.
        BADUMP
        BADUMP
        Your heart is beating out of your chest.
        """)
        print("""\nMaking up your mind you swing the rock down into your leg.
        AAAARGH
        You cry out in pain.
        But luckily, you realize that it did aleviate your previous agony.""")
        hp = 30
        print(f"\nYour hp is now {hp}.")
    
    action = input("""\nWould you like to: 
      -> Walk
      -> Explore
      -> Set up Camp
      -> Inventory
    \n-> """).lower()
    
    print(f"\n-> You have chosen {action}!")
    
    if action == "walk":
      print(f"\nAnd so, {hero} continued their journey.")
      #randomly chose a number of km in between [0.01, 5km]
      #chance of spawn enemy or loot if walk is > 0.5km
      #chance of spawm village if walk is > 
      
      step = round(random.uniform(0.01, 5.00), 2)
      print(f"You've walked {step} km")
      
      if step >= 0.5:
        rEorL = random.randint(0,1)
        if rEorL == 0:
        
          print("\nYou have encountered a foe!")
        
          indexEnemies = random.randint(0, 1)
          lstEnemies = ["slime", "orc"]
          enemy = lstEnemies[indexEnemies]
        
          if enemy == "slime":
            eHp = 12
            eHpmax = 20
            lstEattack = [0, 1, 1, 1, 2, 3, 4, 5, 6, 7]
        
            print("It's a Slime!")
        
          elif enemy == "orc":
            eHp = 25
            eHpmax = 35
            lstEattack = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
            print("It's an Orc!")
        
          print(f"""\nYour HP is {hp}.
          The {enemy}'s hp is {eHp}.
          """)
        
          print(f"The {enemy} is approaching! Make your move.")
        
          while eHp > 0:
            battleAction = input("\n\t[attack/heal] : ").lower()
        
            if battleAction == "heal":
              healing = random.randint(1, 10)
              hp += healing
              print(
                f"\nMiraculously, you've regained {healing} health. As if the world was bending to your will. Your HP is now {hp}!"
              )

              #to limit healing
              if hp > 50:
                print(f"\nSuddenly, the world around you sharpens. {hero} feels as though their senses are about to explode. The agony is sky rocketing! Your hp is too high!")
                dangerH = input("\nStab yourself to save yourself from eternal pain! Hurry! \n\t\t[stab/suffer] : ").lower()
                if dangerH == "suffer":
                  print("\nYour vision explodes and blood bursts out of all your orrifices. Your high hp was too much for your bodily essence to handle.")
                  #game ends, or does it
                  print("\n\t[GAME OVER]")
                  input("\nYou died. Press enter to play again.")
                  replit.clear()
                  hp = 30
                  game()
                elif dangerH == "stab":
                  print(f"""\n{hero} shakily grabs a sharp rock on the ground. You take a deep breath.
                  BADUMP
                  BADUMP
                  Your heart is beating out of your chest.
                  """)
                  print("""\nMaking up your mind you swing the rock down into your leg.
                  AAAARGH
                  You cry out in pain.
                  But luckily, you realize that it did aleviate your previous agony.""")
                  hp = 30
                  print(f"\nYour hp is now {hp}.")
        
            elif battleAction == "attack":
              print(f"\nThe {enemy} lunges towards you!")
        
              indexDamage = random.randint(0, 9)
              damage = lstEattack[indexDamage]
              hp -= damage
        
              print(f"You have taken {damage} damage. Your HP is now {hp}.")
        
              print(f"\nYou've attacked the {enemy}")
              eDamage = random.randint(0, 14)
              eHp -= eDamage
        
              print(f"The {enemy} has taken {eDamage} damage. Their HP is now {eHp}.")
        
            elif battleAction == "die":
              hp -= hp
              break
        
            elif battleAction == "kill":
              eHp -= eHp
              break
        
          #this is supposed to make it so that once the enemy dies it goes back to actions
          if eHp <= 0:
            print(
              f"The {enemy} tries to flee. However, its attempts were futile as it dies on the spot."
            )
            print(f"\nYou've defeated the {enemy}!")
            fightStatus = True
        
          #this is supposed to bring you back to beginning of game
          if hp <= 0:
            print(
              f"\nThe {enemy} swung towards the hero one last time. Your life flashes before your eyes, you couldn't do anything but watch."
            )
            print("\n\t[GAME OVER]")
        
            input("\nYou died. Press enter to play again.")
            replit.clear()
            #game = "main"
            fightStatus = False

          # This code executes AFTER the battle, either won or loss
          if fightStatus == True:
            # I won!
            kill += 1
            tKill += 1
          else : 
            # I lost!
            # or you can put death message in battle.py, before you do return False
            game()
          
    
        elif rEorL == 1:
          #loots.main()
          lstLoot = ["coins", "cool rocks", "armor", "weapon"]
          indexLoot = random.randint(0,3)
          loot = lstLoot[indexLoot]
        
          print("\nOn your walk you've found loot!")
        
          if loot == "cool rocks":
            numRocks = random.randint(2,4)
            rocks += numRocks
        
            print(f"Your loot is {numRocks} cool rocks!!")
        
          elif loot == "coins":
            numCoins = random.randint(1,4)
            coins += numCoins
            
            print(f"Your loot is {numCoins} coins.")
        
          elif loot == "armor":
            armor += 1
        
          elif loot == "weapon":
            weapon += 1
        
  
      elif step < 0.5:
        print("The hero continues walking down the same boring path. Nothing new ahead.")
          
      steps += step
    
      print(f"\nYou've walked {steps} km in total.")
      clock.incrementTime(1,0)
      print(f"\nThe current time is {clock.getTime()}.")
    
    elif action == "explore":
      #hero looks around
      #hero can find items:
        #water
        #herbs
        #animal
          #hero can attack animal
          #animal drops food
      
      #explore.main()
      indexlook = random.randint(0,3)
      lstLook = ["water", "herbs", "an animal", "nothing"]
      look = lstLook[indexlook]
    
      print("""\nWhile walking, the Hero decides to look around. The scenary was plain, nothing out of the ordinary. In fact, it looked like every other scenery, scarily so. You shrug the uncanny valley off, and forage around to see if anything sticks out.\n""")

      #this is for if the random variable is water
      if look == "water":
        drink = input("Right in front of you is a stream of water. Would you like to drink it? [yes/no] : ").lower()
    
        if drink == "no":
          pass
        elif drink == "yes":
          indexWater = random.randint(0,1)
          lstWater = ["dirty water", "clean water"]
          water = lstWater[indexWater]
    
          if water == "dirty water":
            hp = hp - 5
            print(f"\nYuck!! Turns out the water was mud. You lost 5 health. \nYour hp is now {hp}.")
          elif water == "clean water":
            hp = hp + 5
            print(f"\n{hero} kneels by the stream and cups their hands under water. You take a sip of the water. \nHow refreshing! \n\nYou've gained 5 health. Your hp is now {hp}.")

      #if random variable found is herbs
      elif look == "herbs":
        herbs += 2
        print(f"{hero} spots something in the grass. Its herbs! These will be useful for medecin.")

      #if random variable is an animal
      elif look == "an animal":
        indexAnimal = random.randint(0,2)
        lstAnimal = ["tiger", "cow", "cat"]
        animal = lstAnimal[indexAnimal]
        
        print(f"The bush behind you rustles. You turn around slowly only to be met with a {animal}!")

        #what animal is it
        if animal == "cow":
          input("Your stomach growls as you approach the cow. [attack] : ").lower()
          print("""\nSLASH
          \nThe cow has been slain! You gained some meat!""")
          meat += 1

        #if tiger start fighting sequence similar to battle.py
        elif animal == "tiger":
          tHp = 10
          while tHp >= 0:
            
            lstTAttack = [1,2,3,4,5]
            indexTAttack = random.randint(0,4)
            tEAttack = lstTAttack[indexTAttack]

          #fighting tiger: start
            print(f"\nThe tiger leaps forward! The hero tries to dodge but {hero} takes {tEAttack} damage.")
            hp = hp - tEAttack

            print(f"Your hp is {hp}.")
            tFight = input("\nAs the tiger is landing you take your shot. [attack/heal] : ")

            #choice for tiger
            if tFight == "attack":
              tAttack = lstTAttack[indexTAttack]
              print(f"You attack the tiger, giving it {tAttack} damage.")
              tHp = tHp - tAttack

            #if low health and choice is heal
            elif tFight == "heal":
              hp = hp + 5
              print(f"Miraculously, as if world bent to your will. Your hp is now {hp}.")

              if hp > 50:
                print(f"\nSuddenly, the world around you sharpens. {hero} feels as though their senses are about to explode. The agony is sky rocketing! Your hp is too high!")
                dangerH = input("\nStab yourself to save yourself from eternal pain! Hurry! \n\t\t[stab/suffer] : ").lower()
                if dangerH == "suffer":
                  print("\nYour vision explodes and blood bursts out of all your orrifices. Your high hp was too much for your bodily essence to handle.")
                  #game ends, or does it
                  print("\n\t[GAME OVER]")
                  input("\nYou died. Press enter to play again.")
                  replit.clear()
                  hp = 30
                  game()
                elif dangerH == "stab":
                  print(f"""\n{hero} shakily grabs a sharp rock on the ground. You take a deep breath.
                  BADUMP
                  BADUMP
                  Your heart is beating out of your chest.
                  """)
                  print("""\nMaking up your mind you swing the rock down into your leg.
                  AAAARGH
                  You cry out in pain.
                  But luckily, you realize that it did aleviate your previous agony.""")
                  hp = 30
                  print(f"\nYour hp is now {hp}.")

          while tHp <= 0:
            print("You have slain the tiger! You collect 3 meat.")
            meat += 5
            break

          while hp <= 0:
            print("\nThe tiger takes advantage of you recomposing yourself and kills you.")
            print("\n\t[GAME OVER]")
            input("\nYou died. Press enter to play again.")
            replit.clear()
            game()
            
      elif look == "nothing":
        print("The hero searched hard, but couldn't find anything.")

      clock.incrementTime(1,0)
      print(f"\nThe current time is {clock.getTime()}am/pm.")

    #if choice is set up camp
    elif action == "set up camp" or action == "camp":
      #sleep 
      #regen health
      #randomly chose amount hours slept from [1, 7]
      #if clock.getTime() == 
      print(f"\nThe current time is {clock.getTime()}.")
      print("\nThe journey was starting to get to you. And so the hero took out their bedroll and laid down on the floor. Soon enough you fell asleep.")
      print(f"\nThe current time is {clock.getTime()}.")
      clock.incrementTime(7,0)
      hp = 30
      print("""
      Zzz
      Zzz
      Zzz
      ...
      Zzz.!
      Sunlight hits your face as you yawn and stretch awake.""")
      print(f"\nThe current time is {clock.getTime()}.")
      print("\nYou've slept a full 7 hours! How refreshing. Your hp has regenerated!")
      

    #if choice is inventory
    elif action == "inventory":
      #open inventory
        #can eat food
        #equip armor
        #heal
        #check health, hunger and money
  
      print(f"""You have this in your inventory:
      \t{coins} coins
      \t{rocks} cool rocks
      \t{armor} armor
      \t{weapon} weapon
      \t{herbs} herbs
      \t{meat} meat""")

      iOption = input("\nIs there anything you would like to use? : \n-> ").lower()

      #long list of actions for each
      if iOption == "coins":
        pass
        
      elif iOption == "rocks":
        if rocks <= 5 and rocks > 0:
          print(f"{hero} looks at their colourful and unique assortion of pebbles. They were worth the time of collecting, but it they might become inconvenient if you collect any more.")
          
        elif rocks <= 11 and rocks >= 6:
          print("These are kind of getting heavy")
          
        elif rocks > 11:
          print("You pant in exhaustion. The weight of the rocks were starting to get to you. But they were pretty! And so you keep them in your pockets. However, you lose 2 health.")
          hp = hp - 2
          print(f"Your hp is now {hp}")
          
        #easter egg for longerterm veterans
        elif rocks >= 100:
          print("Holy crap, you say to yourself. That's a lot of rocks!! No wonder you back hurt so much.")
          print("As if your body was only now made aware of the pain it was under, you suddenly lose all your health.")
          replit.clear()
          print("GAME OVER")
          print("\nYou died by rocks. The rocks you collect! L.")
          game()
        #once done continue code
        pass

      elif iOption == "armor":
        print("This option is not currently available on this version of the game. Please continue on and wait patiently until next update!")
        # if armor > 0:
        #   equip = input("\nWould you like to equip your armor? [yes/no] : ").lower()
          #equipment choice
          #make armor more useful
          #the hp addition is temporary
          #eventually calculate armor stats into all battles
        #   if equip == "yes":
        #     hp += armor * 2
        # else:
        #   pass
      elif iOption == "weapon":
        print("This option is not currently available on this version of the game. Please continue on and wait patiently until next update!")
        # if weapon > 0:
        #   equipW = input("\nWould you like to equip your weapon")
        #   lstAttack = [1,18]

      elif iOption == "herbs":
        print(f"Herbs can be used to heal hp. Your hp is {hp}.")
        
        if herbs > 0:
          eatH = input("Would you like to eat herb? [yes/no] : ").lower()
          
          #eat herb  
          if eatH == "yes":
            hp = hp + 4
            print(f"You've eaten an herb! Your hp is now {hp}.")

          else:
            pass
        else:
          pass

      elif iOption == "meat":
        print(f"Meats can be used to heal hp. Your hp is {hp}.")
        if meat > 0:
          eatM = input("Would you like to eat meat? [yes/no] : ").lower()
          #eat herb  
          if eatM == "yes":
            hp = hp + 4
            print(f"You've eaten meat! Your hp is now {hp}.")
          else:
            pass

        else:
          pass

      elif iOption == "stats":
        print("You look around startled as a voice comes out of nowhere. It echoes in your ears, like it was only meant for you to hear. \n\t'You sure you want to know? Alrigh then.")

      else:
        print("Invalid.")

      clock.incrementTime(0,30)
      print(f"\nThe current time is {clock.getTime()}.")
      #print(clock)

    #if clock reaches 10oClock 
    if clock.getTime() == "22:00" or clock.getTime == "21:30":
      print("Wow! Look at the time. You should get some rest!")

    elif clock.getTime() == "05:00":
      print("You stop and take a moment to admire the sunrise.")

    elif clock.getTime() == "19:30" or clock.getTime() == "20:00":
      print("You stop for a moment to enjoy the sunset.")
      
hero = str(input("What is the name of our hero? [enter name] : \n-> ")).capitalize()

#start of the game
#display title
print(f"\nWELCOME TO LUCID! Home to our very own hero, {hero}!")
print("\n------------------------------------")

game()
