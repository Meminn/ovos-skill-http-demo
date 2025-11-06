#!/usr/bin/env python3
from setuptools import setup
import os
from os import walk, path

SKILL_CLAZZ = "HttpDemoSkill"
CREATE_SKILL_FUNC = "create_skill"
URL = "https://github.com/meminn/ovos-skill-http-demo"
AUTHOR = "meminn"
PYPI_NAME = URL.split("/")[-1]
SKILL_ID = f"{PYPI_NAME.lower()}.{AUTHOR.lower()}"
SKILL_PKG = PYPI_NAME.lower().replace('-', '_')
PLUGIN_ENTRY_POINT = f"{SKILL_ID}={SKILL_PKG}:{CREATE_SKILL_FUNC}"
VERSION = "0.0.5"
DESCRIPTION = "An Open Voice OS skill that demonstrates making HTTP requests to a public API."
EMAIL = "meminn@example.com"
LICENSE = "Apache-2.0"

def get_requirements(requirements_filename: str):
    """
    Parse requirements from a file.

    Args:
        requirements_filename (str, optional): The filename of the requirements file.
            Defaults to "requirements.txt".

    Returns:
        List[str]: A list of parsed requirements.

    Notes:
        If the environment variable MYCROFT_LOOSE_REQUIREMENTS is set, this function
        will modify the parsed requirements to use loose version requirements,
        replacing '==' with '>=' and '~=' with '>='.

    """
    requirements_file = path.join(path.abspath(path.dirname(__file__)),
                                  requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip()
                    and not r.strip().startswith("#")]
    if 'MYCROFT_LOOSE_REQUIREMENTS' in os.environ:
        print('USING LOOSE REQUIREMENTS!')
        requirements = [r.replace('==', '>=').replace('~=', '>=') for r in requirements]
    return requirements

def find_resource_files():
    """ensure all non-code resource files are included in the package"""
    # add any folder with files your skill uses here!
    resource_base_dirs = ("locale", "ui", "vocab", "dialog", "regex")
    package_root = path.join(path.dirname(__file__), SKILL_PKG)
    package_data = []
    for res in resource_base_dirs:
        resource_dir = path.join(package_root, res)
        if path.isdir(resource_dir):
            for (directory, _, files) in walk(resource_dir):
                if files:
                    relative_dir = path.relpath(directory, package_root)
                    cleaned = relative_dir.replace("\\", "/")
                    package_data.append(f"{cleaned}/*")
    return package_data

# Setup configuration
setup(
    name=PYPI_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    package_dir={SKILL_PKG: SKILL_PKG},
    package_data={SKILL_PKG: find_resource_files()},
    packages=[SKILL_PKG],
    include_package_data=True,
    install_requires=get_requirements("requirements.txt"),
    keywords='ovos skill plugin',
    entry_points={
        'opm.skill': [PLUGIN_ENTRY_POINT]
    }
)
