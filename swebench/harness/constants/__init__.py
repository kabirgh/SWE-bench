from swebench.harness.constants.constants import *
from swebench.harness.constants.javascript import *
from swebench.harness.constants.php import *
from swebench.harness.constants.python import *
from swebench.harness.constants.rust import *

MAP_REPO_VERSION_TO_SPECS = {
    **MAP_REPO_VERSION_TO_SPECS_JS,
    **MAP_REPO_VERSION_TO_SPECS_PHP,
    **MAP_REPO_VERSION_TO_SPECS_PY,
    **MAP_REPO_VERSION_TO_SPECS_RUST,
}

MAP_REPO_TO_INSTALL = {
    **MAP_REPO_TO_INSTALL_JS,
    **MAP_REPO_TO_INSTALL_PHP,
    **MAP_REPO_TO_INSTALL_PY,
    **MAP_REPO_TO_INSTALL_RUST,
}

MAP_REPO_TO_EXT = {
    **{k: "js" for k in MAP_REPO_VERSION_TO_SPECS_JS.keys()},
    **{k: "php" for k in MAP_REPO_VERSION_TO_SPECS_PHP.keys()},
    **{k: "py" for k in MAP_REPO_VERSION_TO_SPECS_PY.keys()},
    **{k: "rust" for k in MAP_REPO_VERSION_TO_SPECS_RUST.keys()},
}

LATEST = "latest"
USE_X86 = USE_X86_PY
