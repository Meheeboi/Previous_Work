
def falling_distance(t):
    d = (1 / 2) * 9.8 * (t ** 2)
    print(round(d, 1), 'meters')
    return d

for t in range(1, 11):
    falling_distance(t)