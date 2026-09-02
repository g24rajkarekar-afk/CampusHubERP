import importlib


def load_module(module_name):
    try:
        module = importlib.import_module(module_name)

        print(f"Module '{module_name}' loaded successfully.")

        return module

    except ImportError:
        print(f"Could not load module: {module_name}")
        return None