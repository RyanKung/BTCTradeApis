from setuptools import setup, find_packages

setup(
    name='BTCTradeApis',
    version='0.1',
    description='BTC trade api implementation for python',
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Console',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial'
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'}
)
