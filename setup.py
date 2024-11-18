from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='enem',
    version='1.0.2',
    packages=find_packages(include=['enem', 'enem.*']),
    entry_points={
        'console_scripts': [
            'enem=enem.__main__:main',
        ],
    },
    install_requires=[
        'pygments',
        'colorama',
        'pillow',
        'PyMuPDF',
    ],
    python_requires='>=3.6',
    author='Pedro Luis Dias',
    author_email='luisp.diias@gmail.com',
    description='CLI Tool for ENEM PDF Extraction and JSON Export.',
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/luiisp/enem-extractor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
