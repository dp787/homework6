import os
import pytest
from app import App

@pytest.fixture
def app_instance():
    return App()

def test_configure_logging(app_instance, caplog):
    app_instance.configure_logging()
    assert "Logging configured." in caplog.text

def test_load_environment_variables(app_instance, monkeypatch):
    monkeypatch.setenv("TEST_ENV_VAR", "test_value")
    settings = app_instance.load_environment_variables()
    assert settings.get("TEST_ENV_VAR") == "test_value"

def test_get_environment_variable(app_instance, monkeypatch):
    monkeypatch.setenv("TEST_ENV_VAR", "test_value")
    assert app_instance.get_environment_variable("TEST_ENV_VAR") == "test_value"
    assert app_instance.get_environment_variable("NON_EXISTING_VAR") is None

def test_load_plugins(app_instance, caplog):
    app_instance.load_plugins()
    assert "Plugins directory 'app/plugins' not found." in caplog.text

def test_register_plugin_commands(app_instance, caplog, monkeypatch):
    # Assuming the GreetCommand is placed in the 'app.plugins' package
    monkeypatch.syspath_prepend(os.path.join(os.getcwd(), 'app'))
    from app.plugins.test_greet_plugin import TestGreetCommand

    app_instance.register_plugin_commands(TestGreetCommand, 'test_greet_plugin')
    assert "Command 'test_greet_plugin' from plugin 'test_greet_plugin' registered." in caplog.text

def test_start_exit_command(app_instance, capsys):
    with pytest.raises(SystemExit) as ex:
        app_instance.start()
    assert ex.value.code == 0
    captured = capsys.readouterr()
    assert "Application exit." in captured.out

def test_start_unknown_command(app_instance, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'unknown_command')
    with pytest.raises(SystemExit) as ex:
        app_instance.start()
    assert ex.value.code == 1
    captured = capsys.readouterr()
    assert "Unknown command: unknown_command" in captured.err

def test_start_keyboard_interrupt(app_instance, capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: KeyboardInterrupt)
    with pytest.raises(SystemExit) as ex:
        app_instance.start()
    assert ex.value.code == 0
    captured = capsys.readouterr()
    assert "Application interrupted and exiting gracefully." in captured.out
