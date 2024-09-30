directory_tree = {
    'type': 'directory',
    'name': 'root',
    'path': '/',
    'children': [
        {
            'type': 'directory',
            'name': 'home',
            'path': '/home',
            'children': [
                {
                    'type': 'directory',
                    'name': 'user',
                    'path': '/home/user',
                    'children': [
                        {
                            'type': 'file',
                            'name': 'file1.txt',
                            'path': '/home/user/file1.txt',
                        },
                        {
                            'type': 'file',
                            'name': 'file2.txt',
                            'path': '/home/user/file2.txt',
                        },
                    ],
                },
                {'type': 'file', 'name': 'readme.md', 'path': '/home/readme.md'},
            ],
        },
        {
            'type': 'directory',
            'name': 'etc',
            'path': '/etc',
            'children': [
                {'type': 'file', 'name': 'config.yaml', 'path': '/etc/config.yaml'},
                {
                    'type': 'directory',
                    'name': 'nginx',
                    'path': '/etc/nginx',
                    'children': [
                        {
                            'type': 'file',
                            'name': 'nginx.conf',
                            'path': '/etc/nginx/nginx.conf',
                        },
                        {
                            'type': 'directory',
                            'name': 'sites-enabled',
                            'path': '/etc/nginx/sites-enabled',
                            'children': [
                                {
                                    'type': 'file',
                                    'name': 'default',
                                    'path': '/etc/nginx/sites-enabled/default',
                                }
                            ],
                        },
                    ],
                },
            ],
        },
    ],
}


def find_file(name, directory):
    # Base Case: Wenn die Datei im aktuellen Verzeichnis gefunden wird
    if directory['type'] == 'file' and directory['name'] == name:
        return directory['path']

    # Wenn das Verzeichnis Kinder hat, durchlaufe sie
    if directory['type'] == 'directory' and 'children' in directory:
        for child in directory['children']:
            path = find_file(name, child)  # Rekursiver Aufruf
            if path:  # Wenn der Pfad gefunden wurde, gebe ihn zurück
                return path

    return None  # Wenn die Datei nicht gefunden wird


if __name__ == '__main__':
    path = find_file('config.yaml', directory_tree)
    print(path)  # Sollte den Pfad zur Datei ausgeben
