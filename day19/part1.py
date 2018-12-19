from machine import Machine

machine = Machine()
i = 0
while True:
    i += 1
    if i % 10000 == 0:
        print(i/1000, machine.registers[0])

    halt = machine.step()
    if halt is not None:
        break

print(machine.registers[0])
