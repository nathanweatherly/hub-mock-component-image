import shutil
import os

# all the env vars
_git_repo_base_dir = os.getcwd() # base repo directory
_mch_repo_dir=os.path.join(_git_repo_base_dir, "multiclusterhub")

# clean up old charts if they exist
if os.path.isdir(_mch_repo_dir):
    shutil.rmtree(_mch_repo_dir)


print("Done!")