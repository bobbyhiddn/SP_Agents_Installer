This is a python script that can install all the necessary session-perminance agents in my environment. I want it to check if the agents are already installed, and if they are, it needs to make sure it is the version specified in the script. 

msiexec.exe /i "\\dsfs\software\VMware Dynamic Environment Manager Enterprise 2209 10.7 x64.msi" /qn ​INSTALLDIR="C:\Program Files\​VMware DEM" ADDLOCAL="FlexEngine,FlexMigrate,FlexProfilesSelfSupport" /l* InstallDEM.log