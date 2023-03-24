## Implement Intersite Connectivity Student 

### In this lab, you will:

<ul>
    <li>Task 1: Provision the lab environment</li>
    <li>Task 2: Configure local and global virtual network peering</li>
    <li>Task 3: Test intersite connectivity</li>
</ul>

![Open powershell ](images/a1.png)

In the Azure portal, open the Azure Cloud Shell

Using powershell upload the files

<br />

**az104-05-vnetvm-loop-template.json**

<br />

**az104-05-vnetvm-loop-parameters.json**

![Open powershell ](images/a2.png)

In the powershell type **code .** and vscode will be open in powershell terminal. Edit password, type secure password **az104-05-vnetvm-loop-parameters.json** and save the file.

We have to create new resource group that will be hosting the lab environment. The first two virtual networks and a pair of virtual machines will be deployed in azure region 1, The third virtual network and the third virtual machine will be deployed in the same resource group but another azure region 2. 