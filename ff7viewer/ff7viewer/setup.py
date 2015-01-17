try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Final Fantasy 7 model viewer in Python and OpenGL',
    'author': 'George Shore',
    # 'url': 'home page for the package',
    # 'download_url': 'Where to download it.',
    'author_email': 'george@georgeshore.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['ff7viewer'],
    'scripts': [],
    'name': 'ff7viewer'
}

setup(**config)