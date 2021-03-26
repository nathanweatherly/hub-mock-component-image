import shutil
import os

_temp_image_name="hmci:test"

if shutil.which("docker") is None:
    # todo install helm if doesn't exist?
    raise Exception("Docker not installed! Go install Helm 3 CLI!")

print("Did you login to Docker?")

_image_names=["hub-mock-component-image"]

os.system('docker build . -t {}'.format(_temp_image_name))

_res=""

for _in in _image_names:
    _new_image_name = "quay.io/nathanweatherly/{}:mock".format(_in)
    os.system('docker tag {} {}'.format(_temp_image_name, _new_image_name))
    os.system('docker push {}'.format(_new_image_name) )
    _res="{}\n{}".format(_res, _new_image_name)

print ("pushed: {}".format(_res))
