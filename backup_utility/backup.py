import os
import time
import subprocess
import tarfile


def archiveFolder(path_dir, path_tar='.'):
    """Creates a tar archive with gzip compression of the specified directory.

    Args:
        path_dir (str): path to directory.
        path_tar (str): path to the created archive.

    Returns:
        str: the path to the created archive.
    """

    if not os.path.exists(path_dir):
        raise ValueError('path dir: no such file or directory')

    if not os.path.isdir(path_dir):
        raise ValueError('path must point to a directory!')

    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = '{}.tar.gz'.format(timestr)
    path = os.path.join(path_tar, filename)

    tar = tarfile.open(path, 'w:gz')
    tar.add(path_dir)
    tar.close()

    return path


def backupVolume(name, path_backup='.'):
    """Create a backup of the specified directory.

    Args:
         name (str): name of volume.
         path_backup (str): path to the created backup.

    Returns:
        str: the path to the created backup.
    """

    process = subprocess.Popen(['docker', 'volume', 'inspect', '-f', "{{ .Mountpoint }}", name],
                               universal_newlines=True, stdout=subprocess.PIPE)
    path_volume = process.communicate()[0].strip()
    path_tar = archiveFolder(path_volume, path_backup)

    return path_tar
