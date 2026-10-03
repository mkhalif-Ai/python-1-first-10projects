bill = int(input("how much is the bill?"))
friends = 6
each_pays = bill/friends
print(f"bill:${bill}")
print(f"friends:{friends}")
print(f"each pays:${each_pays.__round__(2)}")

