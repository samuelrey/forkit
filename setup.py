from setuptools import setup

setup(
    name='forkit',
    version='0.1',
    py_modules=['forkit'],
    install_requires=[
        'certifi',
        'chardet',
        'Deprecated',
        'gitdb2',
        'GitPython',
        'idna',
        'PyGithub',
        'PyJWT',
        'requests',
        'smmap2',
        'urllib3',
        'wrapt',
    ],
    entry_points='''
        [console_scripts]
        forkit=forkit:main
    '''
)
