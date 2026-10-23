from setuptools import find_packages, setup

from typing import List

    
def get_requirements() -> List[str]:
    """
    This function returns list of requirements
    """
    requirement_list : List[str] = []
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            print(lines)
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")

                
    return requirement_list

print(get_requirements())

setup(
    name="Trip_Planner",
    version="0.0.1",
    author="Pratik Potdukhe",
    author_email="pratikpotdukhe89@gmail.com",
    install_requires=get_requirements(),
    packages= find_packages()

)