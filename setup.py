from setuptools import setup, find_packages

setup(
    name='test202206161037',
    version='0.1',
    license='Apache',
    author="Robin Neville",
    author_email='byntje@example.com',
    packages=find_packages('a_package'),
    package_dir={'': 'a_package'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='Test project',
    install_requires=[
        "django>=2.2",
    ],

)
