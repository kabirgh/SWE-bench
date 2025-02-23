# Constants - Task Instance Installation Environment
SPECS_RIPGREP = {
    "2576": {
        "docker_specs": {"rust_version": "1.81"},
        "test_cmd": [
            "RUSTFLAGS=-Awarnings cargo test --package ripgrep --test integration -- regression"
        ],
    },
    "2209": {
        "docker_specs": {"rust_version": "1.81"},
        "test_cmd": [
            "RUSTFLAGS=-Awarnings cargo test --package ripgrep --test integration -- regression::r2208 --exact"
        ],
    },
}

MAP_REPO_VERSION_TO_SPECS_RUST = {
    "burntsushi/ripgrep": SPECS_RIPGREP,
}

# Constants - Repository Specific Installation Instructions
MAP_REPO_TO_INSTALL_RUST = {}
