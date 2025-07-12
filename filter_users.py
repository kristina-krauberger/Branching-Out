import json


def filter_users_by_name(name):
    """Filter users from the JSON file by name (case-insensitive) and print the results."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)

    if not filtered_users:
        print(f"No user found with name '{name}'.")


def filter_users_by_age(age):
    """Filter users from the JSON file by age and print the results."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]
    for user in filtered_users:
        print(user)

    if not filtered_users:
        print(f"No user found with age '{age}'.")


def filter_users_by_email(email):
    """Filter users from the JSON file by email (case-insensitive) and print the results."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    for user in filtered_users:
        print(user)

    if not filtered_users:
        print(f"No user found with email '{email}'.")


def main():
    """Prompt user for a filter option and perform filtering accordingly."""
    filter_option = input("What would you like to filter by? Choose from <Name> / <Age> / <Email>: ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter age to filter user: "))
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter email to filter user: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.") #Change validation


if __name__ == "__main__":
    main()