from sys import argv

// while running program, python keyword is missed, hence argv is 2
if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("Hello, world")