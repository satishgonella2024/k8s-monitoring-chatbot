# app/handlers/kubernetes_handler.py

from kubernetes import client, config

# def get_cluster_info():
#     """
#     Fetch basic information about the Kubernetes cluster.
#     """
#     config.load_kube_config()  # Load kubeconfig from the local system
#     v1 = client.CoreV1Api()
#     nodes = v1.list_node()
#     node_names = [node.metadata.name for node in nodes.items]
#     return {
#         "node_count": len(node_names),
#         "nodes": node_names
#     }
def get_cluster_info():
    # Mock response for testing
    return {
        "status": "Cluster is not running. No active nodes.",
        "nodes": [],
    }

