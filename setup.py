from setuptools import setup

setup(
    name='ism',
    version='1.0.0',
    description='Interactive SSH menu',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
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
        'Development Status :: 5 - Production/Stable'
    ],
)
