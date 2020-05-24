from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    long_description = long_description.replace('images/', 'https://raw.githubusercontent.com/Sch-Tomi/ism/master/images/')

setup(
    name='ism',
    version='1.0.3',
    description='Interactive SSH menu',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/Sch-Tomi/ism',
    author='Sch-Tomi',
    py_modules=['ism'],
    entry_points={
        'console_scripts': [
            'ism = ism:main',
        ],
    }
    ,
    zip_safe=False,
    install_requires=[
        ['questionary'],
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
