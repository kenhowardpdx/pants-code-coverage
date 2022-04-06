from other.main import swoosh

def test_swoosh(capsys):
    swoosh()

    out, err = capsys.readouterr()

    assert "swoosh" in out
