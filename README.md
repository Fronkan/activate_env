# activate_venv
A set of scripts to find and activate a Python virtual environment (virtualenv) in the local directory, for Windows.


## Install
In the repo is a files _installer.py which can be used to "install" the program. This is a very simple program which just copies the neccary files to the supplied directory. You can use the -h/--help flag for more information. The supplied target directory must be added to your path manually so you can access it from your terminal. This tool was built around my set up, but I hope it will work for you as well. In my set up I have .py files open with the python interpreter as the default program and also added .py to the PATHEXT environment variable. This setup is further described in these blog posts:
* [Making your CLI-tools accessible in Windows](https://dev.to/fronkan/making-your-cli-tools-accessible-in-windows-4b18)
* [Settings for Making Python CLI-tools on Windows](https://dev.to/fronkan/settings-for-making-python-cli-tools-on-windows-3phb)


## Running the tool
When installed correctly you can run e.g. the activate_env.bat file to activate a virtual_env environment in your current directory. Using the -r flag also allow for recursive search through your current working directory. If multiple environments where found it will allow you to pick the one you want to activate.
