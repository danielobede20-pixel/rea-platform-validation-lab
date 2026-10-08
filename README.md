# REA native validation lab

**Public test-only repository.** No business documents, credentials, or proprietary binaries are stored here.

This repo validates a synthetic C executable on an isolated GitHub-hosted Ubuntu runner. The workflow runs **only via manual `workflow_dispatch`**, has read-only repository permission and an 18-minute timeout. It downloads SHA-256-verified Ghidra 12.1.4 and installs REA 5.0.0 locally for this job. A passing result proves only that the sample ELF was analyzed with Ghidra; it does **not** imply that third-party software, Android or firmware can be fully reconstructed.

Use the workflow **REA Ghidra Linux** in the GitHub Actions tab. No scheduled jobs, releases, secrets, or external systems are touched. All test software is original and freely inspectable.

The main Hermes instance stays on the Windows notebook; this lab is isolated and disposable.
