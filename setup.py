from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='aus-local-councils',
    version='1.0',
    description='Get list of local councils for Australian states/territories.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OpenGovAus/aus-local-councils',
    author='king-millez',
    author_email='millez.dev@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6'
)