shopping=["bread","butter","milkpowder"]
#print(len(shopping))
#print(shopping[1])
#for item in shopping:
#   print(item)
#for i in range(len(shopping)):
#    print(shopping[i])
shopping.append("flour")
"""for item in shopping:
   print(item)"""
shopping.insert(0,"oil")
for item in shopping:
   print(item)
print(shopping[:])
print("sorted list ")
print("-----")
shopping.sort()
for item in shopping:
   print(item)
print("reversed list")
print('-----')
shopping.reverse()
for item in shopping:
    print(item)
