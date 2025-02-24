import json
import re

from pathlib import Path
from swebench.harness.constants import (
    END_TEST_OUTPUT,
    START_TEST_OUTPUT,
)
from swebench.harness.test_spec.utils import (
    make_env_script_list_common,
    make_eval_script_list_common,
    make_repo_script_list_common,
)
from unidiff import PatchSet


# Constants - Commonly Used Commands
TEST_XVFB_PREFIX = 'xvfb-run --server-args="-screen 0 1280x1024x24 -ac :99"'
XVFB_DEPS = [
    "python3",
    "python3-pip",
    "xvfb",
    "x11-xkb-utils",
    "xfonts-100dpi",
    "xfonts-75dpi",
    "xfonts-scalable",
    "xfonts-cyrillic",
    "x11-apps",
    "firefox",
]
X11_DEPS = [
    "libx11-xcb1",
    "libxcomposite1",
    "libxcursor1",
    "libxdamage1",
    "libxi6",
    "libxtst6",
    "libnss3",
    "libcups2",
    "libxss1",
    "libxrandr2",
    "libasound2",
    "libatk1.0-0",
    "libgtk-3-0",
    "x11-utils",
]

# Constants - Task Instance Installation Environment
SPECS_CALYPSO = {
    **{
        k: {
            "apt-pkgs": ["libsass-dev", "sassc"],
            "install": ["npm install --unsafe-perm"],
            "test_cmd": "npm run test-client",
            "docker_specs": {
                "node_version": k,
            },
        }
        for k in [
            "0.8",
            "4.2.3",
            "4.3.0",
            "5.10.1",
            "5.11.1",
            "6.1.0",
            "6.7.0",
            "6.9.0",
            "6.9.1",
            "6.9.4",
            "6.10.0",
            "6.10.2",
            "6.10.3",
            "6.11.1",
            "6.11.2",
            "6.11.5",
            "8.9.1",
            "8.9.3",
            "8.9.4",
            "8.11.0",
            "8.11.2",
            "10.4.1",
            "10.5.0",
            "10.6.0",
            "10.9.0",
            "10.10.0",
            "10.12.0",
            "10.13.0",
            "10.14.0",
            "10.15.2",
            "10.16.3",
        ]
    }
}

TEST_CHART_JS_TEMPLATE = "./node_modules/.bin/cross-env NODE_ENV=test ./node_modules/.bin/karma start {} --single-run --coverage --grep --auto-watch false"
SPECS_CHART_JS = {
    **{
        k: {
            "install": [
                "pnpm install",
                "pnpm run build",
            ],
            "test_cmd": [
                "pnpm install",
                "pnpm run build",
                f'{TEST_XVFB_PREFIX} su chromeuser -c "{TEST_CHART_JS_TEMPLATE.format("./karma.conf.cjs")}"',
            ],
            "docker_specs": {
                "node_version": "21.6.2",
                "pnpm_version": "7.9.0",
                "run_args": {
                    "cap_add": ["SYS_ADMIN"],
                },
            },
        }
        for k in ["4.0", "4.1", "4.2", "4.3", "4.4"]
    },
    **{
        k: {
            "install": ["npm install"],
            "test_cmd": [
                "npm install",
                "npm run build",
                f'{TEST_XVFB_PREFIX} su chromeuser -c "{TEST_CHART_JS_TEMPLATE.format("./karma.conf.js")}"',
            ],
            "docker_specs": {
                "node_version": "21.6.2",
                "run_args": {
                    "cap_add": ["SYS_ADMIN"],
                },
            },
        }
        for k in ["3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8"]
    },
    **{
        k: {
            "install": ["npm install", "npm install -g gulp-cli"],
            "test_cmd": [
                "npm install",
                "gulp build",
                TEST_XVFB_PREFIX + ' su chromeuser -c "gulp test"',
            ],
            "docker_specs": {
                "node_version": "21.6.2",
                "run_args": {
                    "cap_add": ["SYS_ADMIN"],
                },
            },
        }
        for k in ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9"]
    },
}
for v in SPECS_CHART_JS.keys():
    SPECS_CHART_JS[v]["apt-pkgs"] = XVFB_DEPS

SPECS_MARKED = {
    **{
        k: {
            "install": ["npm install"],
            "test_cmd": "./node_modules/.bin/jasmine --no-color --config=jasmine.json",
            "docker_specs": {
                "node_version": "12.22.12",
            },
        }
        for k in [
            "0.3",
            "0.5",
            "0.6",
            "0.7",
            "1.0",
            "1.1",
            "1.2",
            "2.0",
            "3.9",
            "4.0",
            "4.1",
            "5.0",
        ]
    }
}
for v in ["4.0", "4.1", "5.0"]:
    SPECS_MARKED[v]["docker_specs"]["node_version"] = "20.16.0"

SPECS_P5_JS = {
    **{
        k: {
            "apt-pkgs": X11_DEPS,
            "install": [
                "npm install",
                "PUPPETEER_SKIP_CHROMIUM_DOWNLOAD='' node node_modules/puppeteer/install.js",
                "./node_modules/.bin/grunt yui",
            ],
            "test_cmd": (
                """sed -i 's/concurrency:[[:space:]]*[0-9][0-9]*/concurrency: 1/g' Gruntfile.js\n"""
                "stdbuf -o 1M ./node_modules/.bin/grunt test --quiet --force"
            ),
            "docker_specs": {
                "node_version": "14.17.3",
            },
        }
        for k in [
            "0.10",
            "0.2",
            "0.4",
            "0.5",
            "0.6",
            "0.7",
            "0.8",
            "0.9",
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "1.5",
            "1.6",
            "1.7",
            "1.8",
            "1.9",
        ]
    },
}
for k in [
    "0.4",
    "0.5",
    "0.6",
]:
    SPECS_P5_JS[k]["install"] = [
        "npm install",
        "./node_modules/.bin/grunt yui",
    ]

SPECS_REACT_PDF = {
    **{
        k: {
            "apt-pkgs": [
                "pkg-config",
                "build-essential",
                "libpixman-1-0",
                "libpixman-1-dev",
                "libcairo2-dev",
                "libpango1.0-dev",
                "libjpeg-dev",
                "libgif-dev",
                "librsvg2-dev",
            ]
            + X11_DEPS,
            "install": ["npm i -g yarn", "yarn install"],
            "test_cmd": 'NODE_OPTIONS="--experimental-vm-modules" ./node_modules/.bin/jest --no-color',
            "docker_specs": {"node_version": "18.20.4"},
        }
        for k in ["1.0", "1.1", "1.2", "2.0"]
    }
}
for v in ["1.0", "1.1", "1.2"]:
    SPECS_REACT_PDF[v]["docker_specs"]["node_version"] = "8.17.0"
    SPECS_REACT_PDF[v]["install"] = ["npm install", "npm install cheerio@1.0.0-rc.3"]
    SPECS_REACT_PDF[v]["test_cmd"] = "./node_modules/.bin/jest --no-color"

MAP_REPO_VERSION_TO_SPECS_JS = {
    "Automattic/wp-calypso": SPECS_CALYPSO,
    "chartjs/Chart.js": SPECS_CHART_JS,
    "markedjs/marked": SPECS_MARKED,
    "processing/p5.js": SPECS_P5_JS,
    "diegomura/react-pdf": SPECS_REACT_PDF,
}

# Constants - Repository Specific Installation Instructions
MAP_REPO_TO_INSTALL_JS = {}



# MARK: Test Command Creation Functions
def get_test_cmds_calypso(instance) -> list:
    test_paths = [x.path for x in PatchSet(instance["test_patch"])]
    test_cmds = []
    for test_path in test_paths:
        if re.search(r"__snapshots__/(.*).js.snap$", test_path):
            # Jest snapshots are not run directly
            test_path = "/".join(test_path.split("/")[:-2])

        # Determine which testing script to use
        if any([test_path.startswith(x) for x in ["client", "packages"]]):
            pkg = test_path.split("/")[0]
            if instance["version"] in [
                "10.10.0",
                "10.12.0",
                "10.13.0",
                "10.14.0",
                "10.15.2",
                "10.16.3",
            ]:
                test_cmds.append(
                    f"./node_modules/.bin/jest --verbose -c=test/{pkg}/jest.config.js '{test_path}'"
                )
            elif instance["version"] in [
                "6.11.5",
                "8.9.1",
                "8.9.3",
                "8.9.4",
                "8.11.0",
                "8.11.2",
                "10.4.1",
                "10.5.0",
                "10.6.0",
                "10.9.0",
            ]:
                test_cmds.append(
                    f"./node_modules/.bin/jest --verbose -c=test/{pkg}/jest.config.json '{test_path}'"
                )
            else:
                test_cmds.append(f"npm run test-{pkg} --verbose '{test_path}'")
        elif any([test_path.startswith(x) for x in ["test/e2e"]]):
            test_cmds.extend(
                [
                    "cd test/e2e",
                    f"NODE_CONFIG_ENV=test npm run test {test_path}",
                    "cd ../..",
                ]
            )

    return test_cmds


MAP_REPO_TO_TEST_CMDS = {
    "Automattic/wp-calypso": get_test_cmds_calypso,
}

# MARK: Utility Functions


def get_download_img_commands(instance) -> list:
    cmds = []
    image_assets = {}
    if "image_assets" in instance:
        if isinstance(instance["image_assets"], str):
            image_assets = json.loads(instance["image_assets"])
        else:
            image_assets = instance["image_assets"]
    for i in image_assets.get("test_patch", []):
        folder = Path(i["path"]).parent
        cmds.append(f"mkdir -p {folder}")
        cmds.append(f"curl -o {i['path']} {i['url']}")
        cmds.append(f"chmod 777 {i['path']}")
    return cmds


# MARK: Script Creation Functions


def make_repo_script_list_js(
    specs, repo, repo_directory, base_commit, env_name
) -> list:
    return make_repo_script_list_common(
        specs, repo, repo_directory, base_commit, env_name
    )


def make_env_script_list_js(instance, specs, env_name) -> list:
    """
    Creates the list of commands to set up the environment for testing.
    This is the setup script for the environment image.
    """
    return make_env_script_list_common(instance, specs, env_name)


def make_eval_script_list_js(
    instance, specs, env_name, repo_directory, base_commit, test_patch
) -> list:
    """
    Applies the test patch and runs the tests.
    """
    eval_commands = make_eval_script_list_common(
        instance, specs, env_name, repo_directory, base_commit, test_patch
    )
    # Insert downloading right after reset command
    eval_commands[4:4] = get_download_img_commands(instance)
    if instance["repo"] in MAP_REPO_TO_TEST_CMDS:
        # Update test commands if they are custom
        test_commands = MAP_REPO_TO_TEST_CMDS[instance["repo"]](instance)
        idx_start_test_out = eval_commands.index(f": '{START_TEST_OUTPUT}'")
        idx_end_test_out = eval_commands.index(f": '{END_TEST_OUTPUT}'")
        eval_commands[idx_start_test_out + 1 : idx_end_test_out] = test_commands
    return eval_commands
