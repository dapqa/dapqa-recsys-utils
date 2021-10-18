def pytest_addoption(parser):
    extra_options = {
        "skip_datasets": "List of ids of datasets which tests must be skipped"
    }

    for option, description in extra_options.items():
        parser.addini(option, description)
        parser.addoption(f'--{option}', help=description)