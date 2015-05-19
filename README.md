# nosetests_extras
Wrapper over nosetests

Nosetests doesn't provide a way to dig through folder structure to find all test*.py files. Hence to address this issue, ladder.py helps return a set of directories which contains test*.py files. This list can be iterated with nosetests in order to run all test*.py files under all children directories.
