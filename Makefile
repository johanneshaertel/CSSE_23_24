# Run this suing "make pysetup" to (re)install the environment for the project. 
# This is using conda and installs the dependencies from the evironment.yml file.

# In VS Code, after running, select the intepreter searching 
# for ">Python: Select Interpreter" and select the one with the 
# name of the environment you created.
# For me this was: ~\minconda3\envs\CSSE_23_24\bin\python
pysetup:
	-conda remove -n CSSE_23_24 --all
	-conda env create -f environment.yml

# Rune "make clone_subject" to clone our subject repo.
clone_subject:
	-git clone git@github.com:jwtk/jjwt.git temp/jjwt