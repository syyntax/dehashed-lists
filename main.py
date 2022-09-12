import argparse
from json import loads

parser = argparse.ArgumentParser(description="Create a user and password list using results from Dehashed.")
parser.add_argument("--file", action="store", help="Import JSON from file.", type=str, dest="infile", default=None,
                    metavar="FILE")
parser.add_argument("--output", action="store", help="Output to FILE.", type=str, dest="outfile", default="users.lst",
                    metavar="FILE")

args = parser.parse_args()


def get_data(json):
    return loads(open(json, 'r').read())


def get_users(data):
    for i in data['entries']:
        with open('users.lst', 'a') as f:
            f.write(f"{i['email']}\n")


def get_passwords(data):
    for i in data['entries']:
        with open('pass.lst', 'a') as f:
            f.write(f"{i['password']}\n")


def get_userpass(data):
    for i in data['entries']:
        if len(i['password']) > 0:
            with open('userpass.lst', 'a') as f:
                f.write(f"{i['email']}:{i['password']}\n")


a = get_data(args.infile)
get_users(a)
get_passwords(a)
get_userpass(a)
