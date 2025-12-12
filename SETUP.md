# ChainLock Setup Guide

## Quick Start

### 1. Extract Files
```bash
unzip chainlock.zip
cd chainlock
```

### 2. Initialize Git
```bash
git init
git add .
git commit -m "Initial ChainLock setup"
```

### 3. Create GitHub Repository
```bash
# Using GitHub CLI
gh repo create my-secure-app --public --source=. --push

# Or manually
# 1. Create repo on GitHub
# 2. git remote add origin https://github.com/USERNAME/REPO.git
# 3. git push -u origin main
```

### 4. Verify Build
Visit `https://github.com/USERNAME/REPO/actions`

### 5. Verify Signature
```bash
cosign verify   --certificate-identity-regexp "https://github.com/USERNAME/REPO"   --certificate-oidc-issuer "https://token.actions.githubusercontent.com"   ghcr.io/USERNAME/REPO:latest
```

## Kubernetes Integration

### Install Kyverno
```bash
kubectl create -f https://github.com/kyverno/kyverno/releases/latest/download/install.yaml
```

### Apply Policy
```bash
# Update YOUR_USERNAME first
sed -i 's/YOUR_USERNAME/your-username/g' policy/kyverno-policy.yaml
kubectl apply -f policy/kyverno-policy.yaml
```

### Test
```bash
# Should succeed (signed)
kubectl run test --image=ghcr.io/USERNAME/REPO:latest

# Should fail (unsigned)
kubectl run fail --image=nginx:latest
```
