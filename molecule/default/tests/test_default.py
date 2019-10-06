import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_service_enabled(host):
    service = host.service('docker')
    assert service.is_enabled


def test_docker_service_running(host):
    service = host.service('docker')
    assert service.is_running


@pytest.mark.parametrize('socket_def', [
    # all IPv4 tcp sockets on port 8883 (MQQTS)
    ('tcp://8883'),
])
def test_listening_sockets(host, socket_def):
    socket = host.socket(socket_def)
    assert socket.is_listening


# Tests to write:
# - using the localhost listener:
#    - verify that a message can be published
#    - verify that a published message can be subscribed to
