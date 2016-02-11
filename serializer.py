# encoding: utf-8


def serialize(filename, commands):
    with open(filename, "w") as file:
        print(len(commands), file=file)
        print('\n'.join(' '.join(str(entry) for entry in command) for command in commands), file=file)
