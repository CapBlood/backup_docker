import os

import dropbox


def uploadFileDropbox(path, token, path_upload='/'):
    """Uploads a file to the DropBox.

    Args:
        path (str): path to file.
        token (str): an authentication key for Dropbox.
        path_upload (str): file system boot path Dropbox.

    Returns:
        FileMetadata: metadata about the loaded dump.
    """

    if not os.path.isfile(path):
        raise ValueError('path must point to a file!')

    dbx = dropbox.Dropbox(token)
    filename = os.path.basename(path)
    path_upload = os.path.join(path_upload, filename)
    with open(path, 'rb') as file:
        response = dbx.files_upload(file.read(), path_upload)
    return response
