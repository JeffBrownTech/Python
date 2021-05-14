# Fantasy Game Inventory
# Write a function to display a player's inventory in the fantasy game
# Write a function 

def displayInventory(inventory):
    totalItems = 0
    print('Inventory:')

    for k, v in inventory.items():
        totalItems = totalItems + v
        print(str(v) + ' ' + str(k))
    
    print('Total number of items: ' + str(totalItems) + '\n')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory.setdefault(item, 1)
    return inventory

playerInventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(playerInventory)
playerInventory = addToInventory(playerInventory, dragonLoot)
print('You slayed the dragon and collected new things!\n')
displayInventory(playerInventory)