import os
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class K8sClient:
    def __init__(self):
        """Initialize K8s client using in-cluster config or kubeconfig."""
        try:
            config.load_incluster_config()
        except:
            config.load_kube_config()
        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()

    def list_pods(self, namespace=None):
        """List pods in namespace (default: all namespaces)."""
        try:
            if namespace:
                pods = self.core_api.list_namespaced_pod(namespace)
            else:
                pods = self.core_api.list_pod_for_all_namespaces()
            return pods.items
        except ApiException as e:
            raise Exception(f"Error listing pods: {e}")

    def get_pod(self, namespace, name):
        """Get pod details."""
        try:
            return self.core_api.read_namespaced_pod(name, namespace)
        except ApiException as e:
            raise Exception(f"Error getting pod {name}/{namespace}: {e}")

    def get_pod_events(self, namespace, name):
        """Get events for pod."""
        try:
            events = self.core_api.list_namespaced_event(namespace, field_selector=f'involvedObject.name={name}')
            return events.items
        except ApiException as e:
            raise Exception(f"Error getting events for {name}/{namespace}: {e}")

