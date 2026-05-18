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
print(item_list)