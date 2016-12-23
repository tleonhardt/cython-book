all:
	gcc -g -O2 -fpic -c AddFunction.c -o AddFunction.o
	python setup.py build_ext --inplace

clean:
	rm -f PyAddFunction.c *.o *.so
