
#funtion to display the inventory of our backpack and the amount of of each item.
def inventory(backpack):
    if not backpack:
        print("You have not added anything to your backpack.")
        return
    try:
        items_in_backpack = 0
        print("Backpack inventory:")
        for item, count in backpack.items():
            print(f"{count} {item}")
            items_in_backpack += count
        print(f"You have {items_in_backpack} items in your backpack")
    except Exception:
        print("Something went wrong.")

#funtion to lette the user add the item and amount to the inventory by input
def additemtoinventory(inventory):
    while True: # to let the user add more the one item
        item = input("Enter the items name to add to the inventory or 'done' to finish adding items: ")
        if item.lower() == 'done':# if input is done, we break the while loop
            break
        if not item.isalpha(): # if the inbut is not only letters
            print("Please enter a valid item name, letters only.")
            continue
        try: # add the number of items after the item input, if the input is not number we print a error message
            count = int(input(f"Enter the number of {item} to add to your backpack: "))
            if item in inventory: #if we have it we add more
                inventory[item] += count
            else: # if not we add the amount from count
                inventory[item] = count
        except ValueError:
            print("Please enter a valid number.")
    return inventory


player_inventory = {}
player_inventory = additemtoinventory(player_inventory)
inventory(player_inventory)
