import fish

le_fish = fish.Fish("hans", 5)

print(le_fish.to_string())
le_fish.catch()
print(le_fish.to_string())
le_fish.save()
print(le_fish.to_string())