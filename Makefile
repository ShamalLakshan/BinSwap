CC = g++
CCFLAGS = -g -Wall -Wextra
PROGRAM = beta-cpp-implementation

beta-cpp-implementation: beta-cpp-implementation.cpp
	$(CC) $(CCFLAGS) $(PROGRAM).cpp -o $(PROGRAM)

clean:
	$(PROGRAM)