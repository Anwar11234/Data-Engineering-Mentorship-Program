from collections import deque

def predictPartyVictory(senate):
    rad, dir = deque(), deque()

    for i in range(len(senate)):
        if senate[i] == 'R':
            rad.append(i)
        else:
            dir.append(i)

    while rad and dir:
        r, d = rad.popleft(), dir.popleft()

        if r < d:
            rad.append(r + len(senate))
        else:
            dir.append(d + len(senate))

    return "Radiant" if rad else "Dire" 