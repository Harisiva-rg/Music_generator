from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='music_generator',
    version='0.0.1',
    author='Harisiva R G',
    author_email='harisivarg@gmail.com',
    description='A package to create music notes',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Harisiva-rg/music_generator',
    packages=find_packages(),
    install_requires=[], 
    license="GPL",
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",

)
