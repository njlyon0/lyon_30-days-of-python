"""
Virtual Environments

Virtual environents help create siloed spaces for discrete projects. This makes identifying dependencies unique to a particular project (rather than all packages ever installed on your computer) much simpler. 
"""

# You can use the "virtualenv" package for this
## Installed via command line as follows:
## `python3 -m pip install virtualenv`

# Virtual environments can then be instantiated with the following comand line syntax
## `virtualenv VIRTUALENVIRONMENTNAME`

# Once created, they can be activated like so:
## `source VIRTUALENVIRONMENTNAME/bin/activate`

# From here on out, your command line lines should start with "(venv)" instead of "(base)" (or nothing)

# When finished working, it is good practice to then deactivate the virtual environment
## `deactivate`
