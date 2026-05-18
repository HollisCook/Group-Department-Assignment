#Inventory dictionary
INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}

#Necessary Functions
def inventory_check(items_purchased = [],inventory_new = INVENTORY):
    for i in items_purchased:
        for item in inventory_new.keys():
            if i == item:
                inventory_new[item]["stock"] = inventory_new[item]["stock"] - 1
    return inventory_new

def order_price(items_purchased = [],inventory = INVENTORY):
    price = 0
    for i in items_purchased:
        for item in inventory:
            if i == item:
                price += inventory[item]["price"]
    return price

#Input
Order = item_list

#Processing
Updated_inventory = inventory_check(items_purchased=Order)
total_cost = order_price(items_purchased=Order)

#Ouput
print(f"\nOur updated inventory stock is as follows: {Updated_inventory}")
#total_cost is the number to send to the next step