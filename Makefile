all:
	platex main
	pbibtex main
	platex main
	platex main
	dvipdfmx main

clean:
	ls | grep main | grep -v tex | xargs rm
