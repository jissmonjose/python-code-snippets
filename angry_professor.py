count = 0


def angry_prof(k, n):
    global count
    for each in k:
        if each >= 0:
            count += 1
    if count > n:
        return 'no'.upper()
    return 'yes'.upper()


test_case = 0
while test_case < 2:
    att = int(input("No .of Students: "))
    k = list()
    while len(k) < att:
        val = int(input('Enter each attendee: '))
        k.append(val)
    n = int(input('Cancellation threshold: '))
    test_case += 1
    print(angry_prof(k, n))

# No .of Students: 4
# Enter each attendee: -1
# Enter each attendee: -3
# Enter each attendee: 4
# Enter each attendee: 2
# Cancellation threshold: 3
# YES

# No .of Students: 4
# Enter each attendee: 0
# Enter each attendee: -1
# Enter each attendee: 2
# Enter each attendee: 1
# Cancellation threshold: 2
# NO
