from SP_Functions import prompt_app_vol_params, get_installed_version, install_dem, install_app_vol

# Constants
# I'm going to make this optional at some point.
INSTALL_DEM = True
INSTALL_APP_VOL = True

# Main
if INSTALL_DEM:
  dem_version = get_installed_version('VMware Dynamic Environment Manager Enterprise')
  if dem_version:
    print(f'VMware Dynamic Environment Manager Enterprise {dem_version} is already installed.')
  else:
    install_dem()

if INSTALL_APP_VOL:
  app_vol_version = get_installed_version('VMware Horizon App Volumes Agent')
  if app_vol_version:
    print(f'VMware Horizon App Volumes Agent {app_vol_version} is already installed.')
  else:
    manager_addr, manager_port = prompt_app_vol_params()
    install_app_vol(manager_addr, manager_port)