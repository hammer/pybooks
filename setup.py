from setuptools import setup

setup(
    name='pybooks',
    version='0.1',
    scripts=['scripts/pybooks.py'],
    zip_safe=False,
    install_requires=['requests', 'pyyaml']
)

