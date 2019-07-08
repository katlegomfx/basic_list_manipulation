from setuptools import setup, find_packages

setup(
    name='basic_list_manipulation',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Katlegomfx python list handling package',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://github.com/katlegomfx/basic_list_manipulation.git',
    author='katlegomfx',
    author_email='katlegomfx@gmail.com'
)
