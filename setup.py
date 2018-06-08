from setuptools import setup, find_packages

setup(
  name='dukedomscardbroker',
  version='0.0.0',
  description='microservice for managing card decks and flow for Dukedoms of Daleria',
  packages=find_packages(exclude=['swagger_codegen', '&.tests']),
  include_package_data=True
)
