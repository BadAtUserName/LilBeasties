import time # To handle time tracking

#Def monster class
class Monster:
  def __init__(self, name):
    self.name = name  # Name of the monster
    self.hunger = 50  # Initial hunger level (0 = starving, 100 = full)
    self.happiness = 50  # Initial happiness level (0 = sad, 100 = joyful)
    self.energy = 50  # Initial energy level (0 = exhausted, 100 = fully rested)
    self.age = 0  # Initial age of the monster in days
    self.is_alive = True
    self.is_present = True # Tracks if the monster is still with the user
    self.boredom_threshold = 60 # time in seconds before monster gets bored
    self.last_interaction = time.time() #recored the current time
    self.ascii_art = ""  # Placeholder for ASCII art

  def talk(self):
    """Generate a conversational response based on the monster's mood."""
    if not self.is_alive:
      print(f"{self.name} is no longer here to talk. 💔")
      return
    
  def check_boredom(self):
    """Check if the monster is bored and might run away."""
    current_time = time.time()
    elapsed_time = current_time - self.last_interaction

  # If the elapsed time exceeds the boredom threshold, the monster runs away
    if elapsed_time > self.boredom_threshold and self.is_present:
      self.is_present = False
      print(f"Oh no! {self.name} got bored and ran away! 😢")

  # Responses based on happiness level
    if self.happiness > 80:
      print(f"{self.name} says: 'You're the best! Im so happy to have you!' 😊")
    elif self.happiness > 50:
      print(f"{self.name} says: 'Life's pretty good right now!' 😄")
    elif self.happiness > 30:
      print(f"{self.name} says: 'Im okay, but I could use a little fun.' 🐾")
    else:
      print(f"{self.name} says: 'Im feeling sad… can we play?' 😢")

     # Responses based on hunger level
    if self.hunger > 100:
      print(f"{self.name} says: 'I think I ate too much… ugh.' 😩")
    elif self.hunger < 30:
      print(f"{self.name} says: 'Im so hungry! Can I have a snack?' 🥺")
    
    # Responses based on energy level
    if self.energy < 20:
      print(f"{self.name} says: 'Im feeling really tired… can I nap?' 😴")

  def feed(self,amount): # Method to feed the monster
    """Feed the monster to reduce hunger."""
    if not self.is_alive:
      print(f"{self.name} is no longer with us and cannot eat. 💔")
      return
    
    self.hunger += amount
    self.last_interaction = time.time() #update the last interaction time

    if self.hunger > 150: #Monster dies
      self.is_alive = False
      self.hunger = 0
      print(f"Oh no! {self.name} was overfed and has passed away. 😭")
    elif self.hunger > 140: #Monster is overfed
      print(f"{self.name} says: 'Stop! I'm so full I can't move!' 🐾")
    elif self.hunger > 100: #Monster overfed but still alive
      print(f"Ugh too full, feel bloated")
    else: # Normal Feeding
      self.hunger = min(self.hunger, 100) #hunger capped at 100
      print(f"Yum, yum, yum in my tum {self.name} was so hungry")

  def play(self, amount): # Method to play with the monster
    """Play with your monster to keep it happy"""
    if not self.is_alive or not self.is_present:
      print(f"{self.name} is no longer with us and cannot play. 💔")
      return
    
    self.last_interaction = time.time() #update last interaction

    if self.energy > 10:
      self.happiness = min(self.happiness + amount, 100)
      self.energy = max(self.energy - 10, 0)
      print(f"Happy, Happy, Happy! {self.name} is so happy...and not bored")
    else:
      print(f"YAWN! Double Yawn {self.name} is sleepy")  

  def sleep(self):
    """The monster needs to sleep so it can rest and age"""
    self.energy = 100
    self.age += 1
    print(f"WEEEeee I {self.name} am so well rested")
    print(f"after all that sleep i'm {self.age} years old")

  def display(self):
    print(self.ascii_art)
    print(f"Name: {self.name}")
    print(f"Hunger: {self.hunger}")
    print(f"Happines: {self.happiness}")
    print(f"Energy: {self.energy}")
    print(f"Age: {self.age}")
    if not self.is_alive:
      print(f"status: {self.name} is no longer alive")

#Subclass for monsters
class Fluffernog(Monster):
  def __init__(self,name):
    super().__init__(name)
    self.fur_color = "Rainbow"
    self.energy = 70
    self.ascii_art = r"""
           _____
         .-'     `-.
       .'  _     _  '.
      /   (_)   (_)   \
     :  __           __ :
     | /  \  \_/  /  \  |
     | |   o       o   | |
     : \     \___/     / :
      \ '-._         _.-' /
       '.   `'-----'`   .'
         '-.           .-'
            '--.....--'

        """  # ASCII art for Fluffernog
    
  def fluff_up(self):
    """special action fluff does"""
    self.happiness = min(self.happiness + 20, 100)
    print(f"BBRrreIIIIbbbooof when i get happy i floof!")

class Zogamog(Monster):
  def __init__(self,name):
    super().__init__(name)
    self.belly_glow_color = "Blue"  # Unique attribute
    self.hunger = 30  # Zogamog get hungrier faster
    self.ascii_art = r"""
         ..-"       "-.
        .'  .-" "-.   '.
       /   (  o o  )    \
      :     |  ^  |      :
      |     \__v__/       |
      :         ~         :
       \   \_______/     /
        '.             .'
          '-..____...-'
        """  # ASCII art for Zogamog
  
  def belly_glow(self):
    """Special action unique to Zoglin."""
    print(f"{self.name}'s belly glows {self.belly_glow_color} and calms everyone around!")

class BeansBeans(Monster):
  def __init__(self, name):
    super().__init__(name)
    self.slime_color = "Grey"
    self.happiness = 20 #beansbeans are sad sad
    self.ascii_art = r"""
         .-"      "-.
      .'            '.
     /   .--.  .--.   \
    :   (    \/    )   :
    |    \        /     |
   /:     '-....-'      ;\
  / :                  ;  \
 (   '.              .'    )
  '-.  '-.        .-'   .-'
     '--' '--....--' '--'
        """  # ASCII art for BeansBeans

  def jiggle(self):
    """Special action unique to beansbeans"""
    self.happiness = min(self.happiness + 30, 100)
    print(f"{self.name} jiggled and is now extra happy! Happiness: {self.happiness}.")

class Food:
  def __init__(self, name, nutrition_value):
    self.name = name
    self.nutrition_value = nutrition_value

apple = Food("Apple", 10)
pizza = Food("Pizza", 25)
cupcake = Food("Cupcake", 15)

# Food options list
food_menu = [apple, pizza, cupcake]
    
  
#Function to handle  user inputs for interactions
def interact_with_monster(monster):
  while True:
    if not monster.is_alive: #if monster is dead stop interactions
      print(f"\n{monster.name} has passed away, game over")
      break

    if not monster.is_present:
      print(f"\n{monster.name} has run away. Game over. 😢")
      break

    #check boredom periodically
    monster.check_boredom()

    print("\What would you like to do?")
    print("1. Feed your monster")
    print("2. Play with your monster")
    print("3. Let your monster sleep")
    print("4. Talk to your monster")
    print("5. Quit")
    choice = input("Enter the number of your choice")

    if choice == "1": #Feed your monster
      print("Choose food to feed your monster")
      for i, food in enumerate(food_menu, 1):
        print(f"{i}. {food.name} (+{food.nutrition_value} hunger)")
      food_choice = int(input("Enter then number of your choice")) - 1

      if 0 <= food_choice <len(food_menu):
        selected_food = food_menu[food_choice]
        print(f"\nYou chose to feed your monster a {selected_food.name}!")
        monster.feed(selected_food.nutrition_value)
      else:
        print("Invalid choice please try again")


    elif choice == "2": #Play with your monster
      try:
        amount = int(input("how many minutes would you like to play with your monster (1-30)?"))
        if 1 <= amount <= 30:
          monster.play(amount)
        else:
          print("please enter a number betwixt 1-30")
      except ValueError:
        print("please choose a valid number")

    elif choice == "3": #Let monster sleep
      monster.sleep()
    
    elif choice == 4:
      monster.talk()  # Engage in conversation
    
    elif choice == 5:
      print(f"Bye bye {monster.name}! I'll be waiting.")
      break

    else:
      print("invalid choice please try again")



# Greet the user
print("Welcome to the Lil' Beasties Pet World!")
print("Here, you can adopt your very own monster and take care of it.")
print("Let's start by choosing your pet!")

#Monster creation and interaction
monster_classes = {
  "Fluffernog": Fluffernog,
  "Zogamog": Zogamog,
  "BeansBeans": BeansBeans}

# Display the options for monsters
print("\nChoose your monster type:")
for i, monster_type in enumerate(monster_classes.keys(), 1):
  print(f"{i}.{monster_type}")

choice = int(input("Enter the number of your choice: "))
selected_type_name = list(monster_classes.keys())[choice -1]
name = input("what will you name your monster?")

#Create the monster instance base on the user's choice
selected_class = monster_classes[selected_type_name]
my_monster = selected_class(name)
print(f"You created a {selected_type_name} named {name}")

#Display the monsters stats and art
my_monster.display()

# Start interacting with the monster
interact_with_monster(my_monster)
