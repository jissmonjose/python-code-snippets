min = 0
max = 0

minimum = 0
maximum = 0
scores = []
i = 0


# [12,24,10,24]
def breakingRecords(scores):
    # i = 0
    global min, max, minimum, maximum, i
    for each in scores:
        if minimum == maximum and i == 0:
            minimum = each
            maximum = each
            i += 1

        elif each >= maximum:
            maximum = each
            max += 1
            # print(max)
        elif each <= minimum:
            minimum = each
            min += 1
            # print(min)
    return max, min


score = int(input('Enter Score: '))

scores.append(score)
while len(scores) < len(range(4)):
    score = int(input('Enter Score: '))
    scores.append(score)

print(breakingRecords(scores))

# Output:
# Enter Score: >? 12
# Enter Score: >? 24
# Enter Score: >? 10
# Enter Score: >? 24
# (2, 1)
