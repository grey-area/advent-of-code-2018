from machine import Machine

machine = Machine()

while True:
    machine.step()

    if machine.ip == 28:
        print(machine.registers[2])
        break
