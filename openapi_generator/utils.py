import re

split_pattern = re.compile(r'[ _-]')


def convert_camel_case_to_snake_case(name: str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_to_snake_case(name: str):
    components = split_pattern.split(name)

    return '_'.join(x.lower() for x in components)


def convert_to_camel_case(name: str):
    components = split_pattern.split(name)

    return ''.join(x.capitalize() for x in components)