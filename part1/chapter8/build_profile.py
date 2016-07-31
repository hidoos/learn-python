def build_profile(first, last, **user_info):
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_info = build_profile('hidoos', 'lan', age = 25, job = 'developer', goal = 'full stack engineer')
print("\nprinting user info")
print(user_info)