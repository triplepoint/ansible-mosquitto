from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_service_enabled(Service):
    service = Service('mosquitto')
    assert service.is_enabled


def test_service_running(Service):
    service = Service('mosquitto')
    assert service.is_running


def test_socket_listening_ipv4_1883(Socket):
    socket = Socket('tcp://0.0.0.0:1883')
    assert socket.is_listening


def test_socket_listening_ipv4_9001(Socket):
    socket = Socket('tcp://0.0.0.0:9001')
    assert socket.is_listening


def test_socket_listening_ipv6_1883(Socket):
    socket = Socket('tcp://:::1883')
    assert socket.is_listening


def test_socket_listening_ipv6_9001(Socket):
    socket = Socket('tcp://:::9001')
    assert socket.is_listening
