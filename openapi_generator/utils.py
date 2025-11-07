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


def resolve_type(type_object: dict[str, str | dict]):
    if '$ref' in type_object.keys():
        return type_object['$ref'].split('/')[-1] + "Schema"

    match type_object.get('type'):
        case "string":
            return "str"
        case "integer":
            return "int"
        case "number":
            return "float"
        case "boolean":
            return "bool"
        case "bool":
            return "bool"
        case "array":
            if 'items' not in type_object.keys():
                return "list"

            if '$ref' in type_object['items'].keys():
                return type_object['items']['$ref'].split('/')[-1] + "Schema"
        case _ as test:
            return "Any"