from setuptools import setup

setup(
    name='wowicache',
    version='1.0.0',
    description='OPENWOWI Wowiport SQLAlchemy overlay',
    url='https://github.com/seb-bau/wowicache',
    author='Sebastian Bauhaus',
    author_email='sebastian@bytewish.de',
    license='GPL-3.0',
    packages=['wowicache'],
    install_requires=[
        'attrs>=23.1.0',
        'cattrs>=23.1.2',
        'certifi>=2023.7.22',
        'harset-normalizer>=3.2.0',
        'graypy>=2.1.0',
        'idna>=3.4',
        'jsonmerge>=1.9.2',
        'jsonschema>=4.19.0',
        'jsonschema-specifications>=2023.7.1',
        'platformdirs>=3.10.0',
        'pyhumps>=3.8.0',
        'python-dotenv>=1.0.0',
        'referencing>=0.30.2',
        'requests>=2.31.0',
        'requests-cache>=1.1.0',
        'rpds-py>=0.9.2',
        'six>=1.16.0',
        'url-normalize>=1.4.3',
        'urllib3>=2.0.4',
        'wowipy>=1.1.14',
        'SQLAlchemy~=2.0.20'
                      ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)