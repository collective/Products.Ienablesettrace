from setuptools import setup, find_packages
import os

version = "1.1dev"

setup(
    name="Products.Ienablesettrace",
    version=version,
    description="Fork of Products.enablesettrace which also allows import "
    "of ipdb in restricted code.",
    long_description=open("README.txt").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Zope Public License",
    ],
    keywords="Python Zope Plone skin script debugging",
    author="Mark van Lent",
    author_email="m.van.lent@zestsoftware.nl",
    url="http://github.com/collective/Products.Ienablesettrace",
    license="ZPL 2.1",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
