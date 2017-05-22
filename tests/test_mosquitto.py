import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_service_enabled(Service):
    service = Service('mosquitto')
    assert service.is_enabled


def test_service_running(Service):
    service = Service('mosquitto')
    assert service.is_running


@pytest.mark.parametrize("socket_def", [
    ('tcp://0.0.0.0:1883'),
    ('tcp://0.0.0.0:9001'),
    ('tcp://:::1883'),
    ('tcp://:::9001'),
])
def test_listening_sockets(Socket, socket_def):
    socket = Socket(socket_def)
    assert socket.is_listening
