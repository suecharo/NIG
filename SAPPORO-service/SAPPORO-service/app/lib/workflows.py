# coding: utf-8
from pathlib import Path

from .util import WORKFLOW_INFO_FILE_PATH, read_workflow_info


def read_workflow_setting_file():
    workflow_info = read_workflow_info()
    data = dict()
    data["workflows"] = []
    for workflow in workflow_info["workflows"]:
        location = resolve_workflow_file_path(workflow["location"])
        if location is None:
            continue
        del workflow["location"]
        with location.open(mode="r") as f:
            workflow["content"] = f.read()
        data["workflows"].append(workflow)

    return data


def resolve_workflow_file_path(location):
    if location[0] == "/":
        path = Path(location)
    elif location[0] == ".":
        path = WORKFLOW_INFO_FILE_PATH.parent.joinpath(location).absolute()
    else:
        path = WORKFLOW_INFO_FILE_PATH.parent.joinpath(location).absolute()
    if path.exists() is False:
        return None

    return path
