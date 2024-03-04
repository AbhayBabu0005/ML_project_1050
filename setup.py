from setuptools import find_packages,setup
from typing import List



PROJECT_NAME="Machine Learning Project "
VERSION="0.0.1"
DESCRIPTION="This is our machine learning project modular coding"
AUTHOR_NAME="Abhay"
AUTHOR_EMAIL='abhayhbabu005@gmail.com'
REQUIREMENTS_FILE_NAME="requirements.txt"
HYPEN_E_DOT='-e.'

def get_requirements()->List[str]:#the function should return the list of requirements like [pandas,numpy]
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[req.replace("\n","")for req in requirement_list ]
    if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)









setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
     )