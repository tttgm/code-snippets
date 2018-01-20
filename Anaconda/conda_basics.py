## Using Anaconda - Basic Commands ##

#To install packages simply enter the following into the terminal:
conda install package_name1 package_name2   # this installs the packages package_name1 and package_name2

#For example, to install the package NumPy would be:
conda install numpy

#You can also specify the version of the package as follows:
conda install package_name=1.7  # installs version 1.7 of package_name

#Note: conda automatically installs package dependencies, e.g. if you install scipy it will automatically install numpy

#To uninstall use:
conda remove package_name   # removes package_name

#To update a package:
conda upgrade package_name  # updates the package package_name

#To update all packages in a given environment:
conda upgrade --all      # updates all packages in that environment

#And to view packages:
conda list      # prints a list of available packages

#If you're unsure of the exact package name you can search for it using:
conda search search_term    # will print a list of relevant pages related to search_term