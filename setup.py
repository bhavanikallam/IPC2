import os
from setuptools import setup, find_packages

project_path = os.path.dirname(__file__)


install_requires = []
with open(os.path.join(project_path, "IPC_requirements.txt"), encoding="utf-8") as fh:
    for line in fh:
        req_packages = line.strip()
        if not req_packages.startswith(('pip', 'setuptools', 'six', 'wheel')):
            install_requires.append(req_packages)


VERSION = '0.1'
DESCRIPTION = 'TCPIPCSocketServer'
LONG_DESCRIPTION = 'IPC server'

# Setting up
setup(
    name="IPCApp",
    version=VERSION,
    author_email="developer@aline-consulting.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=install_requires
    # install_requires=['pandas', 'pendulum', 'scipy']
)
