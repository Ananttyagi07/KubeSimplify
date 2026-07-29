# Architecture

## Overview
KubeSimplify is modular CLI:

- `main.py`: Click CLI entrypoint
- `ks/k8s_client.py`: Kubernetes Python client wrapper
- `ks/commands.py`: Business logic orchestrator
- `ks/diagnostics.py`: Issue detection
- `ks/formatter.py`: Rich output formatting

## Flow
CLI command → commands.py → k8s_client.py → API → diagnostics.py → formatter.py → Terminal

