from machine import Machine

#machine = Machine(registers=[1, 0, 0, 0, 0, 0])
#machine = Machine(ip=4, registers=[0, 1, 10551305, 4, 10551305, 10551305])
#machine = Machine(ip=9, registers=[1, 2, 10551305, 9, 10551306, 0])
#machine = Machine(ip=9, registers=[1, 3, 10551305, 9, 10551306, 0])
#machine = Machine(ip=9, registers=[1, 4, 10551305, 9, 10551306, 0])
#machine = Machine(ip=4, registers=[1, 5, 10551305, 4, 2110261, 10551305])
#machine = Machine(ip=9, registers=[6, 5, 10551305, 9, 10551306, 52756530])
#machine = Machine(ip=9, registers=[6, 6, 10551305, 9, 10551306, 0])
# ...
#machine = Machine(ip=9, registers=[6, 16, 10551305, 9, 10551306, 0])
#machine = Machine(ip=4, registers=[6, 17, 10551305, 4, 620665, 10551305])
#machine = Machine(ip=9, registers=[23, 17, 10551305, 9, 10551306, 179372202])
#machine = Machine(ip=9, registers=[23, 18, 10551305, 9, 10551306, 0])
# ...
#machine = Machine(ip=9, registers=[23, 124131, 10551305, 9, 10551306, 0])
#machine = Machine(ip=9, registers=[23, 124132, 10551305, 9, 10551306, 0])
#machine = Machine(ip=4, registers=[23, 124133, 10551305, 4, 85, 10551305])
#machine = Machine(ip=9, registers=[124156, 124133, 10551305, 9, 10551306, 111330068856942])
#machine = Machine(ip=9, registers=[124156, 124134, 10551305, 9, 10551306, 0])
# ... ?
machine = Machine(ip=9, registers=[124156, 10551304, 10551305, 9, 10551305, 0])
#machine = Machine(ip=4, registers=[124156, 10551305, 10551305, 4, 1, 10551305])
#machine = Machine(ip=9, registers=[10675461, 10551305, 10551305, 9, 10551306, 111330068856942])


i = 0

while True:
    if i > 150:
        break
    i += 1
    toprint = False
    toprint = True
    halt = machine.step(toprint)
    if i % 15 == 0:
        print()
    if halt is not None:
        break

print(machine.registers[0])
