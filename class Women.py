user_groups = [
    [
        {'name': 'tom', 'age': 21},
        {'name': 'tim', 'age': 69},
        {'name': 'Donald Trump', 'age': 69}
    ],
    [
        {'name': 'sara', 'age': 5},
        {'name': 'hutao', 'age': 21},
        {'name': 'coolkid420', 'age': 420}
    ]
]

user_name = [user['name'] for group in user_groups for user in group if user['age'] > 10]
print(user_name)