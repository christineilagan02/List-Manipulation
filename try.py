print("\n\t\33[3m\33[1m          This is the list: \33[0m")
list1 = [1, 9, 2, 12, 26, 17, 83, 8, 15, 79]
print("\t" + str(list1) + "\n")
place = int(input("\n\t\33[92m   Enter a number you want to replace\33[0m \n\t    >> "))
value = int(input('\n\t\33[92m   Enter a number you want to insert\33[0m \n\t    >> '))
list1.insert(place, value)
print("\t" + str(list1) + "\n")