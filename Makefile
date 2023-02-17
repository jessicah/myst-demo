
all:
	rm -r _build
	sphinx-build -M html . _build

test:
	python3 ./test.py
