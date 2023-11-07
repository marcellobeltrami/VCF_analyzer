#IMPORTANT: this installer is based on tools available on BEAR. 
# It will not work on local machines
import sys
import subprocess
location_install = input("PATH where to install bin (format /where/to/install/bin:$PATH):")

commands = ["pip install pywin32 setuptools", #Dependencies for 
             ] #list of commands you want to pass 
for command in commands:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()

#Commands required to install dependencies of VAPr

VAPR_dep = ["conda install python=3 pandas mongodb pymongo jupyter notebook", #Ancillaries
            "docker pull mongodb/mongodb-community-server", "docker run --name mongo -d mongodb/mongodb-community-server:latest" # MongoDB
            "wget https://github.com/samtools/bcftools/releases/download/1.6/bcftools-1.6.tar.bz2",
            "tar -vxjf bcftools-1.6.tar.bz2","cd bcftools-1.6","make", "make install", 
            "export {location_installation}",]
