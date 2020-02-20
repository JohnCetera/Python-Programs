lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "oscar", "Toby"]

friends.sort()
friends.append("Creed")
friends.insert(2, "Kelly")
friends.remove("oscar")
lucky_numbers.reverse()
friends.extend(lucky_numbers)
friends.pop()

friends2 = friends.copy()
print(friends.index("Karen"))
print(friends.count("Jim"))
print(friends)
print(friends)
