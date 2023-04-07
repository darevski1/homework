### Exercise: Storage

#### Practice 1: Direct provisioning of Azure File storage

1. Login to Azure and connect to your AKS cluster.
2. Check if any pods run under the default namespace if so delete everything under the default namespace. 
3. 3.In this practice we will directly provision Azure Files to a pod running inside AKS.4
4. First create the Azure Files share. Run the following commands:




First connect your azure clusster, using this commands

    az account set --subscription df86697d-88bc-4474-899b-64b5dfd1d8cf
    az aks get-credentials --resource-group rgLearn --name mkoAKS


## Create a resource group

    AKS_PERS_STORAGE_ACCOUNT_NAME=aksstorage1227
    AKS_PERS_RESOURCE_GROUP=rgLearn1227
    AKS_PERS_LOCATION="eastus"
    AKS_PERS_SHARE_NAME=1227aksshare
    
    az group create --name $AKS_PERS_RESOURCE_GROUP --location $AKS_PERS_LOCATION

![az group create](./images/1.png "k8")

### Create a storage account

    az storage account create -n $AKS_PERS_STORAGE_ACCOUNT_NAME -g $AKS_PERS_RESOURCE_GROUP -l $AKS_PERS_LOCATION --sku Standard_LRS
![az group create](./images/2.png "k8")

### Export the connection string as an environment variable, this is used when creating the Azure file share

    az storage account create -n $AKS_PERS_STORAGE_ACCOUNT_NAME -g $AKS_PERS_RESOURCE_GROUP -l $AKS_PERS_LOCATION --sku Standard_LRS

![az group create](./images/3.png "k8")
    
### Export the connection string as an environment variable, this is used when creating the Azure file shareexport 

    export AZURE_STORAGE_CONNECTION_STRING=$(az storage account show-connection-string -n $AKS_PERS_STORAGE_ACCOUNT_NAME -g $AKS_PERS_RESOURCE_GROUP -otsv)

![az group create](./images/4.png "k8")


### Create the file share

    az storage share create -n$AKS_PERS_SHARE_NAME --connection-string$AZURE_STORAGE_CONNECTION_STRING


![az group create](./images/5.png "k8")



### Get storage account key

    STORAGE_KEY=$(az storage account keys list --resource-group $AKS_PERS_RESOURCE_GROUP --account-name $AKS_PERS_STORAGE_ACCOUNT_NAME --query [0].value -otsv)

![az group create](./images/7.png "k8")

### Echo storage account name and key 

    echo Storage account name: $AKS_PERS_STORAGE_ACCOUNT_NAME
    echo Storage account key: $STORAGE_KEY

![az group create](./images/8.png "k8")



5. Make a note of the storage account name and key shown at the end of the script output. These values are
needed when you create the Kubernetes volume in one of the following steps.

6. Now we will need to create a Kubernetes secret that will be used to mount the Az File Share to the pod. You
need to hide this information from the pod’s definition and K8S secret is the best way to do it.

7. Run the following (single) command to create the secret


Create secret using this command

    kubectl create secret generic azure-secret --from-literal=aksstorage1227=$AKS_PERS_STORAGE_ACCOUNT_NAME --from-literal=LdZz/dov9WiXe/NGeLUzls6CN8mT4lYbXEpNAc2yejsfEg53LBKnW7tGtLXcAmG9gGNCAEDDYc+k+AStQR7TYQ===$STORAGE_KEY

Check if secret was created. 
    
    Run kubectl get secret -A.

![az group create](./images/9.png "k8")

After we created secret we can create the yaml file **azure-files-pod.yaml.**

![az group create](./images/11.png "k8")

Upload newly created file and run to create new pod:

    kubectl apply -f azure-files-pod.yaml. 

![az group create](./images/10.png "k8")


You can use kubectl describe pod mypod to verify the share is mounted successfully.

![az group create](./images/12.png "k8")

## Practice 2: Provisioning Azure File storage using PVs and PVCs

1. Login to Azure and connect to your AKS cluster.
2. Check if any pods run under the default namespace if so delete everything under the default namespace.
3. Now we will provision Azure files storage to a pod using PV and PVC.
4. Create a azurefile-mount-options-pv.yaml file with a PersistentVolume like this:

Lets create new zurefile-mount-options-pv.yaml PersistentVolume and upload 


![az group create](./images/14.png "k8")


    kubectl apply -f azurefile-mount-options-pv.yaml 


![az group create](./images/15.png "k8")


5. Note the access mode. Can you use other mode with Azure files?
6. Now create a azurefile-mount-options-pvc.yaml file with a PersistentVolumeClaim that uses the
PersistentVolume like this:

![az group create](./images/16.png "k8")

    kubectl apply -f azurefile-mount-options-pv.yaml

![az group create](./images/17.png "k8")

Mount the PersistentVolumeClaim

![az group create](./images/18.png "k8")

Verify your PersistentVolumeClaim is created and bound to the PersistentVolume. 
Run:
     kubectl get pvc azurefile.

![az group create](./images/19.png "k8")


Now we can embed the PVC info inside our pod definition. Create the following file azure-files-pod.yaml with
following content:

![az group create](./images/20.png "k8")


    kubectl apply -f azure-files-pod.yaml.


    kubectl describe pod mypod


![az group create](./images/21.png "k8")