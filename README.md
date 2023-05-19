# Mastan 3 - Source Code Repository

**Important Note: Confidential and ONLY accessed by team members**

## Project Leaders:
R.D. Ziemian - Bucknell University, the United States  
S.W. Liu - The Hong Kong Polytechnic University, Hong Kong, China


   
## Team Members: 
Liang Chen, Wenlong Gao, Guanhua Li, Weihang Ouyang and Haoyi Zhang    
      

---
## Style Guide for Developers
Please follow the "PEP 8 – Style Guide for Python Code"       
https://peps.python.org/pep-0008/       

In principle, the variables, class and function names should be concise, short and clear to read. Necessary comments should be provided. 

It is collaborative work!       

No duplicated codes!

---
## Latest Updates
- 2023-01-07:
    - New cross-section analysis module MSASECT2 version 1.1.0 is completed.
- 2022-04-03:
    - Frame analysis module version 1.1.0 is completed. 
    - Distributed soil spring boundary condition has been added. 
    - Log file is addded. 
- 2022-03-06:
    - Frame analysis module version 1.0.0 is completed.
    - GUI technique is confirmed. 
- 2021-11-14:
    - Project Initiates.
    - Mastan3 team is formed.
---
## How to setup the development environment

### Mac OS
- Step 0 (Optional): Install Python Interpreter (version 3.8+)      
If your computer does not have a Python, please install a Python below:
```buildoutcfg
https://www.python.org/downloads/
```

- Step 1: Install PyCharm - Community Editor - Free and open-sourced
```buildoutcfg
https://www.jetbrains.com/pycharm/download/#section=mac
```
- Step 2: Install Git Batch
```buildoutcfg
https://sourceforge.net/projects/git-osx-installer/
```
- Step 3: Open PyCharm and click *Get from CVS*
- Step 4: Click Github and Select the Mastan3 project
```buildoutcfg
If you can not login Github, please create a new project. 
Click File -> Settings -> Version Control -> Github, and login your account. 
```
- Step 5: After the last source code is pulled out from the respository, please setup the environment using:
```buildoutcfg
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
Use Python 3.8 or above version.
```
- Step 6: Click Terminal and install all requried libraries by:
```buildoutcfg
pip install -r requirements.txt
```
- Step 7: Done and congratulation!
```buildoutcfg
Please run main.py as the main entrance of the program.
```

### Windows 
- Step 1: Install PyCharm - Community Editor - Free and open-sourced
```buildoutcfg
https://www.jetbrains.com/pycharm/download/#section=windows
```
- Step 2: Install Git Batch
```buildoutcfg
https://gitforwindows.org/
```
- Step 3: Open PyCharm and click *Get from CVS*
- Step 4: Click Github and Select the Mastan3 project
```buildoutcfg
If you can not login Github, please create a new project. 
Click File -> Settings -> Version Control -> Github, and login your account. 
```
- Step 5: After the last source code is pulled out from the respository, please setup the environment using:
```buildoutcfg
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
Use Python 3.8 or above version.
```
- Step 6: Click Terminal and install all requried libraries by:
```buildoutcfg
pip install -r requirements.txt
```
In Mac OS, the scipy library may not be automatically installed, please use the following method:
 ```pip install --pre -i https://pypi.anaconda.org/scipy-wheels-nightly/simple scipy```

- Step 7: Done and congratulation!
```buildoutcfg
Please run main.py as the main entrance of the program.
```
---
## Libraries
```buildoutcfg
numpy~=1.21.1
pyqtgraph~=0.12.3
vispy~=0.9.6
PySide6~=6.2.3
uuid~=1.30
triangle~=20220202
argparse~=1.4.0
Shapely~=1.8.0
matplotlib~=3.4.2
scipy~=1.7.2
```

