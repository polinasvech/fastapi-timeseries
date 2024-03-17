from fastapi.openapi.utils import get_openapi
from app.main import app
import json
import yaml


def export_schema():
    api_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )
    with open("api_schema.json", "w") as file:
        json.dump(api_schema, file)

    with open("api_schema.yaml", "w") as file:
        yaml.dump(api_schema, file, default_flow_style=False)


export_schema()
