"""
Chai Tea Maker
==============

A simple program that walks you through making a warm, spiced cup of chai tea
(masala chai) from scratch.

Run it with:

    python chai.py

"""


def show_ingredients():
    """Print the list of ingredients needed to make chai tea."""
    print("=" * 50)
    print("INGREDIENTS (makes 2 cups)")
    print("=" * 50)
    ingredients = [
        "2 cups water",
        "2 cups whole milk (or any milk of your choice)",
        "2-3 teaspoons loose black tea (or 2-3 tea bags)",
        "1-2 tablespoons sugar (adjust to taste)",
        "4-5 green cardamom pods, lightly crushed",
        "1 small cinnamon stick",
        "3-4 whole cloves",
        "1/2 inch piece of fresh ginger, sliced or grated",
        "A pinch of black peppercorns (optional, for extra warmth)",
    ]
    for item in ingredients:
        print(f"  - {item}")
    print()
# above code explanation
#
# def tells python you are creating a function
# 
#show_ingredients is the functions name. 
# 
# () means the function currently takes no 
# arguments
# 
# : tells python with the function body 
# starts here 
#
#  NOTe: important
# defining a function does not execute it.
# you need to call it. 
# 
#  show_ingredients()
 # 
 # Next, we have the docstring
 #
 # """ Print  the list of ingredients needed to make chai tea """
 #
 # above , this is called a docstring .
 # 
 # it describes what the function does
 # 
 # think  of it as a little explanation for 
 # someone reading you code.
 #
 # We know what a comments is  #  symboll
 # 
 # Printing a divider
 # 
 # print("=" * 50)
 #
 # create a list [] brackets
# 
#  The square brackets [] create a list.

# A list can store multiple values.

# Each ingredient is a string, which means text.

# You could also create a simple list like this:
#
# What does for item in ingredient do?
#  > loop through the list
#  > for starts a loop 
#  > item is a temporary variable
# > in ingredients tells python to go through
# the  ingredients list
#   > print() displays each item
# 
# Python takes on ingredient at a  time.
#
# first loop:  
# item = '2 cups water'
#
# second loop
#  item = '2 cups whole milk'
#
# third loop 
#  item =. '2 -3 teaspoons loose black tea'
#
# it continues until all ingredients has 
# been printed 
# 
# what does f-string do?
#
# print(f' - {item}')
#  > the f allows you to insert a variable 
# inside a string using  curly braces {}

def show_instructions():
    """Print step-by-step instructions for making chai tea."""
    print("=" * 50)
    print("HOW TO MAKE CHAI TEA")
    print("=" * 50)
 
    steps = [
        "1. Crush the spices: Lightly crush the cardamom, cloves, and "
        "peppercorns to release their flavor.",
        "2. Boil the water: Pour the water into a saucepan and add the "
        "crushed spices, cinnamon stick, and ginger.",
        "3. Simmer the spices: Bring the water to a boil, then lower the "
        "heat and let it simmer for 4-5 minutes until the water is fragrant.",
        "4. Add the tea: Stir in the loose black tea (or tea bags) and let "
        "it brew for 2-3 minutes.",
        "5. Add the milk: Pour in the milk and raise the heat until the "
        "chai just starts to bubble up.",
        "6. Sweeten: Add the sugar and stir until it fully dissolves. "
        "Taste and add more if you like it sweeter.",
        "7. Strain and serve: Turn off the heat and strain the chai "
        "through a fine sieve into cups.",
        "8. Enjoy: Serve hot and enjoy your homemade chai!",
    ]

    for step in steps:
        print(step)

    print()
    print("TIP: For a richer flavor, let the chai simmer a little longer")
    print("     before straining. Adjust spices and sweetness to your taste.")
    print()


def main():
    """Run the chai tea making program."""
    print()
    print("Welcome to the Chai Tea Maker! 🍵")
    print()
    show_ingredients()
    show_instructions()
    print("=" * 50)
    print("Happy brewing!")
    print("=" * 50)


if __name__ == "__main__":
    main()

# creat folder , directory , organize

# Python/ main folder python-exercises
# └── 01_basics/
#     ├── 01_variables.py
#     ├── 02_data_types.py
#     ├── 03_string_repetition.py
