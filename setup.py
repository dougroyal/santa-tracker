from setuptools import setup, find_packages

PROJECT_NAME = 'santa_tracker'

__version__ = None  # this will be set by the next two lines
with open('santa_tracker/__version__.py') as f:
    exec(f.read())

config = dict(
    name=PROJECT_NAME,
    version=__version__,
    packages=find_packages(),
    url='https://github.com/dougroyal/santa-tracker',
    install_requires=[
        'pygame==1.9.3'
    ],
    entry_points={
        'console_scripts': [
            'santa-tracker=santa_tracker.bin.main:main',
        ]
    },
)

if __name__ == '__main__':
    setup(**config)

