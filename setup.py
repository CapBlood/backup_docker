from setuptools import setup

setup(name='Docker Backup Utility',
      version='1.0',
      packages=['backup_utility'],
      setup_requires=['dropbox', 'python-crontab'],
      entry_points={
            'console_scripts': ['backup_docker=backup_utility.__main__:main'],
      })