def test_import(capsys):
    import helloworld
    out, _ = capsys.readouterr()
    assert out == "Hello World from cython!\n"
