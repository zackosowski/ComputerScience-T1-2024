import random

prefix = ["cool", "wild", "super", "incredible"]
suffix = ["thing", "sword", "axe", "shield", "bow"]
def drop_item():
    global prefix, suffix

    p = random.randint(0,3)
    s = random.randint(0,3)
    print(prefix[p] + " " + suffix[s])
    if input("Another drop?\n>") == "y":
        drop_item()

drop_item()