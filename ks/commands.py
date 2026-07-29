from ks.k8s_client import K8sClient
from ks.formatter import print_pod_table, print_diagnosis
from ks.diagnostics import diagnose_pod

def pods_command():
    """Handle pods command."""
    client = K8sClient()
    pods = client.list_pods()
    print_pod_table(pods)

def diagnose_command(namespace, pod_name):
    """Handle diagnose command."""
    issues = diagnose_pod(namespace, pod_name)
    print_diagnosis(pod_name, namespace, issues)

