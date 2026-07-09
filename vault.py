

class Vault:
    def __init__(self):
        self.accounts = []

    def add_account(self):
        website = input("Enter the website name: ")
        username = input("Enter the username: ")
        password = input("Enter the password")

        account = {
            "website":website,
            "username":username,
            "password":password
        }

        self.accounts.append(account)

    def show_accounts(self):
        if not self.accounts:
            print("No accounts saved.")
            return
        for index, account in enumerate(self.accounts, start=1):
            print(f"\nAccount: {index}")
            print(f"Website: {account['website']}")
            print(f"username: {account['username']}")
            print(f"Password: {account['password']}")

    def delete_account(self):
        self.show_accounts()
        if not self.accounts:
            return
        try:
            choice = int(input("Enter the account number to delete"))
            index = choice - 1
            if 0 <= index < len(self.accounts):
                self.accounts.pop(index)
                print("Account deleted successfully")
            else:
                print("Invalid account number")

    
        except ValueError:
            print("Please Enter a valid number")

       

    def search_account(self):
        search = input("Enter the website or username: ").lower()
        found = False

        for account in self.accounts:
            if search in account["website"].lower() or search in account["username"]:
                print("\n--Account Found")
                print(f"Website: {account['website']}")
                print(f"Username: {account['username']}")
                print(f"Password: {account['password']}")
                found = True

        if not found:
            print("No matching accounts found")
            

    def edit_account(self):
        user = input("Enter the website or username: ").lower()
        found = False
        

        for account in self.accounts:
            if account["username"].lower() == user or account["website"].lower() == user:
                print("----Account found----")
                print(f"Website: {account['website']}")
                print(f"Username: {account['username']}")
                print(f"Password: {account['password']}")

                found = True
                print("\nchoose the option to edit")
                print("1.website")
                print("2.username")
                print("3.password")

                choice = input("Enter the choice: ")

                if choice == "1":
                    new_website_edited = input("Enter the new website: ")
                    account["website"] = new_website_edited
                    print("Website changed succesfully")

                elif choice == "2":
                    account["username"] = input("Enter the new username: ")
                    print("Username changed successfully")

                elif choice == "3":
                    account["password"] = input("Enter the new password: ")
                    print("Password Changed successfully")

                else:
                    print("Invalid option")
                return
            
                if not found:
                    print("Accout Not Found")

def main():
    print("VaultX")
    print("Welcome user to VaultX")

    my_vault = Vault()

    while True:
        print("\n---VaultX Menu===")
        print("1.Add Account")
        print("2.Show All Accounts")
        print("3.Search Account")
        print("4.Edit Account")
        print("5.Delete Account")
        print("6.Exit")

        choice = input("Enter the choice (1-6): ")

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
            print("Thank you for using VaultX . Goodbye!")
            break
        
        else:
            print("INVALID CHOICE pls try again.")

        
if __name__ == "__main__":
    main()
            


    


