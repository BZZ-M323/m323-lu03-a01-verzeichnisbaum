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

def test_find_file_found_in_deep_nested_subdir():
    """Testet, ob die Datei in einem tief verschachtelten Verzeichnis gefunden wird, mit mehreren parallelen Verzeichnissen."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {
                'type': 'directory',
                'name': 'subdir_1',
                'path': '/subdir_1',
                'children': [
                    {'type': 'file', 'name': 'file_in_subdir_1.txt', 'path': '/subdir_1/file_in_subdir_1.txt'}
                ]
            },
            {
                'type': 'directory',
                'name': 'subdir_2',
                'path': '/subdir_2',
                'children': [
                    {
                        'type': 'directory',
                        'name': 'nested_subdir_1',
                        'path': '/subdir_2/nested_subdir_1',
                        'children': [
                            {'type': 'file', 'name': 'file_in_nested_subdir_1.txt', 'path': '/subdir_2/nested_subdir_1/file_in_nested_subdir_1.txt'}
                        ]
                    },
                    {
                        'type': 'directory',
                        'name': 'nested_subdir_2',
                        'path': '/subdir_2/nested_subdir_2',
                        'children': [
                            {'type': 'file', 'name': 'file_in_nested_subdir_2.txt', 'path': '/subdir_2/nested_subdir_2/file_in_nested_subdir_2.txt'}
                        ]
                    }
                ]
            },
            {
                'type': 'directory',
                'name': 'subdir_3',
                'path': '/subdir_3',
                'children': [
                    {
                        'type': 'directory',
                        'name': 'deep_nested_subdir',
                        'path': '/subdir_3/deep_nested_subdir',
                        'children': [
                            {
                                'type': 'directory',
                                'name': 'even_deeper_subdir',
                                'path': '/subdir_3/deep_nested_subdir/even_deeper_subdir',
                                'children': [
                                    {'type': 'file', 'name': 'deep_file.txt', 'path': '/subdir_3/deep_nested_subdir/even_deeper_subdir/deep_file.txt'}
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
    path = main.find_file('deep_file.txt', directory_tree)
    assert path == '/subdir_3/deep_nested_subdir/even_deeper_subdir/deep_file.txt'

def test_find_file_not_found():
    """Testet den Fall, dass die Datei nicht gefunden wird, obwohl mehrere Verzeichnisse vorhanden sind."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {
                'type': 'directory',
                'name': 'subdir_1',
                'path': '/subdir_1',
                'children': []
            },
            {
                'type': 'directory',
                'name': 'subdir_2',
                'path': '/subdir_2',
                'children': [
                    {'type': 'file', 'name': 'another_file.txt', 'path': '/subdir_2/another_file.txt'}
                ]
            }
        ]
    }
    path = main.find_file('non_existent.txt', directory_tree)
    assert path is None

def test_find_file_found_in_multiple_nested_subdirs():
    """Testet, ob die Datei in einem tief verschachtelten Verzeichnis mit mehreren parallelen Verzeichnissen gefunden wird."""
    directory_tree = {
        'type': 'directory',
        'name': 'root',
        'path': '/',
        'children': [
            {
                'type': 'directory',
                'name': 'subdir_A',
                'path': '/subdir_A',
                'children': [
                    {
                        'type': 'directory',
                        'name': 'nested_A1',
                        'path': '/subdir_A/nested_A1',
                        'children': [
                            {'type': 'file', 'name': 'file_A1.txt', 'path': '/subdir_A/nested_A1/file_A1.txt'}
                        ]
                    },
                    {
                        'type': 'directory',
                        'name': 'nested_A2',
                        'path': '/subdir_A/nested_A2',
                        'children': []
                    }
                ]
            },
            {
                'type': 'directory',
                'name': 'subdir_B',
                'path': '/subdir_B',
                'children': [
                    {'type': 'file', 'name': 'file_in_B.txt', 'path': '/subdir_B/file_in_B.txt'}
                ]
            },
            {
                'type': 'directory',
                'name': 'subdir_C',
                'path': '/subdir_C',
                'children': [
                    {
                        'type': 'directory',
                        'name': 'nested_C1',
                        'path': '/subdir_C/nested_C1',
                        'children': [
                            {
                                'type': 'directory',
                                'name': 'deep_nested_C1',
                                'path': '/subdir_C/nested_C1/deep_nested_C1',
                                'children': [
                                    {'type': 'file', 'name': 'file_in_deep_nested_C1.txt', 'path': '/subdir_C/nested_C1/deep_nested_C1/file_in_deep_nested_C1.txt'}
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
    path = main.find_file('file_in_deep_nested_C1.txt', directory_tree)
    assert path == '/subdir_C/nested_C1/deep_nested_C1/file_in_deep_nested_C1.txt'
