import json
import shutil

import click
from api import generate_api
from schema import generate_pydantic_models
import pathlib
from utils import convert_to_snake_case, convert_camel_case_to_snake_case, convert_to_camel_case


@click.command()
@click.argument("source")
@click.argument("output")
def main(source: str, output: str):
    openapi = {}

    with open(source) as file:
        openapi = json.loads(file.read())

    pathlib.Path(output).mkdir(parents=True, exist_ok=True)

    # Copy base files
    base_dir = pathlib.Path(__file__).parent / 'base'
    output_base_dir = pathlib.Path(output)
    shutil.copytree(base_dir, output_base_dir, dirs_exist_ok=True)

    # Generate API
    pathlib.Path(output, 'api').mkdir(parents=True, exist_ok=True)

    api_endpoints = generate_api(openapi['paths'])

    with open(f"./{output}/api/__init__.py", "w") as file:
        for name in api_endpoints.keys():
            file.write(f"from .{convert_to_snake_case(name)} import {convert_to_camel_case(name)}\n")

    for name, schema in api_endpoints.items():
        with open(f"./{output}/api/{convert_to_snake_case(name)}.py", "w") as file:
            file.write(schema)

    # Generate schemas
    pathlib.Path(output, 'schemas').mkdir(parents=True, exist_ok=True)

    schemas = generate_pydantic_models(openapi['components']['schemas'])

    with open(f"./{output}/schemas/__init__.py", "w") as file:
        for name in schemas.keys():
            file.write(f"from .{convert_camel_case_to_snake_case(name)} import {name}Schema\n")

    for name, schema in schemas.items():
        with open(f"./{output}/schemas/{convert_camel_case_to_snake_case(name)}.py", "w") as file:
            file.write(schema)

    # Finally, insert the api classes into the client:
    client_file = open(base_dir / '__init__.py', 'r')
    client_file_content = client_file.read()
    client_file.close()

    with (open(f"{output}/__init__.py", "w")) as client_file:

        client_file_content = client_file_content.replace(
            "# _imports_",
            f"from .api import {', '.join([convert_to_camel_case(name) for name in api_endpoints.keys()])}\n"
        )

        client_file_content = client_file_content.replace(
            "# _attribute_definitions_",
            "\n    ".join([f"{convert_to_snake_case(name)}: {convert_to_camel_case(name)}" for name in api_endpoints.keys()])
        )

        client_file_content = client_file_content.replace(
            "# _attribute_inits_",
            "\n        ".join([f"self.{convert_to_snake_case(name)} = {convert_to_camel_case(name)}(self.__http_client)" for name in api_endpoints.keys()])
        )



        client_file.write(
            client_file_content
        )


if __name__ == '__main__':
    main()

