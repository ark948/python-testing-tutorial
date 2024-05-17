from random import randint

def speed():
    return randint(40, 120)

def alert():
    # if speed is too slow or too fast, make an alert (return true)
    s = speed()
    if s < 60 or s > 100:
        return True
    return False