from machine import Machine, load_data

machine = Machine()

data = load_data()

for line in data:
    print(line)
