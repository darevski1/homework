### Create a Namespace & ClusterRole

First we need to created namespace for our monitoring using the following command, after we start the minikube

    minikube start

create new namespace using 

    kubectl create namespace monitoring

To start the dashboard for kubernetis cluster run **minikube dashboard** and navigate to **Cluster / Namespaces** and we can see that the namespace that we create.

![namespace ](images/a1.png)     

To verify that namespace **monitoring** is created in command line type:

   kubectl get namespaces

![namespace ](images/1.png)     

Now lets create new file caled **clusterRole.yaml** 
Note: In the role, given below, you can see that we have added ***get, list, and watch*** permissions to nodes, services endpoints, pods, and ingresses. The role binding is bound to the monitoring namespace. If you have any use case to retrieve metrics from any other object, you need to add that in this cluster role.

**clusterRole.yaml** 

![namespace ](images/2.png)    

run the following command to create the role

    kubectl create -f clusterRole.yaml

![namespace ](images/3.png)    


## Create a Config Map To Externalize Prometheus Configurations

All configurations for Prometheus are part of prometheus.yaml file and all the alert rules for Alertmanager are configured in prometheus.rules.

***prometheus.yaml:*** This is the main Prometheus configuration which holds all the scrape configs, service discovery details, storage locations, data retention configs, etc)

***prometheus.rules:*** This file contains all the Prometheus alerting rules

Lets create new file config-map.yaml with the following content [config-map.yaml](https://raw.githubusercontent.com/bibinwilson/kubernetes-prometheus/master/config-map.yaml)


    kubectl create -f config-map.yaml


![namespace ](images/3.png)    







