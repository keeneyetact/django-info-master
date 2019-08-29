import os.path
import json


def get_project_info_dict(version_config=None):
    if version_config is None:
        from django.conf import settings

        version_config = settings.VERSION_CONFIG


    print(version_config)

    if os.path.isfile(version_config):
        with open(version_config) as f:
            return json.load(f)
    else:
        return {}


def get_version(version_config=None):
    return get_project_info_dict(version_config).get('version')
