# Manny Pagan
# Sept 24th Python Course
# Assignment 2
# Due: Oct 3rd

# The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps! Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:
#
# ```
# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep.
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars.
# Otherwise T-Rex gives a toothy smile.


angry = True
bored = False
hungry = False
tired = True

def dino_moods():

    if tired and hungry:
        print("T-rex eats the Triceratops")
    elif hungry and bored:
        print("T-rex eats the Iguanadon")
    elif tired:
        print("T-rex is tired, he goes to sleep")
    elif angry and bored:
        print("T-rex will fight with the Velociraptor")
    elif angry or bored:
        print("T-rex roars")
    else:
        print("T-rex smiles!")

dino_moods()