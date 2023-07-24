from cryptography.fernet import Fernet
import json

with open('key.txt', 'rb') as key:
    KEY = key.read()

with open('passwords.json', 'rb') as file:
    data = json.loads(Fernet(KEY).decrypt(file.read()))


def master_login():
    passwd = input("Enter Master Password: ")
    for _ in range(2):
        if passwd == data['master_pass']:
            return True
        else:
            passwd = input("Incorrect Password, Try again: ")
    print("Terminated! Too many incorrect attempts.")
    return False


def list_all():
    for id_ in data:
        if id_ != 'master_pass':
            print("\nAccount Name:", data[id_]['account'])
            print("Password:", data[id_]['passwd'])


def new_entry():
    account = input("Enter account name: ")
    passwd = input("Enter password: ")
    data[str(len(data))] = {'account': account, 'passwd': passwd}
    with open('passwords.json', 'wb') as file:
        file.write(Fernet(KEY).encrypt(json.dumps(data).encode('utf-8')))


def view():
    account = input("Enter account name: ")
    for id_ in data:
        if id_ != 'master_pass':
            if data[id_]['account'] == account:
                print("\nAccount Name:", data[id_]['account'])
                print("Password:", data[id_]['passwd'])
                break
    else:
        print("\nAccount does not exist.")


if __name__ == '__main__':
    if master_login():
        functions = {'1': new_entry, '2': view, '3': list_all}
        choice = input("Enter one of the following options to continue:\n1. Add a new entry\n2. View password of an account\n3. Print all accounts and associated passwords\n\nChoice: ")
        while choice not in ['1', '2', '3']:
            choice = input("Enter one of the following options to continue:\n1. Add a new entry\n2. View password of an account\n3. Print all accounts and associated passwords\n\nChoice: ")
        functions[choice]()
