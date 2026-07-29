# Development Guide

## Standards
- Python 3.8+
- Black formatting: `black .`
- Type hints
- Docstrings

## Testing
Requires kubeconfig or in-cluster. Test with:
```
python main.py pods
kubectl run test-nginx --image=nginx --restart=Never # for diagnose default test-nginx
```

## Adding Commands
Add to main.py with @cli.command(), call from ks/commands.py

