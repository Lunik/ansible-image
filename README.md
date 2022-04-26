# Ansible image

[![Build](https://github.com/Lunik/ansible-image/actions/workflows/build.yml/badge.svg)][github-action-build]
[![Docker Pulls](https://img.shields.io/docker/pulls/lunik/ansible)][docker-image]
[![Docker Stars](https://img.shields.io/docker/stars/lunik/ansible)][docker-image]
[![Latest version](https://img.shields.io/github/v/tag/Lunik/ansible-image?sort=semver)][docker-image]

Base image for using Ansible in CI/CD pipelines
Supported architectures: amd64, arm/v7, arm64/v8

## Simple Tags

- [`5.7.0`][version-5-sources], [`5.7`][version-5-sources], [`5`][version-5-sources], [`latest`][version-5-sources]
- [`5.7.0-alpine3.15`][version-5-sources], [`5.7-alpine3.15`][version-5-sources], [`5-alpine3.15`][version-5-sources], [`alpine`][version-5-sources]
- [`5.7.0-slim-bullseye`][version-5-sources], [`5.7-slim-bullseye`][version-5-sources], [`5-slim-bullseye`][version-5-sources], [`slim-bullseye`][version-5-sources], [`debian`][version-5-sources]
- [`4.10.0`][version-4-sources], [`4.10`][version-4-sources], [`4`][version-4-sources]
- [`4.10.0-alpine3.15`][version-4-sources], [`4.10-alpine3.15`][version-4-sources], [`4-alpine3.15`][version-4-sources], [`alpine`][version-4-sources]
- [`4.10.0-slim-bullseye`][version-4-sources], [`4.10-slim-bullseye`][version-4-sources], [`4-slim-bullseye`][version-4-sources], [`slim-bullseye`][version-4-sources]

### Shared tags

- `5.7.0`, `5.7`, `5`, `latest`, `alpine`
  - `5.7.0-alpine3.15`

- `debian`
  - `5.7.0-slim-bullseye`

- `4.10.0`, `4.10`, `4`
  - `4.10.0-alpine3.15`

## Supported tags and respective Dockerfile links

(See "[What's the difference between 'Shared' and 'Simple' tags?][faq-shared-simple-tags]" in the FAQ.)

## How to use this image

### With Docker

```shell
docker pull Lunik/ansible

docker run \
  -it --rm \
  Lunik/ansible \
  --volume .:/opt/ansible \
  -- \
  ansible-playbook playbook.yml
```

## Reference

- Maintained by: [Lunik][lunik-github]
- [Ansible release cycles][ansible-release-cycle]

<!-- Links -->

[this]: https://github.com/Lunik/ansible-image
[docker-image]: https://hub.docker.com/r/lunik/ansible
[lunik-github]: https://github.com/Lunik
[github-action-build]: https://github.com/Lunik/ansible-image/actions/workflows/build.yml
[faq-shared-simple-tags]: https://github.com/docker-library/faq#whats-the-difference-between-shared-and-simple-tags
[version-5-sources]: https://github.com/Lunik/ansible-image/tree/master/templates
[version-4-sources]: https://github.com/Lunik/ansible-image/tree/master/templates
[ansible-release-cycle]: https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html
