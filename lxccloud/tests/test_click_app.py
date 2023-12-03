from click.testing import CliRunner

from click_app import cli, pdf


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0


def test_pdf():
    runner = CliRunner()
    result = runner.invoke(pdf, ["createpdf", "--dryrun", "0"])
    assert result.exit_code == 0


def test_selftest():
    pass


def test_selfcoverage():
    pass
