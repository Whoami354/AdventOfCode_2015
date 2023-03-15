import itertools

ingredients = {
    'Sprinkles': {'capacity': 5, 'durability': -1, 'flavor': 0, 'texture': 0, 'calories': 5},
    'PeanutButter': {'capacity': -1, 'durability': 3, 'flavor': 0, 'texture': 0, 'calories': 1},
    'Frosting': {'capacity': 0, 'durability': -1, 'flavor': 4, 'texture': 0, 'calories': 6},
    'Sugar': {'capacity': -1, 'durability': 0, 'flavor': 0, 'texture': 2, 'calories': 8}
}

# Alle möglichen Kombinationen von 100 Teelöffeln der Zutaten
combinations = itertools.product(range(101), repeat=len(ingredients))

# Der höchste erreichte Score
max_score = 0

for amounts in combinations:
    if sum(amounts) == 100:  # Wir verwenden genau 100 Telöffel
        # Berechne die Eigenschaften der Keks-Zutaten
        capacity = max(0, sum(amounts[i] * ingredients[z]['capacity'] for i, z in enumerate(ingredients)))
        durability = max(0, sum(amounts[i] * ingredients[z]['durability'] for i, z in enumerate(ingredients)))
        flavor = max(0, sum(amounts[i] * ingredients[z]['flavor'] for i, z in enumerate(ingredients)))
        texture = max(0, sum(amounts[i] * ingredients[z]['texture'] for i, z in enumerate(ingredients)))
        calories = sum(amounts[i] * ingredients[z]['calories'] for i, z in enumerate(ingredients))

        score = capacity * durability * flavor * texture
        if calories == 500:
            max_score = max(max_score, score)


print("Der höchste erzielte Score ist:", max_score)
