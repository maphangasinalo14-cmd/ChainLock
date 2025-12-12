# ChainLock ⛓️🔒
**Zero-Trust Software Supply Chain Security for Containers**

[![Security](https://img.shields.io/badge/security-sigstore-blue)](https://www.sigstore.dev/)
[![SBOM](https://img.shields.io/badge/sbom-spdx%20%7C%20cyclonedx-green)](https://spdx.dev/)
[![Scanning](https://img.shields.io/badge/scanning-trivy%20%7C%20grype-orange)](https://trivy.dev/)

## 🎯 Overview

ChainLock implements **complete software supply chain security** for containerized applications using industry-standard open-source tools. It provides cryptographic verification, transparency, and auditability for every artifact in your deployment pipeline.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions Workflow                                    │
│  ┌────────────┐  ┌──────────┐  ┌────────┐  ┌─────────────┐│
│  │ Build      │→│ Scan     │→│ Sign   │→│ Verify      ││
│  │ Container  │  │ Vulns    │  │ Image  │  │ Signature   ││
│  └────────────┘  └──────────┘  └────────┘  └─────────────┘│
│         ↓              ↓            ↓             ↓         │
│  ┌────────────┐  ┌──────────┐  ┌────────┐  ┌─────────────┐│
│  │ Generate   │  │ Attest   │  │ Attach │  │ Policy      ││
│  │ SBOM       │  │ Results  │  │ SBOM   │  │ Enforcement ││
│  └────────────┘  └──────────┘  └────────┘  └─────────────┘│
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  Kubernetes Cluster                                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Admission Controller (Kyverno/Policy Controller)    │  │
│  │  - Verifies signatures before deployment             │  │
│  │  - Validates SBOM attestations                        │  │
│  │  - Enforces security policies                         │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## ✨ Features

### 🔐 Cryptographic Signing
- Keyless signing with Sigstore Cosign
- OIDC-based identity (no keys to manage!)
- Transparency log (Rekor) for auditability
- Certificate transparency verification

### 📋 Software Bill of Materials
- Multi-format: SPDX, CycloneDX, Syft
- Attached to images for easy distribution
- Cryptographically attested for integrity
- Compliance-ready

### 🔍 Vulnerability Scanning
- Trivy & Grype for comprehensive coverage
- SARIF output for GitHub Security
- Scan attestations
- Continuous monitoring

### 🛡️ Policy Enforcement
- Sigstore Policy Controller support
- Kyverno policies included
- Runtime verification
- Fail-closed security

## 🚀 Quick Start

### 1. Generate Project (Google Colab)
Run this notebook and download the ZIP file!

### 2. Extract and Setup
```bash
unzip chainlock.zip
cd chainlock
git init
git add .
git commit -m "Initial ChainLock setup"
```

### 3. Create GitHub Repository
```bash
gh repo create my-secure-app --public --source=. --push
```

### 4. Watch the Magic
Visit `https://github.com/YOUR_USERNAME/my-secure-app/actions`

## 🔍 Verification

### Manual Verification
```bash
# Verify signature
cosign verify   --certificate-identity-regexp "https://github.com/YOUR_USERNAME"   --certificate-oidc-issuer "https://token.actions.githubusercontent.com"   ghcr.io/YOUR_USERNAME/my-secure-app:latest

# Verify SBOM attestation
cosign verify-attestation   --certificate-identity-regexp "https://github.com/YOUR_USERNAME"   --certificate-oidc-issuer "https://token.actions.githubusercontent.com"   --type spdxjson   ghcr.io/YOUR_USERNAME/my-secure-app:latest

# Download SBOM
cosign download sbom ghcr.io/YOUR_USERNAME/my-secure-app:latest
```

### Kubernetes Policy Enforcement

#### Install Kyverno
```bash
kubectl create -f https://github.com/kyverno/kyverno/releases/latest/download/install.yaml

# Update YOUR_USERNAME in policy
sed -i 's/YOUR_USERNAME/your-github-username/g' policy/kyverno-policy.yaml
kubectl apply -f policy/kyverno-policy.yaml
```

## 📚 What You Get

- ✅ Cryptographically signed container images
- ✅ Complete SBOM (3 formats)
- ✅ Automated vulnerability scanning
- ✅ Transparency log entries
- ✅ Multi-architecture builds
- ✅ GitHub Security integration
- ✅ Kubernetes policy enforcement
- ✅ SLSA Level 3 compliance

## 📖 Documentation

- Read `docs/SETUP.md` for detailed setup
- Visit [Sigstore Docs](https://docs.sigstore.dev/)
- Check [Kyverno Docs](https://kyverno.io/docs/)

## 🤝 Contributing

Contributions welcome! Open issues or submit PRs.

## 📄 License

MIT License

---

**Made with 🔒 for supply chain security**
