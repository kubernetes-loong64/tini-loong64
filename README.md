# Tini for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/Tini%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=docker&logoColor=white" alt="Tini LoongArch64 龙芯架构发行版"></p>

Build [Tini](https://github.com/krallin/tini) — a tiny but valid `init` for containers — for the **LoongArch64 (loong64)
** architecture via CI/CD.

## How it works

A GitHub Actions workflow clones the specified krallin/tini version, cross-compiles with a
loongarch64 toolchain in a Debian 13 container, and produces a statically-linked `tini-static`
binary. Target platform: `linux/loong64`.

Tini acts as a proper PID 1 inside containers: it reaps zombie processes, forwards signals to
child processes, and exits when its child exits.

See [Discussion #6 — Why Use container: debian:13?](https://github.com/orgs/kubernetes-loong64/discussions/6) for the
rationale behind the Debian 13 container choice.

## Branch naming

Push a branch named `loong64-<version>` (e.g. `loong64-master`) to trigger a build. Append
`+<build>` (e.g. `loong64-master+0`) to include build metadata.

## [Release](https://github.com/kubernetes-loong64/tini-loong64/releases)

Push a tag matching `release-loong64-<version>` (e.g. `release-loong64-master+0`) to publish
a GitHub Release with the built binary.

The `+<build>` suffix provides build metadata (e.g. `+0`, `+1-alpha.1`).

The suffix in the build metadata indicates the release stage:

| Suffix  | Stage         |
|---------|---------------|
| `alpha` | Internal beta |
| `beta`  | Public beta   |
| `rc`    | Pre-release   |
| (none)  | Stable        |

## Release artifacts

Each release includes the following files:

| File          | Description                                       |
|---------------|---------------------------------------------------|
| `tini-static` | Statically-linked Tini binary (no glibc required) |
| `tini`        | Dynamically-linked Tini binary                    |

## License

[MIT License](LICENSE)
