@echo off
:: This scripts uses the _find_virtial_env.py script to find and
:: allow the user tho choose a virtual envirionment. 
:: This script then simply takes the result and runs the activation 
:: of the environment.

:: Yes, using a for-loop seems to be the only way to save the output
:: of another program into a variable. Unless you want to write to a tmp file
:: and then read it back. The weird variable name is to minimize risk of
:: overriding an existing name. 
FOR /F "tokens=*" %%F IN ('_find_virtual_env.py %*') DO (
    SET __choosen_virtual_env__=%%F
)

:: This checks jumps the program to the end if the output of the python
:: script was empty
if [%__choosen_virtual_env__%]==[] GOTO EXIT 

:: I tried using setlocal and endlocal for using local variables.
:: However, this stops the call command from actually working.
:: Probably caused by the fact that acticating a new virtual environment
:: includes setting environment variables. Then the local scope created here
:: probably is still in affect and when we leave it the environment is deactivate
:: by having the environment variables deleted. 
call %__choosen_virtual_env__%

:: This is just a label to use with the GOTO command, so we can 
:: skip the call command.
:EXIT
:: Here we unset the variable, because we do not want
:: it in our global state
SET __choosen_virtual_env__=