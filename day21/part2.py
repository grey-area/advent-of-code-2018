from machine import Machine

machine = Machine()

seen_termination_conditions = set()
last_termination_condition = None

while True:
    # Optimized the inner loop
    if machine.ip == 18:
        machine.registers[3] = machine.registers[5] // 256

    machine.step()

    # Record values of register 0 that would cause us to terminate
    # until we start seeing repeat values
    if machine.ip == 28:
        termination_condition = machine.registers[2]
        if termination_condition in seen_termination_conditions:
            break
        seen_termination_conditions.add(termination_condition)
        last_termination_condition = termination_condition

print(last_termination_condition)
