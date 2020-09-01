import argparse
import os

from backup_utility import backup
from backup_utility import upload


def getParser():
    parser_backup = argparse.ArgumentParser(description='Make a backup of volume')

    parser_backup.add_argument('volume', help='Name of docker volume')
    parser_backup.add_argument('token', help='OAuth2 token for Dropbox')

    return parser_backup


def main():
    parser = getParser()
    namespace = parser.parse_args()

    path_backup = backup.backupVolume(namespace.volume)
    upload.uploadFileDropbox(path_backup, namespace.token)
    os.remove(path_backup)


if __name__ == '__main__':
    main()
