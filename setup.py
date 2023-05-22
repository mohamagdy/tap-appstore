#!/usr/bin/env python

from setuptools import setup

setup(name="tap-appstore",
      version="0.2.2.a3+airbyte",
      description="Singer.io tap for extracting data from the App Store Connect API",
      author="JustEdro",
      url="https://github.com/JustEdro",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap-appstore"],
      install_requires=[
          "singer-python==5.13.0",
          "appstoreconnect==0.10.0",
          "pytz==2023.3"
      ],
      entry_points="""
          [console_scripts]
          tap-appstore=tap_appstore:main
      """,
      packages=["tap_appstore"],
      package_data={},
      include_package_data=True,
)
