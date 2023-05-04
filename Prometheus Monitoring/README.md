### Create a Namespace & ClusterRole

First we need to created namespace for our monitoring using the following command, after we start the minikube

    minikube start

create new namespace using 

    kubectl create namespace monitoring

To verify that namespace **monitoring** is created in command line type:

   kubectl get namespaces

![namespace ](images/1.png)     