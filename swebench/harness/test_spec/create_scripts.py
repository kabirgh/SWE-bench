from swebench.harness.test_spec.javascript import (
    make_repo_script_list_js,
    make_env_script_list_js,
    make_eval_script_list_js,
)
from swebench.harness.test_spec.php import (
    make_repo_script_list_php,
    make_env_script_list_php,
    make_eval_script_list_php,
)
from swebench.harness.test_spec.python import (
    make_repo_script_list_py,
    make_env_script_list_py,
    make_eval_script_list_py,
)
from swebench.harness.test_spec.rust import (
    make_env_script_list_rust,
    make_eval_script_list_rust,
    make_repo_script_list_rust,
)
from swebench.harness.constants import MAP_REPO_TO_EXT


def make_repo_script_list(specs, repo, repo_directory, base_commit, env_name) -> list:
    """
    Create a list of bash commands to set up the repository for testing.
    This is the setup script for the instance image.
    """
    ext = MAP_REPO_TO_EXT[repo]
    func = {
        "js": make_repo_script_list_js,
        "php": make_repo_script_list_php,
        "py": make_repo_script_list_py,
        "rs": make_repo_script_list_rust,
    }[ext]
    return func(specs, repo, repo_directory, base_commit, env_name)


def make_env_script_list(instance, specs, env_name) -> list:
    """
    Creates the list of commands to set up the environment for testing.
    This is the setup script for the environment image.
    """
    ext = MAP_REPO_TO_EXT[instance["repo"]]
    func = {
        "js": make_env_script_list_js,
        "php": make_env_script_list_php,
        "py": make_env_script_list_py,
        "rs": make_env_script_list_rust,
    }[ext]
    return func(instance, specs, env_name)


def make_eval_script_list(
    instance, specs, env_name, repo_directory, base_commit, test_patch
) -> list:
    """
    Applies the test patch and runs the tests.
    """
    ext = MAP_REPO_TO_EXT[instance["repo"]]
    func = {
        "js": make_eval_script_list_js,
        "php": make_eval_script_list_php,
        "py": make_eval_script_list_py,
        "rs": make_eval_script_list_rust,
    }[ext]
    return func(instance, specs, env_name, repo_directory, base_commit, test_patch)
