# By inspecting the execution of the program and jumping to the end of loops:
# The inner loop progresses until register register 1 is a factor of 10551305.
# That factor is then added to register 0.
# The result is that register 0 contains the sum of the factors of 10551305.

N = 10551305

print(sum([i for i in range(1, N + 1, 1) if N % i == 0]))
