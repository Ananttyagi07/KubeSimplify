from ks.k8s_client import K8sClient

COMMON_ISSUES = [
    "CrashLoopBackOff",
    "ImagePullBackOff",
    "OOMKilled",
    "FailedScheduling",
    "ErrImagePull"
]

def diagnose_pod(namespace, pod_name):
    """Diagnose pod for common issues."""
    client = K8sClient()
    issues = []
    
    # Get pod status
    try:
        pod = client.get_pod(namespace, pod_name)
        status = pod.status.phase
        if status != "Running":
            issues.append(f"Pod not running: {status}")
        
        # Check container restarts
        if pod.status.container_statuses:
            for cont in pod.status.container_statuses:
                if cont.restart_count > 3:
                    issues.append("High restart count detected")
        
        # Check events
        events = client.get_pod_events(namespace, pod_name)
        for event in events:
            reason = event.reason
            if any(issue in reason for issue in COMMON_ISSUES):
                issues.append(f"Event: {reason} - {event.message}")
    
    except Exception as e:
        issues.append(str(e))
    
    return issues

