from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    licence = f.read()

setup(name='sample_package',
      version='1.0',
      description='Sample package',
      long_description=readme,
      author='Bartosz Tyński',
      license=license,
      packages=find_packages(exclude=('tests'))
)
