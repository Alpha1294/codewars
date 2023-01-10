from collections import Counter

def score(dice):
    counts = Counter(dice)
    score = 0
    for face_value in counts:
        if counts[face_value] >= 3:
            if face_value == 1:
                score += 1000
            elif face_value == 6:
                score += 600
            elif face_value == 5:
                score += 500
            elif face_value == 4:
                score += 400
            elif face_value == 3:
                score += 300
            elif face_value == 2:
                score += 200
        if counts[face_value] >= 1:
            if face_value == 1:
                score += counts[face_value] * 100
            if face_value == 5:
                score += counts[face_value] * 50
    return score


print(score([1, 1, 1, 3, 1]))
