#!/usr/bin/python
# encoding: utf-8
import distutils.spawn
import os
import logging
import wget
from os import environ
from os.path import expanduser
import platform
import zipfile


def check_envrionment():

    C_program_folder = os.environ['PROGRAMFILES']
    Path = os.getenv('Path')

    #=====================================================================================
    #                                     JAVA
    #java.exe
    # C:\Program Files\Java\jre1.8.0_241
    # C:\Program Files (x86)\Java\jre1.8.0_241
    #=====================================================================================
    #JAVA_HOME = C:\Program Files\Java\jre1.8.0_241
    #--- To know the path of java version folder and java.exe, we need to search for another file. I.E: javacpl.exe
    javacpl_folder= distutils.spawn.find_executable('javacpl.exe')
    #--- By this way, we can rebuild the path to java.exe
    java_exe_path = javacpl_folder.replace("javacpl.exe","java.exe")
    #--- and so check if java.exe is present in "C:\Program Files\Java\jrexxxxxxxx\bin"
    print(str(os.environ))
    JAVA_HOME_VALUE = java_exe_path.replace("\\bin\java.exe", "")
    if os.path.isfile(java_exe_path):
        print(f"We found java.exe in folder {java_exe_path}. Let's check now the environment variable!")

        if "JAVA_HOME" in os.environ:

            print("We found JAVA_HOME exists.")
            print(f"Value of JAVA_HOME is " + str(os.getenv('JAVA_HOME')))
            java=True
        else:
            print(f"JAVA_HOME_VALUE = {JAVA_HOME_VALUE}")
            print(f"Environment variable JAVA_HOME doesn't exist. We will create it and add the value {JAVA_HOME_VALUE}")
            #--- We prepare the value of command for adding vlaue in environment variable
            os_command = 'setx JAVA_HOME "' + JAVA_HOME_VALUE + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)
            java = True
        #--- Now we add the Java path in environment variable 'Path'
        if JAVA_HOME_VALUE in Path:
            print(f"Perfect! JAVA_HOME is in {Path} ")
            java=True
        else:
            Path = os.getenv('Path') + ';' + JAVA_HOME_VALUE
            os_command = 'setx Path "' + Path + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)




    else:
        print("We didn't find java.exe. You will have to install it.")
        java= False

    #=====================================================================================
    #                                NODE.js
    #node.exe
    # C:\Program Files\nodejs
    # C:\Program Files (x86)\nodejs
    #=====================================================================================
    #--- To know the path of adb.exe folder
    node_file= distutils.spawn.find_executable('node.exe')
    node_folder = node_file.replace("node.exe","")
    print(f"node_folder : {node_folder}")

    if os.path.isfile(node_file):
        print(f"We found node.exe in folder {node_folder}. Let's check now the environment variable!")

        if node_folder in os.environ:

            print(f"We found '{node_folder}' exists in environment variable Path.")
            print(f"Value of Path is " + str(os.getenv('Path')))
            node=True
        else:
            #--- We rebuild the path of ANdroid in order to add it in Environment Variable
            Path = os.getenv('Path') + ';' + node_folder
            os_command = 'setx Path "' + Path + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)
            node = True
    else:
        print("We didn't find node.exe. You will have to install it.")
        node= False

    #=====================================================================================
    #                                ANDROID (adb.exe)
    #=====================================================================================

    #--- To know the path of adb.exe folder
    adb_folder= distutils.spawn.find_executable('adb.exe')
    print(f"adb_folder : {adb_folder}")
    pos_ANDROID_HOME_VALUE = adb_folder.find('Android', 1)
    ANDROID_HOME_VALUE = adb_folder[0:pos_ANDROID_HOME_VALUE + 7]
    print(f"ANDROID_HOME_VALUE = {ANDROID_HOME_VALUE}")
    if os.path.isfile(adb_folder):
        print(f"We found adb.exe in folder {adb_folder}. Let's check now the environment variable!")

        if "ANDROID_HOME" in os.environ:

            print("We found ANDROID_HOME exists.")
            print(f"Value of ANDROID_HOME is " + str(os.getenv('ANDROID_HOME')))
            android=True
        else:
            #--- We rebuild the path of ANdroid in order to add it in Environment Variable

            print(f"Environment variable ANDROID_HOME doesn't exist. We will create it and add the value {ANDROID_HOME_VALUE}")
            #--- We prepare the value of command for adding vlaue in environment variable
            os_command = 'setx ANDROID_HOME "' + ANDROID_HOME_VALUE + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)
            android = True
        if ANDROID_HOME_VALUE in Path:
            print(f"Perfect! ANDROID_HOME is in {Path} ")
            android=True
        else:
            Path = os.getenv('Path') + ';' + ANDROID_HOME_VALUE
            os_command = 'setx Path "' + Path + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)
    else:
        print("We didn't find adb.exe. You will have to install it.")
        android= False

    #=====================================================================================
    #                                Appium server (appium.cmd)
    #=====================================================================================
    #--- We get the HOME user folder in order to find the path of appium
    #---  which suppose to be in C:\Users\USERNAME\AppData\Roaming\npm
    home_user = expanduser("~")
    print(f"home_user : {home_user}")
    appium_folder = home_user + "\AppData\Roaming\\npm"
    appium_exe = appium_folder + "\\appium.cmd"
    print(f"appium_folder : {appium_folder} - appium_exe {appium_exe}")
    if os.path.isfile(appium_exe):
        print(f"We found appium.cmd in folder {appium_folder}. Let's check now the environment variable!")

        if appium_folder in os.environ:

            print(f"We found {appium_folder} exists in envirnment variable 'Path'.")
            print(f"Value of Path is " + str(os.getenv('Path')))
            appium=True
        else:
            #--- We rebuild the path of ANdroid in order to add it in Environment Variable
            print(f"Path of Appium doesn't exist in environment variable 'Path'. We will create it and add the value {appium_folder}")
            #--- We prepare the value of command for adding vlaue in environment variable
            Path = os.getenv('Path') + ';' + appium_folder
            os_command = 'setx Path "' + Path + '"'
            print(f"os_command :{os_command}")
            os.system(os_command)
            appium = True



    else:
        print("We didn't find appium.cmd. We will try to install it.")
        appium= False


    print("================= REPORT ===================")
    print(f"Is Java Ready? => {java}")
    print(f"Is NodeJS Ready? => {node}")
    print(f"Is Android Tools Ready? => {android}")
    print(f"Is Appium Ready? => {appium}")
    print("=============================================")

    return java,node,android,appium

def install_environment(java,node,android,appium):

    C_program_folder = os.environ['PROGRAMFILES']

    print("We will try to install the missing software and add tne environment variable.")
    print("If something goes wrong, please contact our support at support@programname.co.")

    #=====================================================================================
    #                                INSTALLATION
    #=====================================================================================
    #JAVA => https://javadl.oracle.com/webapps/download/AutoDL?BundleId=241536_1f5b5a70bf22433b84d0e960903adac8
    if java==False:
        try:
            print("We will try now to download Java.")
            wget.download('https://javadl.oracle.com/webapps/download/AutoDL?BundleId=241536_1f5b5a70bf22433b84d0e960903adac8',
                      'java_install.exe')
            print("We will try now to install Java. Follow the installation process.")
            os.system("java_install.exe")
        except:
            print("We tried to download and install Java on your computer, but something went wrong.\n \
                  Please download and install Java manually from https://www.java.com/fr/download/ \
                  Once it is done, re-run programname.exe")

    if node==False:
        try:
            print("We will try now to download NodeJS.")
            if platform.architecture()[0] == "64bit":
                wget.download('https://nodejs.org/dist/v12.15.0/node-v12.15.0-x64.msi','node_install.msi')
                print("We will try now to install NodeJS 64Bits. Please follow the installation process.")
                os.system("node_install.msi")
            else:
                wget.download('https://nodejs.org/dist/v12.15.0/node-v12.15.0-x86.msi', 'node_install.msi')
                print("We will try now to install NodeJS 32Bits. Please follow the installation process.")
                os.system("node_install.msi")
        except:
            print("We tried to download and install NodeJS on your computer, but something went wrong.\n \
                  Please download and install DoneJS manually from https://nodejs.org/en/download/\n \
                  Once it is done, re-run programname.exe")

    if android==False:
        android_tools_folder = C_program_folder + 'Android\\tools'
        try:
            print("We will try now to download Android Tools.")
            wget.download('https://dl.google.com/android/repository/platform-tools-latest-windows.zip','android_tool.zip')
            print("We will try now to install unzip the Android Tools.")
            with zipfile.ZipFile('android_tool.zip', 'r') as zip_ref:
                zip_ref.extractall('android_tools_folder')
        except:
            print(f"We tried to download and unzip Android tools on your computer, but something went wrong.\n \
                  Please download Android tools manually from https://dl.google.com/android/repository/platform-tools-latest-windows.zip\n  \
                  And unzip all the files in {android_tools_folder} \n  \
                  Once it is done, restart programname.exe")


    if appium==False:

        try:
            print("We will try now to install Appium.")
            os.system("npm install -g appium")
        except:
            print("We tried to download and install NodeJS on your computer, but something went wrong.\n \
                  Please download and install DoneJS manually from https://nodejs.org/en/download/\n \
                  Once it is done, re-run programname.exe")

C_program_folder = os.environ['PROGRAMFILES']
java,node,android,appium = check_envrionment()
while java!=True or node!=True or android!=True or appium!=True:
    if java==True and node==True and android==True and appium==True:
        print("Everything seems to be fine. When you will run the programname.exe, please send us the log file to support@programname.co if something goes wrong!")
        break
    else:
        install_environment(java,node,android,appium)
        java, node, android, appium = check_envrionment()
        answer = None
        while answer not in ("y", "n"):
            answer=input("Would you like to try again to install the missing program?(answer => y) or would you prefer to install it yourself manually(answer => n) : ").lower().strip()
            if answer=='y':
                print("Ok. We will try to install again the missing program!")
            elif answer =='n':
                print("Ok. Here is the list of tasks in chronologicall order for installing the software:")
                if java==False:
                    print(f"    - Java is missing. You can download it here: https://www.java.com/download/\n")
                if node==False:
                    print(f"    - NodeJS is missing. You can download it here: https://www.java.com/download/\n")
                if android==False:
                    print(f"    - Android Tools are missing. You can download the zip file here: https://developer.android.com/studio/releases/platform-tools/")
                    print(f"      Then, unzip all these files in {C_program_folder}\Android\\tools folder. If these folder and subfolder doesn't exist, create them.\n")
                if appium==False:
                    print(f"    - Appium is missing. Open the windows 'command' and type this line: 'npm install -g appium' (without the quotes)")
                java, node, android, appium = True,True,True,True
                break
            else:
                print("Please answer 'y' to try again or 'n' to exit the program")


