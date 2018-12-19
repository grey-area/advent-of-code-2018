from machine import Machine

# Disclaimer: This is an additional solution after coming to the answer
# more or less manually. I got the idea for optimizing the program from elsewhere,
# but did the optimizing myself

m = Machine(registers=[1, 0, 0, 0, 0, 0])

while True:
    if m.ip == 3:
        a, b, c, d, e, f = m.registers
        if b * e <= c and c % b == 0:
            m.registers[0] += b
            m.registers[4] = c // b
        m.ip = 10
        m.registers[4] = c + 1
        m.registers[5] = 1

    halt = m.step()
    if halt is not None:
        break

print(m.registers[0])
