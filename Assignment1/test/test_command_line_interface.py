import pytest

@pytest.fixture
def cli():
    from Assignment1.command_line_interface import CommandLineInterface
    return CommandLineInterface()


def test_hello_world(cli):
    assert cli.hello_world() == "hello world"
