import json
import click
from api import generate_api
from schema import generate_pydantic_models
import pathlib
from utils import convert_to_snake_case, convert_camel_case_to_snake_case


@click.command()
@click.argument("source")
@click.argument("output")
def main(source: str, output: str):
    openapi = {}

    with open(source) as file:
        openapi = json.loads(file.read())

    pathlib.Path(output).mkdir(parents=True, exist_ok=True)

    pathlib.Path(output, 'api').mkdir(parents=True, exist_ok=True)

    api_endpoints = generate_api(openapi['paths'])

    for name, schema in api_endpoints.items():
        with open(f"./{output}/api/{convert_to_snake_case(name)}.py", "w") as file:
            file.write(schema)

    # pathlib.Path(output, 'schemas').mkdir(parents=True, exist_ok=True)
    #
    # schemas = generate_pydantic_models(openapi['components']['schemas'])
    #
    # for name, schema in schemas.items():
    #     with open(f"./{output}/schemas/{convert_camel_case_to_snake_case(name)}.py", "w") as file:
    #         file.write(schema)
    #
    # print(schemas)

if __name__ == '__main__':
    main()

