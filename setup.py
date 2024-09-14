from setuptools import setup, find_packages

setup(
    name='linepy',
    version='1.0.0-beta.1',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    author='NgTuanVy',
    author_email='tuanvy860@gmail.com',
    description='LinePy is a package that help you with Linear algebra',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TuanVy-dot/linepy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)