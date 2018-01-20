## Managing environments with Anaconda ##

#To create a new virtual environment use:
conda create -n env_name package1 package2  # creates an environment called env_name and installs listed packages

#When creating an environment you can specify which version of python to use. This is useful for running older programs that require python 2 for example. For example:
conda create -n py2 python=2

#note: this will install the most recent version of python 2. To install a specific version, use:
conda create -n py2.x python=2.x    # creates an environment that uses python version 2.x

#Entering the new environment.
#To start working in your newly-created environment enter the following:
source activate my_env  # will enter the created environment my_env

#To leave the environment:
source deactivate   # leaves the current working virtual environment

#You can also save environments or load saved environments as YAML files. This is useful for sharing projects so that people can load the environment (with all the packages and there set versions) to ensure your code will work well on their machine. 
#To save an environment:
conda env export > environment.yaml     # exports the current environment to the file name environment.yaml

#To open an environment file:
conda env create -f environment.yaml    # opens the environment environment.yaml (note: -f is for 'file')

#To see a list of your saved environments:
conda env list      # prints out a list of the saved/named environments

#You can delete environments you no linger use as follows:
conda env remove -n env_name    # will remove the environment named env_name

#Note: it is good practise to export the environment as an .yaml file and include it with the project files if you are putting them on github. That way people can install the environment and it will include all required packages etc to make the program run properly.