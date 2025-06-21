# NAME: Hilary Chol Libo Nyawella
# REG. NO. M25B13/050
# ACC. NO B33493

#CHALLANGE 4: INVESTIGATION SCENE
def investigation_scene():
    print("You arrive at a daily lit room with clues scattered around.")
    print("You find a note on the table.")
    if flashlight_available:
        print("You can see better with your flashlight.")
        print("The note reads, 'The code to the safe is 4732.'")
    else:
        print("The notes reads, 'You need to find the fashlight first.'")

def open_safe(code):
    if code == 4732:
        print("The safe opens, revealing a hidden treasure.")
        print("Congratulations! You solved the mystery.")
    else:
        print("The safe remains locked. Try again.")

flashlight_available = True
investigation_scene()
safe_code = int(input("enter safe code: "))
open_safe(safe_code)

