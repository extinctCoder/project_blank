from setuptools import setup, find_packages

setup(
    name='pb',
    version='0.0.1',
    url='https://github.com/extinctCoder/project_blank.git',
    author='extinctCoder',
    author_email='write2shourov@gmail.com',
    description='demo project to learn python more ... :)',
    packages=find_packages(include=['project_blank']),
    install_requires=['dynaconf >= 3.1.11'],
)
