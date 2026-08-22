class Vault:
    def __init__(self):
        self.accounts = []

    def add_account(self):
        print("\n--- Add Account ---")

        website = input("Enter the website name: ").strip()
        username = input("Enter the username: ").strip()
        password = input("Enter the password: ").strip()

        if not website or not username or not password:
            print("Website, username, and password cannot be empty.")
            return

        account = {
            "website": website,
            "username": username,
            "password": password
        }

        self.accounts.append(account)
        print("Account added successfully.")

    def show_accounts(self):
        if not self.accounts:
            print("No accounts saved.")
            return

        for index, account in enumerate(self.accounts, start=1):
            print(f"\nAccount: {index}")
            print(f"Website: {account['website']}")
            print(f"Username: {account['username']}")
            print(f"Password: {account['password']}")

    def delete_account(self):
        if not self.accounts:
            print("No accounts saved.")
            return

        self.show_accounts()

        try:
            choice = int(input("\nEnter the account number to delete: "))
            index = choice - 1

            if 0 <= index < len(self.accounts):
                self.accounts.pop(index)
                print("Account deleted successfully.")
            else:
                print("Invalid account number.")

        except ValueError:
            print("Please enter a valid number.")

    def search_account(self):
        if not self.accounts:
            print("No accounts saved.")
            return

        search = input(
            "Enter the website or username: "
        ).strip().lower()

        found = False

        for account in self.accounts:
            if (
                search in account["website"].lower()
                or search in account["username"].lower()
            ):
                print("\n--- Account Found ---")
                print(f"Website: {account['website']}")
                print(f"Username: {account['username']}")
                print(f"Password: {account['password']}")

                found = True

        if not found:
            print("No matching accounts found.")

    def edit_account(self):
        if not self.accounts:
            print("No accounts saved.")
            return

        user = input(
            "Enter the website or username: "
        ).strip().lower()

        found = False

        for account in self.accounts:

            if (
                account["username"].lower() == user
                or account["website"].lower() == user
            ):
                found = True

                print("\n--- Account Found ---")
                print(f"Website: {account['website']}")
                print(f"Username: {account['username']}")
                print(f"Password: {account['password']}")

                print("\nChoose the option to edit:")
                print("1. Website")
                print("2. Username")
                print("3. Password")

                choice = input("Enter the choice: ").strip()

                if choice == "1":
                    new_website = input(
                        "Enter the new website: "
                    ).strip()

                    if new_website:
                        account["website"] = new_website
                        print("Website changed successfully.")
                    else:
                        print("Website cannot be empty.")

                elif choice == "2":
                    new_username = input(
                        "Enter the new username: "
                    ).strip()

                    if new_username:
                        account["username"] = new_username
                        print("Username changed successfully.")
                    else:
                        print("Username cannot be empty.")

                elif choice == "3":
                    new_password = input(
                        "Enter the new password: "
                    ).strip()

                    if new_password:
                        account["password"] = new_password
                        print("Password changed successfully.")
                    else:
                        print("Password cannot be empty.")

                else:
                    print("Invalid option.")

                return

        if not found:
            print("Account not found.")


def main():
    print("================================")
    print("            VaultX")
    print("================================")
    print("Welcome to VaultX!")

    my_vault = Vault()

    while True:
        print("\n--- VaultX Menu ---")
        print("1. Add Account")
        print("2. Show All Accounts")
        print("3. Search Account")
        print("4. Edit Account")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("\nEnter the choice (1-6): ").strip()

        if choice == "1":
            my_vault.add_account()

        elif choice == "2":
            my_vault.show_accounts()

        elif choice == "3":
            my_vault.search_account()

        elif choice == "4":
            my_vault.edit_account()

        elif choice == "5":
            my_vault.delete_account()

        elif choice == "6":
            print("\nThank you for using VaultX. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
