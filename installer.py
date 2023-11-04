###Requires VS studio build tools for C++#####
import sys
import subprocess
# Checks useful python dependencies and installs them if not found
def install_checker(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#subprocess.check_call([sys.executable, "-m", "pip", "install", "wheel", "setuptools"])
#install_checker("PyVCF3")
#subprocess.check_call([sys.executable, ])

