def add_bonus(scores, bonus):
    """Add bonus to every score in place (max 100). Returns nothing."""
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)


def with_bonus(scores, bonus):
    """Return a new list with bonus added (max 100); original is unchanged."""
    new_scores = []
    for score in scores:
        new_scores.append(min(score + bonus, 100))
    return new_scores


scores = [70, 95, 88, 100]
print(with_bonus(scores, 10))
print(scores)
add_bonus(scores[:], 10)
print(scores)
add_bonus(scores, 10)
print(scores)
