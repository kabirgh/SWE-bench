from swebench.harness.dockerfiles.javascript import (
    _DOCKERFILE_BASE_JS,
    _DOCKERFILE_ENV_JS,
    _DOCKERFILE_INSTANCE_JS,
)

from swebench.harness.dockerfiles.python import (
    _DOCKERFILE_BASE_PY,
    _DOCKERFILE_ENV_PY,
    _DOCKERFILE_INSTANCE_PY,
)

from swebench.harness.dockerfiles.php import (
    _DOCKERFILE_BASE_PHP,
    _DOCKERFILE_INSTANCE_PHP,
)

from swebench.harness.dockerfiles.rust import (
    _DOCKERFILE_BASE_RUST,
    _DOCKERFILE_INSTANCE_RUST,
)

_DOCKERFILE_BASE = {
    "py": _DOCKERFILE_BASE_PY,
    "js": _DOCKERFILE_BASE_JS,
    "php": _DOCKERFILE_BASE_PHP,
    "rust": _DOCKERFILE_BASE_RUST,
}

_DOCKERFILE_ENV = {
    "py": _DOCKERFILE_ENV_PY,
    "js": _DOCKERFILE_ENV_JS,
}

_DOCKERFILE_INSTANCE = {
    "py": _DOCKERFILE_INSTANCE_PY,
    "js": _DOCKERFILE_INSTANCE_JS,
    "php": _DOCKERFILE_INSTANCE_PHP,
    "rust": _DOCKERFILE_INSTANCE_RUST,
}


def get_dockerfile_base(platform, arch, language, **kwargs):
    if arch == "arm64":
        conda_arch = "aarch64"
    else:
        conda_arch = arch
    return _DOCKERFILE_BASE[language].format(
        platform=platform, conda_arch=conda_arch, **kwargs
    )


def get_dockerfile_env(platform, arch, language, base_image_key, **kwargs):
    # Some languages do not have an environment Dockerfile. In those cases, the
    # base Dockerfile is used as the environment Dockerfile.
    dockerfile = _DOCKERFILE_ENV.get(language, _DOCKERFILE_BASE[language])
    return dockerfile.format(
        platform=platform, arch=arch, base_image_key=base_image_key, **kwargs
    )


def get_dockerfile_instance(platform, language, env_image_name):
    return _DOCKERFILE_INSTANCE[language].format(
        platform=platform, env_image_name=env_image_name
    )
