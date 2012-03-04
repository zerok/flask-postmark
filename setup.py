"""
Flask-Postmark
==============

Flask-Postmark provides a simple layer on top of the Postmark library for
Python. Right now this only supported sending mails through postmark.

To configure Postmark for use in your application, following settings are
provided:

POSTMARK_API_KEY
    Your service's Postmark API key.

POSTMARK_SENDER
    Provide a default sender for your emails with this.

POSTMARK_TEST_MODE
    Setting this to True will prevent mails from actually being sent but
    instead being printed.

"""
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

version = "0.1"

setup(
    name="Flask-Postmark",
    version=version,
    url="https://github.com/zerok/flask-postmark",
    license="BSD",
    author="Horst Gutmann",
    author_email="zerok@zerokspot.com",
    description="Integration of Postmark with Flask",
    long_description=__doc__,
    packages=["flask_postmark"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "Flask",
        "python-postmark",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
