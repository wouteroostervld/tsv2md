try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'tsv2md',
    'author': 'Wouter Oosterveld',
    #'url': 'URL to get it at.',
    #'download_url': 'Where to download it.',
    'author_email': 'Wouter+tsv2md@fizzyflux.nl',
    'version': '0.1',
    'install_requires': [],
    'packages': ['tsv2md'],
    'scripts': ['scripts/tsv2md'],
    'name': 'tsv2md'
}

setup(**config)
