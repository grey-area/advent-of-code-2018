from machine import Machine

machine = Machine()
#while True:
#    halt = machine.step()
#    if halt is not None:
#        break

while True:
    machine.step()
    if machine.registers[machine.ip_register] == 28:
        print(machine.registers[2])
        break
