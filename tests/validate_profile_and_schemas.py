# This script validates the GeoLocator-DP standard itself is valid (regarding JSON and Frictionless definitions)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional
from frictionless import Schema

THIS_SCRIPT_PATH = Path(__file__).parent
REPOSITORY_ROOT_PATH = THIS_SCRIPT_PATH / ".."
PROFILE_PATH = REPOSITORY_ROOT_PATH / "geolocator-dp-profile.json"
TABLE_SCHEMA_PATHS = [
    REPOSITORY_ROOT_PATH / "observations-table-schema.json",
    REPOSITORY_ROOT_PATH / "tags-table-schema.json",
    REPOSITORY_ROOT_PATH / "measurements-table-schema.json",
    REPOSITORY_ROOT_PATH / "staps-table-schema.json",
    REPOSITORY_ROOT_PATH / "twilights-table-schema.json",
    REPOSITORY_ROOT_PATH / "paths-table-schema.json",
    REPOSITORY_ROOT_PATH / "edges-table-schema.json",
    REPOSITORY_ROOT_PATH / "pressurepaths-table-schema.json",
]

EXPECTED_SCHEMA_RESOURCES = {
    "tags",
    "observations",
    "measurements",
    "staps",
    "twilights",
    "paths",
    "edges",
    "pressurepaths",
}

def load_json(filepath: Path) -> Optional[dict]:
    with open(filepath) as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return None


def validate_schema(file_path: Path) -> bool:
    report = Schema.validate_descriptor(descriptor=file_path)
    return report.valid


def get_schema_metadata_error_messages(file_path: Path) -> List[str]:
    """Return a list of error messages for the table schema at file_path

    Undefined behavior if the table schema is valid
    """
    report = Schema.validate_descriptor(descriptor=file_path)
    return [err.message for err in report.errors]


def _listify_fields(fields) -> List[str]:
    if isinstance(fields, str):
        return [fields]
    if isinstance(fields, list):
        return [field for field in fields if isinstance(field, str)]
    return []


def _get_schema_fields(descriptor: dict) -> set:
    fields = descriptor.get("fields", [])
    return {
        field.get("name")
        for field in fields
        if isinstance(field, dict) and isinstance(field.get("name"), str)
    }


def check_schema_coherence(schema_descriptors: Dict[Path, dict]) -> bool:
    encountered_errors = False
    resource_to_paths: Dict[str, List[Path]] = {}

    # 1) filename <-> schema name consistency
    for schema_path, descriptor in schema_descriptors.items():
        schema_name = descriptor.get("name")
        expected_name = schema_path.name.replace("-table-schema.json", "")

        if not isinstance(schema_name, str):
            print(f"✕ {schema_path.name}: missing or non-string `name`")
            encountered_errors = True
            continue

        resource_to_paths.setdefault(schema_name, []).append(schema_path)

        if schema_name != expected_name:
            print(
                f"✕ {schema_path.name}: schema `name` is `{schema_name}` but expected `{expected_name}`"
            )
            encountered_errors = True

    # 2) expected resources exist exactly once
    observed_resources = set(resource_to_paths.keys())
    missing_resources = sorted(EXPECTED_SCHEMA_RESOURCES - observed_resources)
    unexpected_resources = sorted(observed_resources - EXPECTED_SCHEMA_RESOURCES)

    for resource in missing_resources:
        print(f"✕ schema resources: missing expected resource `{resource}`")
        encountered_errors = True

    for resource in unexpected_resources:
        print(f"✕ schema resources: unexpected resource `{resource}`")
        encountered_errors = True

    for resource, paths in sorted(resource_to_paths.items()):
        if len(paths) > 1:
            path_list = ", ".join(path.name for path in paths)
            print(
                f"✕ schema resources: resource `{resource}` is defined more than once ({path_list})"
            )
            encountered_errors = True

    # 3) foreign keys reference existing resources and target fields
    fields_by_resource: Dict[str, set] = {}
    for resource, paths in resource_to_paths.items():
        if len(paths) == 1:
            fields_by_resource[resource] = _get_schema_fields(schema_descriptors[paths[0]])

    for schema_path, descriptor in schema_descriptors.items():
        foreign_keys = descriptor.get("foreignKeys", [])
        if not isinstance(foreign_keys, list):
            continue

        for foreign_key in foreign_keys:
            if not isinstance(foreign_key, dict):
                continue

            reference = foreign_key.get("reference", {})
            if not isinstance(reference, dict):
                print(f"✕ {schema_path.name}: malformed foreign key reference")
                encountered_errors = True
                continue

            target_resource = reference.get("resource")
            target_fields = _listify_fields(reference.get("fields"))

            if not isinstance(target_resource, str):
                print(f"✕ {schema_path.name}: foreign key reference missing `resource`")
                encountered_errors = True
                continue

            if target_resource not in resource_to_paths:
                print(
                    f"✕ {schema_path.name}: foreign key references unknown resource `{target_resource}`"
                )
                encountered_errors = True
                continue

            target_resource_fields = fields_by_resource.get(target_resource, set())
            missing_target_fields = [
                field for field in target_fields if field not in target_resource_fields
            ]

            if missing_target_fields:
                fields_str = ", ".join(missing_target_fields)
                print(
                    f"✕ {schema_path.name}: foreign key references missing field(s) in `{target_resource}`: {fields_str}"
                )
                encountered_errors = True

    return not encountered_errors


if __name__ == "__main__":
    encountered_errors = False
    schema_descriptors: Dict[Path, dict] = {}

    print(PROFILE_PATH.name)
    profile_json = load_json(PROFILE_PATH)
    if profile_json is not None:
        print("✔︎ valid JSON")
    else:
        print("✕ valid JSON")
        encountered_errors = True

    for table_schema in TABLE_SCHEMA_PATHS:
        print(f"\n{table_schema.name}")

        schema_json = load_json(table_schema)
        if schema_json is not None:
            schema_descriptors[table_schema] = schema_json
            print("✔︎ valid JSON")
            if validate_schema(table_schema):
                print("✔︎ valid Table Schema")
            else:
                print("✕ valid Table Schema, errors:")
                for err in get_schema_metadata_error_messages(table_schema):
                    print(f"\t - {err}")
                encountered_errors = True
        else:
            print("✕ valid JSON")
            encountered_errors = True

    print("\nSchema coherence")
    if check_schema_coherence(schema_descriptors):
        print("✔︎ schema coherence checks passed")
    else:
        encountered_errors = True

    if encountered_errors:
        print("Errors were encountered")
        sys.exit(1)
    else:
        print("\nAll good!")
        sys.exit(0)
