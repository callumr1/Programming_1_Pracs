def main():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye','swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Please enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()