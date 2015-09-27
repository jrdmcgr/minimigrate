from setuptools import setup

setup(
    name='minimigrate',
    version='0.1.0',
    description='A simple schema migration tool',
    url='https://github.com/jrdmcgr/minimigrate',
    author='Jared McGuire',
    author_email='jrdmcgr@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    keywords='schema migration',
    py_modules=['minimigrate'],
    install_requires=['sqlalchemy', 'pathlib'],
    extras_require={
        'test': ['nose', 'coverage'],
    },
    entry_points={
        'console_scripts': [
            'minimigrate=minimigrate:main',
        ],
    },
)
