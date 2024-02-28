import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)

while True:
    project_name = input("Enter the project name: ")
    if project_name != "":
        break

# Define list of files
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

# Create files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    if not filedir.is_dir():
        os.makedirs(filedir, exist_ok=True)
    if not filepath.exists() or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"File is already present at: {filepath}")
