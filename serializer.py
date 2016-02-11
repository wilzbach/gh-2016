def serialize(filename, orders):
    with open(filename, "w") as file:
        print('\n'.join(' '.join(str(entry) for entry in order) for order in orders), file=file)
