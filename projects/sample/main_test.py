def test_main(capsys):
    from sample.main import main

    assert main() == 0

    out, err = capsys.readouterr()

    assert out.startswith("Hello, World!")


