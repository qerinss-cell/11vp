users = ['Admin', 'Guest', 'User', 'Bot']

users[2] = 'Moderator'
users[-1] = 'SuperAdmin'

Newbie = ["Newbie"]
users = users + Newbie

print(*users, sep=",")
