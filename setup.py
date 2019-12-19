from setuptools import setup

with open('pypi_desc.md') as f:
    long_description = f.read()

setup(
    name='s3-extend',
    version='1.9',
    packages=[
      's3_extend',
      's3_extend.gateways'
    ],
    install_requires=[
        'python-banyan>=3.8',
        'pymata-express>=1.7'
    ],

    entry_points={
        'console_scripts': [
            's3a = s3_extend.s3a:s3ax',
            's3e = s3_extend.s3e:s3ex',
            's3p = s3_extend.s3p:s3px',
            's3r = s3_extend.s3r:s3rx',
            'ardgw = s3_extend.gateways.arduino_gateway:arduino_gateway',
            'espgw = s3_extend.gateways.esp8266_gateway:esp8266_gateway',
            'pbgw = s3_extend.gateways.picoboard_gateway:picoboard_gateway',
            'rpigw = s3_extend.gateways.rpi_gateway:rpi_gateway',
            'wsgw = s3_extend.gateways.ws_gateway:ws_gateway',
        ]
    },

    url='https://github.com/MrYsLab/s3-extend',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='A Non-Blocking Event Driven Applications Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Scratch3', 'Arduino', 'ESP-8266', 'Raspberry Pi'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: System :: Hardware'
    ],
)
