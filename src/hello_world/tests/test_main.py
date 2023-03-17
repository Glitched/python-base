from hello_world import main


def test_hello_world_succeeds() -> None:
    """Asserts that we return a fun message."""
    assert main.hello_world() == "Hello, World!"
