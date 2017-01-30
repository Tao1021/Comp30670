'''
Created on 27 Jan 2017

@author: Tao
'''
from setuptools import setup
setup(name="systeminfo",
      version="0.1",
      description="Basic system information for Comp30670",
      url="",
      author="Tao Li",
      author_email="taoli1021@gmail.com",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
            }
    )