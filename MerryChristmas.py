def max_activities(X):
    activities = [1, 2, 4]
    activities.sort()
    count = 0
    for time in activities:
        if X >= time:
            X -= time
            count += 1
        else:
            break
    return count

X = int(input().strip())
print(max_activities(X))
