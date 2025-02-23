from swebench.harness.log_parsers.javascript import MAP_REPO_TO_PARSER_JS
from swebench.harness.log_parsers.php import MAP_REPO_TO_PARSER_PHP
from swebench.harness.log_parsers.python import MAP_REPO_TO_PARSER_PY
from swebench.harness.log_parsers.rust import MAP_REPO_TO_PARSER_RUST
from swebench.harness.log_parsers.utils import get_eval_type

MAP_REPO_TO_PARSER = {
    **MAP_REPO_TO_PARSER_JS,
    **MAP_REPO_TO_PARSER_PHP,
    **MAP_REPO_TO_PARSER_PY,
    **MAP_REPO_TO_PARSER_RUST,
}
