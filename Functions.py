import subprocess
import os
import re

# Functions
def get_installed_version(name):
  """Get the installed version of the given software.
  
  Args:
    name (str): The name of the software.
    
  Returns:
    str: The installed version of the software. Returns an empty string if the software is not installed.
  """
  output = subprocess.run(['wmic', 'product', 'get', 'name, version'], stdout=subprocess.PIPE).stdout.decode()
  pattern = f'^{name}\s+(\d+\.\d+\.\d+)'
  match = re.search(pattern, output, re.MULTILINE)
  if match:
    return match.group(1)
  else:
    return ''

def install_dem():
  """Install the VMware Dynamic Environment Manager Enterprise.
  """
  install_dir = 'C:\\Program Files\\VMware DEM'
  msi_path = '\\\\dsfs\\software\\VMware Dynamic Environment Manager Enterprise 2209 10.7 x64.msi'
  log_path = 'C:\\Temp\\Logs\\InstallDEM.log'
  cmd = [
      'msiexec', '/i', msi_path, '/qn',
      f'INSTALLDIR="{install_dir}"',
      'ADDLOCAL="FlexEngine,FlexMigrate,FlexProfilesSelfSupport"',
      f'/l* "{log_path}"'
  ]
  subprocess.run(cmd)

def install_app_vol():
  """Install the VMware Horizon App Volumes agent.
  """
  msi_path = '\\\\dsfs\\software\\Horizon\\App Volumes Agent.msi'
  manager_addr = '<Manager_FQDN/IP>'
  manager_port = '<port/443>'
  log_path = 'C:\\Temp\\Logs\\InstallAppVol.log'
  cmd = [
      'msiexec', '/i', msi_path, '/qn',
      f'MANAGER_ADDR={manager_addr}',
      f'MANAGER_PORT={manager_port}',
      'EnforceSSLCertificateValidation=0',
      f'/l* "{log_path}"'
  ]
  subprocess.run(cmd)