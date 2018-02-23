### Interacting with the os from within IPython ###
'''
These are some examples of 'magic functions' that go straight to the base shell (i.e. terminal) to execute
when called from within the IPython (or Jupyter Notebook) environment.
'''

!cmd    # execute cmd in the system shell
output = !cmd args      # run cmd and store the stdout in 'output'
%alias alias_name cmd   # define an alias for a system (shell) command
%bookmark       # utilize IPython's directory bookmarking system
%cd directory   # change system working directory to passed directory
%pwd        # print the current working directory
%pushd directory   # place current directory on stack and change to target directory
%popd       # change to directory popped off the top of the stack
%dirs       # return a list containing the current directory stack
%dhist      # print the history of visited directories
%env        # return the sys environment variables as a dict


# Example usage of built-in 'bookmarking' system

# set a dir as a 'bookmark' and give it a name
%bookmark some_name /home/tom/Documents/

# can then easily access that dir via the given name
# e.g.
cd some_name
(bookmark: some_name) -> /home/tom/Documents/
/home/tom/Documents/    # are now in the directory
