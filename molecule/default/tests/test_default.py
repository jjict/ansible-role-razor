import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
    'razor-server',
    'rubygems',
    'ipmitool'
])
def test_installed_pkgs(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('file', [
    'README',
    'SHA256SUM',
    'initrd0.img',
    'vmlinuz0'
])
def test_microkernel_files(host, file):
    file = host.file(
        '/opt/puppetlabs/server/data/razor-server/repo/microkernel/' + file
    )

    assert file.exists
