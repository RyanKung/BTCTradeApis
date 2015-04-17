from setuptools import setup, find_packages

setup(
    name='BTCTradeApis',
    version='0.1.1',
    description='BTC trade api implementation for python',
    author='Ryan Kung',
    author_email='ryankung@ieee.org',
    license='MIT',
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'': 'src'},
    tests_require=['nose'],
    install_requires=['requests'],
    test_suite='nose.collector',
)
