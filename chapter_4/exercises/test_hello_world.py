import hello_world


def test_hello_v1():
    hello_world.hello()
    with open('hello.txt', 'r') as f:
        f = f.read()
    assert f == 'Hello World!\n'


def test_hello_v2(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    hello_full_dir = tmp_path / 'hello.txt'
    print(hello_full_dir)

    hello_world.hello()
    with open(hello_full_dir, 'r') as f:
        f = f.read()
    assert f == 'Hello World!\n'
