## Implement Web Apps

<ul>
     <li> Task 1: Create an Azure web app </li>
     <li> Task 2: Create a staging deployment slot </li>
     <li> Task 3: Configure web app deployment settings </li>
     <li> Task 4: Deploy code to the staging deployment slot </li>
     <li> Task 5: Swap the staging slots </li>
     <li> Task 6: Configure and test autoscaling of the Azure web app </li>
</ul>


![Open powershell ](images/Screenshot_1.png)

 
 ### Task 1: Create an Azure web app 

 Create new VM in **App Service** 

 ![Open powershell ](images/Screenshot_2.png)

 ### Task 2: Create a staging deployment slot

 Open the VM that we have deployed and from left side menu click **Deployment slots**

 ![Open powershell ](images/Screenshot_3.png)


and click Add Slot

 ![Open powershell ](images/Screenshot_4.png)

create staging slot as follow

 ![Open powershell ](images/Screenshot_5.png)

 succes we created new staging slot who differs from the one assigned to the production slot.
 
 ![Open powershell ](images/Screenshot_6.png)


###  Task 3: Configure web app deployment settings 

On the staging **deployment** slot blade, in the Deployment section, click **Deployment Center** and then select the **Settings tab.**

On the **Settings tab**, in the Source drop-down list, select **Local Git** and click the **Save** button

 ![Open powershell ](images/Screenshot_7.png)


On the **Deployment Center** blade, copy the **Git Clone Url** entry to Notepad.


     Git Clone Uri
     https://mkov1-staging.scm.azurewebsites.net:443/mkov1.git



On the **Deployment Center** blade, select the **Local Git/FTPS** credentials

 ![Open powershell ](images/Screenshot_8.png)

 User Scope section, specify the following settings, and click Save.

 ![Open powershell ](images/Screenshot_9.png)


### Task 4: Deploy code to the staging deployment slot

Open cloud shell / PowerShell and clone git repo from powershell


     git clone https://github.com/Azure-Samples/php-docs-hello-world

From the Cloud Shell pane, run the following to set the current location to the newly created clone of the local repository containing the sample web app code.

     Set-Location -Path $HOME/php-docs-hello-world/


From the Cloud Shell pane, run the following to add the remote git (make sure to replace the [deployment_user_name] and [git_clone_url] placeholders with the value of the Deployment Credentials user name and Git Clone Url, respectively, which you identified in previous task):

     git remote add [deployment_user_name] [git_clone_url]

     git remote add darevski https://github.com/Azure-Samples/php-docs-hello-world

 ![Open powershell ](images/Screenshot_11.png)

 Verify that the browser page displays the Hello World! message and close the new tab.

  ![Open powershell ](images/Screenshot_12.png)

  ### Task 5: Swap the staging slots

  In the **eployment section**, click **Deployment** slots and then, click **Swap** toolbar icon.

![Open powershell ](images/Screenshot_13.png)

![Open powershell ](images/Screenshot_14.png)
Click **Overview** on the production slot blade of the web app and then click the **URL** link to display the web site home page in a new browser tab.
![Open powershell ](images/Screenshot_15.png)


### Task 6: Configure and test autoscaling of the Azure web app

In this task, you will configure and test autoscaling of Azure web app. 
Not working !!!!



