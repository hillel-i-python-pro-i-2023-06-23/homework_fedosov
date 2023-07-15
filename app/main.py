import os
from faker import Faker


def show_greeting() -> [str]:
    fake = Faker()
    name = fake.name()
    address = fake.address()

    print(f"Hello, my name is {name}!\nI live in {address}\n")


def show_current_directory() -> [str]:
    current_directory = os.getcwd()
    print(f"We work in {current_directory} :)")


def main():
    show_greeting()
    show_current_directory()
