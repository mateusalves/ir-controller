#makefile
C_COMPILER=gcc

# TARGET_EXTENSION=.so

BINDIR=bin/
EXTDIR=ext/
SRCDIR=src/

FLAGS = -Wall
FLAGS += -I$(EXTDIR)

LIBS = -lpigpio
LIBS += -lm #liking to libmath
LIBS += -pthread

all: clean bindir ir_controller

ir_controller:
	$(C_COMPILER) $(FLAGS) $(SRCDIR)* -o $(BINDIR)ir_functions$(TARGET_EXTENSION) $(LIBS)

bindir:
	@mkdir $(BINDIR)

clean:
	@rm -rf $(BINDIR)
