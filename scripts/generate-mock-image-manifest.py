import shutil
import os
import json
from check_env_vars import _product_version, _image_remote, _image_name, _image_tag

_full_image = "{}/{}:{}".format(_image_remote, _image_remote, _image_tag)

_image_keys = ["multicloud_manager", "work", "registration", "multiclusterhub_repo", "hub_mock_component_image"]

_git_repo_base_dir = os.getcwd() # base repo directory
_results_dir = os.path.join(_git_repo_base_dir, "results")

if not os.path.isdir(_results_dir):
    os.mkdir(_results_dir)

_new_image_man_destination = os.path.join(_results_dir, "{}.json".format(_product_version))

with open(_new_image_man_destination, 'a') as f:
    _manifest_python = []
    for _ik in _image_keys:
        _entry = {
            "image-name": _image_name,
            "image-remote": _image_remote,
            "image-tag": _image_tag,
            "image-key": _ik
        }
        _manifest_python.append(_entry)
    _manifest_json = json.dumps(_manifest_python, sort_keys=True, indent=4)

with open(_new_image_man_destination, "w") as f:
    f.write(_manifest_json)