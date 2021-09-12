from setuptools import setup, find_packages

classifiers = [
    'Developement Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9.5'
]

setup(
name = 'trading_stoploss_and_takeprofit',
version ='1.0.1',
description = 'trading_stoploss_and_takeprofit is a python program that calculate stop loss and take profit',
url= 'https://github.com/Iankfc/trading_stoploss_and_takeprofit',
author='ece',
author_email='odesk5@outlook.com',
license = 'None',
classifiers=classifiers,
keywords='None',
packages=find_packages(),
use_scm_version=True,
include_package_data=True,
setup_requires=['setuptools_scm'],
install_requires=['pyodbc==4.0.30',
                'packaging==20.9',
                'pandas==1.2.5',
                'SQLAlchemy==1.4.22']
)