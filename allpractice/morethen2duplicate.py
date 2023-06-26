votes = {
    "user1": "yes",
    "user2": "no",
    "user3": "yes",
    "user4": "no",
    "user5": "maybe",
    "user6": "yes"}

#vote = OrderedDict()
for key, value in votes.items():
    if value in votes:
        votes[value] += 1
    else:
        votes[value] = 1

