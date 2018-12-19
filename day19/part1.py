from machine import Machine

machine = Machine()
while True:
    halt = machine.step()
    if halt is not None:
        break

print(machine.registers[0])
