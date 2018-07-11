all: open

create:
	platex main
	dvipdfmx main

open: create
	evince main.pdf

clean:
	ls | grep main | grep -v tex | xargs rm
