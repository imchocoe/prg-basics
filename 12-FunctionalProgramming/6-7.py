

# Ratings of the four players
ratings = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]

# Calculate the total score for each player
total_scores = list(map(lambda rating: sum(rating) - min(rating) - max(rating), ratings))

print(total_scores)
