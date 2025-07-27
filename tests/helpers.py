import sys
from pathlib import Path
from pprint import pprint
from typing import Optional, List
from frictionless import validate


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


def validate_package_print_and_exit(
    descriptor_data: dict, paths_to_delete: Optional[List] = None
) -> None:
    report = validate(descriptor_data)

    # Cleanup
    if paths_to_delete is not None:
        for path in paths_to_delete:
            path.unlink()

    if report.valid:
        print("✔︎ valid package")
        sys.exit(0)
    else:
        print("✕ valid package, errors:")
        if report.errors:
            print("Top-level errors : ")
            for err in report.errors:
                pprint(err)

        for task in report.tasks:
            if len(task.errors) != 0:
                print(f"Errors for resource {task.name}:")

                if len(task.errors) == 1:
                    errors_to_print = [
                        task.error
                    ]  # Weird frictionless API design: must use .error if only one error...
                else:
                    errors_to_print = task.errors

                for task_err in errors_to_print:
                    pprint(task_err)

        sys.exit(1)
