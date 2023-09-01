import main
def test_find_file_found_at_root():
    """Testet, ob die Datei im Wurzelverzeichnis gefunden wird."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {'type': 'file', 'name': 'root_file.txt', 'path': '/root_file.txt'},
        ],
    }
    path = main.find_file('root_file.txt', directory_tree)
    assert path == '/root_file.txt'

def test_find_file_found_in_subdir():
    """Testet, ob die Datei in einem Unterordner gefunden wird."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {
                'type': 'directory',
                'name': 'subdir',
                'path': '/subdir',
                'children': [
                    {'type': 'file', 'name': 'file_in_subdir.txt', 'path': '/subdir/file_in_subdir.txt'}
                ]
            }
        ]
    }
    path = main.find_file('file_in_subdir.txt', directory_tree)
    assert path == '/subdir/file_in_subdir.txt'

def test_find_file_not_found():
    """Testet den Fall, dass die Datei nicht gefunden wird."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {'type': 'file', 'name': 'another_file.txt', 'path': '/another_file.txt'},
        ],
    }
    path = main.find_file('non_existent.txt', directory_tree)
    assert path is None

def test_find_file_nested_subdir():
    """Testet, ob die Datei in einem tief verschachtelten Unterordner gefunden wird."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {
                'type': 'directory',
                'name': 'subdir',
                'path': '/subdir',
                'children': [
                    {
                        'type': 'directory',
                        'name': 'nested_subdir',
                        'path': '/subdir/nested_subdir',
                        'children': [
                            {'type': 'file', 'name': 'nested_file.txt', 'path': '/subdir/nested_subdir/nested_file.txt'}
                        ]
                    }
                ]
            }
        ]
    }
    path = main.find_file('nested_file.txt', directory_tree)
    assert path == '/subdir/nested_subdir/nested_file.txt'
