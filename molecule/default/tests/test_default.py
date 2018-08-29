import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repo_package(host):
    pkg = host.package('mysql80-community-release')

    assert pkg.is_installed
