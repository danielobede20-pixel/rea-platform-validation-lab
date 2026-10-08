# REA isolated Linux validation lab

**Public test-only repository.** All input files are synthetic and original. No customer files, private repositories, credentials, secrets, or business assets may be uploaded here.

## Verified workflows (2026-10-08)

| Workflow | Components | Synthetic proof | Latest successful run |
| --- | --- | --- | --- |
| REA Ghidra Linux | REA 5.0.0, Ghidra 12.1.4, Java 21 | Ghidra `binary_overview` on x86-64 ELF, 4/4 checks | [37742162269](https://github.com/danielobede20-pixel/rea-platform-validation-lab/actions/runs/37742162269) |
| REA Android Linux | REA 5.0.0, JADX headless MCP 0.7.1 | Generated Android APK and searched for LeadScore, 4/4 checks | [37742468262](https://github.com/danielobede20-pixel/rea-platform-validation-lab/actions/runs/37742468262) |
| REA Firmware Linux | REA 5.0.0, Binwalk 3.1.0, Unblob 26.6.4 | Inspected GZIP signature and executed extraction workflow on synthetic blob, 5/5 checks | [37742905775](https://github.com/danielobede20-pixel/rea-platform-validation-lab/actions/runs/37742905775) |

All workflows use **manual `workflow_dispatch`**, restricted `contents: read` permissions, execution timeouts, and ephemeral standard GitHub-hosted Ubuntu runners. They do not modify the Windows Hermes installation or use credentials.

Ghidra and JADX headless release downloads are SHA-256 verified. Binwalk is installed from the pinned Cargo version; Unblob is pinned to PyPI version 26.6.4.

**Scope matters:** these results do not validate all executables, applications, encryption, anti-tampering protections, or functional equivalence. Ghidra test validates a native binary overview, not complete recovered source code. Firmware test uses a synthetic GZIP-containing blob, not an actual vendor firmware image.

## Usage
Open the repository's [GitHub Actions](https://github.com/danielobede20-pixel/rea-platform-validation-lab/actions) tab and run any workflow manually. These workflows deliberately have no input upload mechanism: real private business artifacts need a separate private execution path and authorization.

## Future work
- Validate native function-level decompilation and compare observable behavior.
- Validate Android method-level source tracing and independent functional tests.
- Validate multi-region firmware with extractor output digests.
- Design a private, isolated workspace for authorized nonpublic assets; never use this public repository for confidential data.
