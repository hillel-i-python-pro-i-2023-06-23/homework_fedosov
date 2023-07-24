from faker import Faker

def generate_users(amount=100):
    faker = Faker()

    for i in range(amount):
        fake_name = faker.first_name()
        fake_email = faker.email()
        yield f'{i+1} {fake_name} {fake_email}'

def show_users(users=generate_users()):
    users_list = []
    for user in users:
        users_formatted = f"<li>{user}</li>"
        users_list.append(users_formatted)
    results = "".join(users_list)
    return results


