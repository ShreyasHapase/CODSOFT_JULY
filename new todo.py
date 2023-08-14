li = []


def add():
    flag = True
    while flag:
        items = input("Enter items in list:")
        li.append(items)
        print(li)
        choice = input("if you want to add another item press Y: ")
        if choice == 'y':
            flag = True
        else:
            flag = False
            print("your list items are : ")
            print(li)
add()

flag1 = True
while flag1:
    choice_up = input("enter u for updating list : ")
    if choice_up == 'u':
        todo1 = int(input("Which index number you want to update: "))
        todo2 = input("enter updated item : ")
        li[todo1 - 1]= todo2
        print(li)

        choice1 = input("If you want to update another item press u: ")
        if choice1 == 'u':
            flag1 = True
        else:
            flag1 = False
            print(li)
    else:
        flag1 = False


flag2 = True

while flag2:
    choice_del = input("Enter d to delete item from list: ")
    if choice_del == 'd':
        todo3 = int(input("which index you want to delete: "))
        del li[todo3 - 1]
        print(li)

        choice2 = input("if you want to delete any other item press D: ")
        if choice2 == 'd':
            flag2 = True
        else:
            flag2 = False
            print(li)
    else:
        flag2 = False

choice3 = input("if you want to add item in list press Y: ")
if choice3 == 'y':
    add()
else:
    flag2 = False
    print(f"Your final list is {li}")







