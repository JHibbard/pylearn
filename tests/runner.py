# External Libraries
from click.testing import CliRunner

# Internal Libraries
from pylearn.runner import hello


def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert result.output == 'Hello World!\n'
