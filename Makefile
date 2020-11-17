.PHONY : all
all: deploy
deploy:
	./package.sh
	sls deploy