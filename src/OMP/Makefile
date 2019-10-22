CC=cc
ifeq ($(VIS),1)
	INC=-DVIS -I../../include/
endif
OMPFLAGS=-homp
CFLAGS=-DROWS=2046 -DCOLS=2046 $(OMPFLAGS) $(INC)
EXE=../../bin/heat_omp
all: heat_omp

heat_omp: heat_omp.o
	@mkdir -p ../../bin
	$(CC) $(CFLAGS) heat_omp.o -o $(EXE)

heat.o: heat_omp.c
		$(CC) -c -o $@ $< $(CFLAGS)

clean:
		rm *.o $(EXE)
cleanall:
		rm *.o *.out *.vtk $(EXE)
