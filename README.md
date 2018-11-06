# MySQL Community Repo Ansible Role

This role provides support for the MySQL Community repository.

## Requirements

* Ansible 2.4+

## Role Variables

``` yaml
# Valid values are "8.0" or "5.7"
mysql_community_repo_version: "8.0"
```

## Dependencies

None.

## Example Playbook

``` yaml
- hosts: localhost
  roles:
    - rchouinard.repo-mysql-community
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
