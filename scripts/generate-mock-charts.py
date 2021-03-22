import shutil
import os

# make sure helm installed
if shutil.which("helm") is None:
    # TODO install helm if doesn't exist?
    raise Exception("Helm not installed! Go install Helm 3 CLI!")

# all the env vars
_git_repo_base_dir = os.getcwd() # base repo directory
_template_chart_dir=os.path.join(_git_repo_base_dir, "template-chart")
_mch_repo_dir=os.path.join(_git_repo_base_dir, "multiclusterhub")
_mch_repo_charts_dir=os.path.join(_mch_repo_dir, "charts")
_chart_names=["application-chart", "cert-manager-chart", "cert-manager-webhook-chart", "cluster-lifecycle-chart", "configmap-watcher-chart", "console-chart", "grc-chart", "kui-web-terminal-chart", "management-ingress-chart", "search-chart"]
_chart_version="2.3.0"

# clean up old charts if they exist
if os.path.isdir(_mch_repo_dir):
    shutil.rmtree(_mch_repo_dir)

os.mkdir(_mch_repo_dir)  
os.mkdir(_mch_repo_charts_dir)

# copy template chart for all charts, substituting chart names and versions
for _cn in _chart_names:
    _new_chart_destination=os.path.join(_mch_repo_charts_dir, _cn)
    _new_chart_path= shutil.copytree(_template_chart_dir, _new_chart_destination)
    _chart_yaml = os.path.join(_new_chart_path, "Chart.yaml")
    with open(_chart_yaml) as f:
        _chart_yaml_text=f.read()
        _chart_yaml_text= _chart_yaml_text.replace('CHARTNAME', _cn)
        _chart_yaml_text= _chart_yaml_text.replace('CHARTVERSION', _chart_version )
    with open(_chart_yaml, "w") as f:
        f.write(_chart_yaml_text)
    os.system('helm package {}'.format(_new_chart_path))
    os.system('mv {}-{}.tgz {}'.format(_cn, _chart_version, _mch_repo_charts_dir))
    if os.path.isdir(_new_chart_path):
        shutil.rmtree(_new_chart_path)

print("Done!")