# Overview
This utility will allow you to make backups of volumes in your docker (backups are saved to your dropbox).

Currently only works on linux.

# How to install
1. Clone the repository
2. `pip3 install .` in the root of the directory

# How to use
The utility is available from the terminal:
`backup_docker <volume_name> <token>`
- `<volume_name>` - volume name for backup
- `<token>` - OAuth2 token for authorization in dropbox
