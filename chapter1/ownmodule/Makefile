all:
	gcc -g -O2 -fpic -c AddFunction.c -o AddFunction.o
	cythonize -b PyAddFunction.pyx
	cython -2 PyAddFunction.pyx

clean:
	rm -f PyAddFunction.c *.o *.so
