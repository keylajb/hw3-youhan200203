ENV_NAME = ligo

.PHONY: env html clean
env:
	conda env create -f environment.yml --name $(ENV_NAME) || \
	conda env update --f environment.yml --name $(ENV_NAME)

html:
	myst build --html

clean:
	rm -rf _build/*
	rm -rf figures/*
	rm -rf audio/*