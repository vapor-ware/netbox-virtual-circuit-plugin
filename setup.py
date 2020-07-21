import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
readme = ""
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        readme = f.read()

setup(
    name='netbox-virtual-circuit-plugin',
    version='0.3.0',
    description='A Netbox plugin that supports Virtual Circuit management',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/vapor-ware/netbox-virtual-circuit-plugin',
    author='Hoanh An',
    license='GNU General Public License v3.0',
    package_data={
        '': ['LICENSE'],
    },
    install_requires=[],
    packages=find_packages(),
    include_package_data=True
)
