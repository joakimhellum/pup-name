import subprocess
import re


def run_cli(args: list[str]) -> str:
    result = subprocess.run(["python", "cli.py"] + args, capture_output=True, text=True)
    return result.stdout.strip()


def test_cli_generate_default():
    output = run_cli(["generate"])
    assert output
    assert "-" in output


def test_cli_generate_with_count():
    output = run_cli(["generate", "--count", "3"])
    lines = output.splitlines()
    assert len(lines) == 3


def test_cli_validate_valid():
    result = run_cli(["validate", "actually-actual-pup"])
    assert result == "Valid"


def test_cli_validate_invalid():
    result = run_cli(["validate", "definitely-not-in-list"])
    assert result == "Invalid"


def test_cli_generate_with_uuid():
    output = run_cli(["generate", "--uuid"])
    parts = output.split("-")
    assert len(parts) == 4  # adjective, noun, uuid4 suffix


def test_cli_separator():
    output = run_cli(["generate", "--words", "2", "--separator", "_"])
    assert "_" in output

