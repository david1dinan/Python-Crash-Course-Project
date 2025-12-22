current_users = ['alex', 'morgan', 'casey' 'taylor', 'jordan']
new_users = ['alex', 'morgan', 'evan', 'lynn', 'emmy']

for user in new_users:
    if user in current_users:
        print(f"That username is not available.")
    else:
        print(f"Adding {user.title()} to the list.")


