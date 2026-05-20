#Final code

def scan_items():
    items = []
    scaning_loop = False
    print()
    while scaning_loop == False:
        item = input('Please input items (to finish type "done"): ').lower()
        if item == 'done':
            contunue_question = input('Are you sure you have no more items to input? (yes/no): ').lower()
            if contunue_question == 'yes':
                scaning_loop = True
            else:
                scaning_loop = False
        else:
            items.append(item)
    return items
    print()

item_list = scan_items()

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
print(f"\nOur updated inventory stock is as follows: {Updated_inventory}\n")
#total_cost is the number to send to the next step

from enum import member

MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}

#do you have a discount?
member_id = input("Do you have member discount? (yes/no) ").lower()

#if yes
if member_id == "yes":
    id = input("What is your member ID: ").capitalize()
    if id in MEMBERS.keys():
        member = MEMBERS[id]
        print(f" Hi {member['name']}, your discount is {member['discount']} ")

    total_discount = total_cost * member['discount']
else:
    print(f"Total is ${total_cost}")

subtotal = total_cost-total_discount

def calculate_tax(amount=total_cost, tax_rate=0.0825):
    total = amount*tax_rate
    return total
tax_time = calculate_tax

def generate_receipt(items, inventory1, subtotal, membership, total_discount, total):
    print("\n" + "="*30)
    print("FRESHCART RECEIPT")
    print("="*30)
    for item in items:
        for product in inventory1:
            if item == product:
                print(f"{item} @ ${inventory1[product]['price']:.2f}") #This needs to find the price within the inventory dictionary
    print("-"*30)
    print(f"Subtotal: ${subtotal:.2f}")
    if membership:
        print(f"Membership Discount: -${total_discount:.2f}")
    print(f"Tax: ${calculate_tax(subtotal-total_discount):.2f}")
    print(f"Total (incl. tax): ${total}")
    print("="*30)

generate_receipt(item_list,INVENTORY,subtotal,member_id,total_discount,tax_time)
