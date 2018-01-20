default: uninstall install

uninstall:clean
	pip uninstall aerolyzer

install:
	python setup.py sdist
	python setup.py install

clean:
	rm -rf aerolyzer.egg-info/
	rm -rf dist/
	rm -f aerolyzer/*.pyc
