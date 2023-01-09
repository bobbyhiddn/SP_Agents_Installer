This is a python script that can install all the necessary session-perminance agents in my environment. I want it to check if the agents are already installed, and if they are, it needs to make sure it is the version specified in the script. 

Before use, the defaults must be changed to fit your environment's AppVolume Manager and DEM configs. The DEM will probably be less complicated since it is so heavily administrated using GPOs.


These are the commands to silently install both the DEM and AppVol agent:


DEM:

msiexec.exe /i "\\dsfs\software\VMware Dynamic Environment Manager Enterprise 2209 10.7 x64.msi" /qn ​INSTALLDIR="C:\Program Files\​VMware DEM" ADDLOCAL="FlexEngine,FlexMigrate,FlexProfilesSelfSupport" /l* "C:\Temp\Logs\InstallDEM.log"

AppVol:

msiexec.exe /i "\\dsfs\software\Horizon\App Volumes Agent.msi" /qn MANAGER_ADDR=<Manager_FQDN/IP> MANAGER_PORT=<port/443> EnforceSSLCertificateValidation=0 /l* "C:\Temp\Logs\InstallAppVol.log"

