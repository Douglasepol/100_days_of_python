
'''

Problem: Create a Basic Shopping List Application

Write a Python program that simulates a simple shopping list. The program should be able to do the following:

1) Add items to the shopping list.
2) Remove items from the shopping list.
3) Display the current items in the shopping list.


'''

def add_item(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"Item {item} not found in the shopping list.")
    return shopping_list

def display_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")


shopping_list = []

# Adding items
shopping_list = add_item(shopping_list, "milk")
shopping_list = add_item(shopping_list, "bread")
shopping_list = add_item(shopping_list, "eggs")

# Displaying the list
display_list(shopping_list)

# Removing an item
shopping_list = remove_item(shopping_list, "bread")

# Displaying the list again
display_list(shopping_list)
