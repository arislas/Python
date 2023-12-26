current_users = ['xto', 'arislas', 'sarcior', 'YOSTON', 'admin']
new_users = ['mono', 'xto', 'querubin', 'Sarcior', 'Admin', 'yoston']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"'{user.title()}', you will need to enter a new username.")
    else:
        print(f"'{user.title()}', this username is available.")