# setup.py
from setuptools import setup

SKILL_CLAZZ = "HttpDemoSkill"
URL = "https://github.com/Meminn/ovos-skill-http-demo"
AUTHOR = "Meminn"
PYPI_NAME = URL.split("/")[-1]
SKILL_ID = f"{PYPI_NAME.lower()}.{AUTHOR.lower()}"
SKILL_PKG = PYPI_NAME.lower().replace('-', '_')
PLUGIN_ENTRY_POINT = f"{SKILL_ID}={SKILL_PKG}:{SKILL_CLAZZ}"

setup(
    name=PYPI_NAME,
    version="0.0.1",
    url=URL,
    author=AUTHOR,
    packages=[SKILL_PKG],
    install_requires=["ovos-workshop", "requests"],
    entry_points={"ovos.plugin.skill": [PLUGIN_ENTRY_POINT]},
)
