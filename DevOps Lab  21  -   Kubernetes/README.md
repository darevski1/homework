


Exercise: PodsPods are the smallest, most basic deployable objects in Kubernetes. A Pod represents a single instance of a running process in your cluster. Pods contain one or more containers, such as Docker containers. Although you want deploy pods directly (static pods), knowledge for defining pods manifest files will be used for defining more complex Kubernetes resources like Controllers.

### Practice1: Simple pods operations


Login to your Azure portal and crete AKS cluster, navigate to Kubernetes services / Create Cluster


![Create cluster k8](./images/1.png "")

![Create cluster k8](./images/2.png "Create cluster ")

![Create cluster k8](./images/3.png "Create cluster ")

When we created the clusted we can connect to the cluster, click Connect new windows will popup on the right side of the screen there we have details how to connect to our cluster

![Create cluster k8](./images/5.png "Create cluster ")


Next open PowerShell and Run the following commands.

    az account set --subscription df86697d-88bc-4474-899b-64b5dfd1d8cf
    az aks get-credentials --resource-group rgLearn --name mkoAKScluster


![Create cluster k8](./images/4.png "Create cluster ")









