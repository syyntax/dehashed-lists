# Dehashed-Lists
Generate user and password lists based off Dehashed JSON exports.
## Description
**dehashed-lists** is a Python script used to parse through Dehashed JSON files to build user and password wordlists. The lists can then be used in dictionary attacks using publicly accessible password dumps.
## Download
```git clone https://github.com/syyntax/dehashed-lists.git```
# Command Usage
```python3 main.py --file <FILE>```
## Options
| Option          | Description                                  |
|-----------------|----------------------------------------------|
| --file, -f FILE | Import the JSON file as FILE.                |
| --email, -e | Consider email addresses as valid usernames. |
| --help | Show the help information.                   |
## Sample Usage
###### Generate wordlists from example.json
```python3 /opt/dehashed-lists/main.py --file example.json```
###### Generate wordlists from example.json that include email addresses as usernames
```python3 /opt/dehashed-lists/main.py --file example.json --email```
## Output
The application will create three files. These three files will contain _unique_ entries (no duplicates):
* userpass.lst
* users.lst
* pass.lst