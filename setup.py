from setuptools import find_packages, setup


with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='tracker',
    version='0.1',
    description='Tracker Service',
    author='Horatiu Maiereanu',
    author_email='horatiu.maiereanu@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=dependencies,
)
