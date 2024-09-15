from setuptools import setup, find_packages

setup(
    name='lalgpy',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    author='NgTuanVy',
    author_email='tuanvy860@gmail.com',
    description='lalgpy is a package that help you with Linear algebra',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TuanVy-dot/lalgpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)