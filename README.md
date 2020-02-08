# prepare_envir_appium.py
This script will check and install the necessary software required by appium.
Appium need several software to be installed on your machine.
THis script is for Python newbie who would like to start quickly to work on Appium.
Appium require different softwares to be installed and it need some environment variable.

For the moment, the script work only in Windows 32/64. It needs improvement. Any people who likes this project is welcome to contribute to imporve the code.

# How it works?
The script has 2 functions:
  1. check_envrionment(): It checks if softwares are installed on the computer and if environment variables are added.
  2. install_environment(java,node,android,appium): It download the necessary program and launch the installation from command line. User will have to follow the steps of installation process if necessary.
  
 After these 2 functions has been proceed, there is a loop 'while' asking to user if he/she wants to start again a checking/installing in case something went wrong.
 
Any suggestion or imporvement is welcome! It is a public free script for anyone who loves python and appium.

# Final goal of this script
If some contributors could join the project to make work the script on any machine (Windwos, IOS, Linux). 
The final purpose of the script is to check that the environment is perfecty configured before to run Appium.

Feel free to contact me on Telegram if you have any question @gauthierbuttez


