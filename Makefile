.PHONY: test

dist: phrases_case
	poetry build

phrases_case: src
	rm -rf phrases_case
	mkdir phrases_case
	cp -r src/* phrases_case/
	3to2 -nw phrases_case -x printfunction -x print

test: phrases_case
	tox
