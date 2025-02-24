import re


def ansi_escape(text: str) -> str:
    """
    Remove ANSI escape sequences from text
    """
    pattern = re.compile(
        r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])",
        re.VERBOSE,
    )
    return pattern.sub("", text)
