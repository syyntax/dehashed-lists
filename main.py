import argparse
from json import loads

parser = argparse.ArgumentParser(description="Create a user and password list using results from Dehashed.")
parser.add_argument("--file", "-f", action="store", help="Import JSON from file.", type=str, dest="infile",
                    default=None, metavar="FILE")
parser.add_argument("--email", "-e", action="store_true", help="Include emails as a valid username option.")

args = parser.parse_args()


def get_data(json):
    return loads(open(json, 'r').read())


def get_users(data):
    lines = set()
    [lines.add(i['email']) for i in data['entries']]
    with open('users.lst', 'a') as f:
        [f.write(f"{line}\n") for line in lines]


def get_passwords(data):
    lines = set()
    [lines.add(i['password']) for i in data['entries'] if not i['password'] == '']
    with open('pass.lst', 'a') as f:
        [f.write(f"{line}\n") for line in lines]


def get_userpass(data):
    lines = set()
    [lines.add(f"{i['username']}:{i['password']}") for i in data['entries'] if not i['password'] == '' and not
        i['username'] == '']
    [lines.add(f"{i['email']}:{i['password']}") for i in data['entries'] if not i['password'] == '' and args.email]
    with open('userpass.lst', 'a') as f:
        [f.write(f"{line}\n") for line in lines]


a = get_data(args.infile)
get_users(a)
get_passwords(a)
get_userpass(a)
