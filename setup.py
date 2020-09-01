from setuptools import setup

setup(name='DockerBackupUtility',
      author='CapBlood',
      author_email='stalker.anonim@mail.ru',
      description=('This utility will allow you to make backups'
                   'of volumes in your docker (backups are saved to your dropbox).'),
      version='1.0',
      url='https://github.com/CapBlood/backup_docker',
      download_url='https://github.com/CapBlood/backup_docker/archive/1.0.tar.gz',
      license='GPL-3.0',
      packages=['backup_utility'],
      install_requires=['dropbox'],
      classifiers=[
            'Environment :: Console',
            'Programming Language :: Python',
            'Operating System :: Linux'
      ],
      entry_points={
            'console_scripts': ['backup_docker=backup_utility.__main__:main'],
      })