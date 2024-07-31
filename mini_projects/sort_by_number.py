#sort by number
ids =["id1","id22","id11","id11","id6"]
def ids1(ids2):
    return int(ids2[2:])
ids.sort(key=ids1)
print(ids)