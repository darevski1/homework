
## Implement Azure Kubernetes Service

### Lab scenario

Contoso has a number of multi-tier applications that are not suitable to run by using Azure Container Instances. In order to determine whether they can be run as containerized workloads, you want to evaluate using Kubernetes as the container orchestrator. To further minimize management overhead, you want to test Azure Kubernetes Service, including its simplified deployment experience and scaling capabilities.

In this lab, you will:

Task 1: Register the Microsoft.Kubernetes and Microsoft.KubernetesConfiguration resource providers.

Task 2: Deploy an Azure Kubernetes Service cluster

Task 3: Deploy pods into the Azure Kubernetes Service cluster

Task 4: Scale containerized workloads in the Azure Kubernetes service cluster

![](./images/1.png)

Exercise 1
First login to you azure aacount and open **PowerShell**

From the Cloud Shell pane, run the following to register the Microsoft.Kubernetes and Microsoft.KubernetesConfiguration resource providers.

    Register-AzResourceProvider -ProviderNamespace Microsoft.Kubernetes

    Register-AzResourceProvider -ProviderNamespace Microsoft.KubernetesConfiguration

Task 2

In task 2 we have to create new cluster, navigate to **Kubernetes services** / and then in **Kubernetes services** click **Create** +  + **Create a Kubernetes cluster**

Task 3 
run

    kubectl get nodes

    NAME                                STATUS   ROLES   AGE     VERSION
    aks-agentpool-15031957-vmss000000   Ready    agent   4m56s   v1.24.10

    kubectl create deployment nginx-deployment --image=nginx    
    deployment.apps/nginx-deployment created


    kubectl get pods
    NAME                                READY   STATUS    RESTARTS   AGE
    nginx-deployment-85c6d5f6dd-sw5lf   1/1     Running   0          54s

    kubectl get deployment
    NAME               READY   UP-TO-DATE   AVAILABLE   AGE
    nginx-deployment   1/1     1            1           93s

    kubectl expose deployment nginx-deployment --port=80 --type=LoadBalancer
    service/nginx-deployment exposed

    kubectl get service
    NAME               TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
    kubernetes         ClusterIP      10.0.0.1       <none>           443/TCP        9m22s
    nginx-deployment   LoadBalancer   10.0.197.176   52.188.218.174   80:31209/TCP   23s

![](./images/2.png)

Task 4: Scale containerized workloads in the Azure Kubernetes service cluster
     kubectl scale --replicas=2 deployment/nginx-deployment
     deployment.apps/nginx-deployment scaled


    kubectl get pods
    NAME                                READY   STATUS    RESTARTS   AGE
    nginx-deployment-85c6d5f6dd-6rpw6   1/1     Running   0          36s
    nginx-deployment-85c6d5f6dd-sw5lf   1/1     Running   0          6m6s

    kubectl get nodes
    NAME                                STATUS   ROLES   AGE     VERSION
    aks-agentpool-15031957-vmss000000   Ready    agent   24m     v1.24.10
    virtual-node-aci-linux              Ready    agent   8m40s   v1.19.10-vk-azure-aci-1.4.8

    kubectl scale --replicas=10 deployment/nginx-deployment
    deployment.apps/nginx-deployment scaled

    kubectl get pods
    NAME                                READY   STATUS    RESTARTS   AGE
    nginx-deployment-85c6d5f6dd-6rpw6   1/1     Running   0          13m
    nginx-deployment-85c6d5f6dd-94th4   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-cxng6   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-l9lbn   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-m8z2p   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-nhllp   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-rd95p   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-sf85x   1/1     Running   0          8s
    nginx-deployment-85c6d5f6dd-sw5lf   1/1     Running   0          19m
    nginx-deployment-85c6d5f6dd-vxlh7   1/1     Running   0          8s

    kubectl get pod -o=custom-columns=NODE:.spec.nodeName,POD:.metadata.name
    NODE                                POD
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-6rpw6
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-94th4
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-cxng6
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-l9lbn
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-m8z2p
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-nhllp
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-rd95p
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-sf85x
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-sw5lf
    aks-agentpool-15031957-vmss000000   nginx-deployment-85c6d5f6dd-vxlh7

    kubectl delete deployment nginx-deployment
    deployment.apps "nginx-deployment" deleted