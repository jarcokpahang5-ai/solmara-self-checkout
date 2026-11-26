"""The Self-Checkout Is Judging You — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "The self-checkout scanned my 2 a.m. ice cream and sighed, \"Unexpected item in bagging area — your life choices, however, were fully expected.\""


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()
