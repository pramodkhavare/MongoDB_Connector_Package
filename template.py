#Tjis Template is for MongoDB Connection

import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",  #ci is continious integration
   
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py",
    
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",         #i will right all unit test cases
   "tests/integration/__init__.py",
   "tests/integration/int.py",   
   
   "init_setup.sh",  #linus command (all command in terminal )
   "requirements.txt",   #requirement in production environment
   "requirements_dev.txt", #requirement in developement environment
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file