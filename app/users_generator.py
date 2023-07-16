from faker import Faker

def generate_users(amount=100):
    faker = Faker()

    for i in range(amount):
        fake_name = faker.first_name()
        fake_email = faker.email()
        yield f'{i+1} {fake_name} {fake_email}'

def show_users(users=generate_users())->str:
    print('Ex #4')
    for user in users:
        print(f'{user}')

show_users()