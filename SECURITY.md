# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| main    | :white_check_mark: |
| v1.x    | :white_check_mark: |

This is an early-stage proof-of-concept. We actively support the `main` branch.

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in this codebase, please report it responsibly.

**Please do NOT report security vulnerabilities through public GitHub issues.**

### How to Report

1. Go to the [Security Advisories](https://github.com/YOURUSERNAME/mycelial-man-poc/security/advisories) page.
2. Click **"New advisory"** → **"Report a vulnerability"**.
3. Fill in the details using the template below.

Alternatively, you can email the maintainer directly at: **[your-email@example.com]** (replace with your actual email).

### What to Include in Your Report

- Description of the vulnerability
- Steps to reproduce
- Potential impact (e.g., remote code execution, data leakage, privacy budget bypass, graft poisoning, etc.)
- Suggested fix (if known)
- Any PoC or screenshots (if safe to share)

We aim to acknowledge reports within **48 hours** and provide a fix timeline within **7 days**.

## Security Considerations in This Project

This prototype implements several security-sensitive features:

- **Differential Privacy** on grafts
- **Orthogonal SVD projection** to prevent catastrophic forgetting
- **Hardware-rooted attestation** concepts (simulated)
- **Base64 serialized tensor transmission**

**Known limitations in this PoC:**
- The current version runs on a single machine for demonstration.
- Privacy budget is tracked in-memory only.
- No production-grade authentication or rate limiting between nodes.
- 4-bit quantized models have additional attack surfaces.

We welcome contributions that improve the security posture of the Mycelial Adapter Network.

## Responsible Disclosure

We follow the principle of **Coordinated Vulnerability Disclosure**. We ask that you:
- Allow us reasonable time to fix the issue before public disclosure.
- Not exploit the vulnerability for malicious purposes.

---

**Thank you** for helping keep the Mycelial Adapter Network secure.

---

This is the standard, professional format used by serious open-source projects. 

### How to Add It

1. In your repository folder, create the directory `.github`
2. Inside it, create the file `SECURITY.md`
3. Paste the content above (remember to replace `YOURUSERNAME` and your email address).

Would you also like:
- A `CONTRIBUTING.md`?
- A `CODE_OF_CONDUCT.md`?
- A simple `.gitignore` tailored for this project?

Just say the word and I’ll generate them.
