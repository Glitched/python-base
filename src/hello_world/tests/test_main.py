from hello_world import main


def test_hello_world_succeeds():
    assert main.hello_world() == "Hello, World!"
