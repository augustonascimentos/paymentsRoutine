import os
import importlib


def files_on_tree(root_path):
    files = []
    for file in os.listdir(root_path):
        if file[0] != '_':
            path = root_path+'/'+file
            if os.path.isdir(path):
                files = files + files_on_tree(path)
            elif os.path.isfile(path):
                files.append(path.replace('.py', ''))
    return files


def Routes(app):
    path = os.path.dirname(__file__)
    files = files_on_tree(path)
    files = [file.replace(os.path.dirname(__file__),
                          'src.main.flask_routes').replace('/', '.') for file in files]

    for file in files:
        try:
            print('Import {}...'.format(file))
            route = importlib.import_module(file, 'route')
            getattr(route, file.split('.').pop().title())(app)
        except ImportError as e:
            print(e)
