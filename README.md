# cs329e-collatz

Project 1 files
---------------
Note about the following rule in the makefile.

Collatz.log:
	git log > Collatz.log
	
After first execution "make collatz.log", the file "collatz.log" will be created. 
However, you must note that the rule "collatz.log" does not have any dependencies (or prerequisite) and the file is already created.
Since it has no prerequisites, "collatz.log" would always be considered up to date and its recipe would not be executed. To avoid this problem you can 
explicitly declare the target to be phony by making it a prerequisite of the special target .PHONY as follows:

.PHONY: Collatz.log

Once this is done, "make collatz.log" will run the recipe regardless of whether there is a file named "collatz.log".


Note you need to upgrade the dependencies in rquirements.txt
pip install -r requirements-to-freeze.txt --upgrade
pip freeze > requirements.txt