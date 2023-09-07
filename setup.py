from setuptools import setup

readme = open("README.MD")

setup(
    name='ee.py',
    version='1.0',
    packages=['eepy'],
    url='https://github.com/binlaab/ee.py',
    license='',
    author='binlaab',
    author_email='root@binlab.es.eu.org',
    description='eepy',
    long_description_content_type='text/markdown',
    long_description=readme.read(),
    package_data={
        'eepy': [
            'py.typed'
        ]
    }
)
