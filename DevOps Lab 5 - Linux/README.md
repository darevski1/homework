
# Exercise: Basic Linux & Bash commands 

## Exercise 01

### Create a file friends.txt with a list of names of three of your friends on separate lines. 

* Lets create new file using nano - text editor, open Terminal and type:

        $ nano friends.txt
![Open terminal](images/1.png)

* Alternativy you can create new file using touch command

		$ touch friends.txt

![Open terminal](images/2.png)


* Open the document in text editor and save using ctrl + x and select y

		$ nano friends.txt

![Open friends.txt ](images/3.png)

## Exercise 02
### Display the contents of friends.txt on the console. 

		$ cat friends.txt

![Open friends.txt ](images/4.png)

![Open friends.txt ](images/5.png)


## Exercise 03 
### Rename file friends.txt to bestfriends.txt 

 * To change the of the use command mv
 
 	
        $ mv friends.txt  bestfriends.txt 

 
![Rename friends.txt  to bestfriends.txt ](images/6.png)


## Exercise 04 
### Make a copy of bestfriends.txt under the name sysadmins.txt

 * Copy bestfriends.txt sysadmins.txt using cp command
 
 	
        $ cp bestfriends.txt sysadmins.txt

 
![Rename friends.txt  to bestfriends.txt ](images/7.png)

## Exercise 05

### List all files whose name begins with letter 'b' and ends with extension txt. 

    $ ls | grep ^b


 ![](images/11.png)

## Exercise 06

###  Write a command that will tell you how many bytes are taken up by file sysadmins.txt 

* we can check the file size using commands 
 
 		    ls -l filename | awk '{print $5}'
            stat -c %s filename
            wc -c < filename


![Rename friends.txt  to bestfriends.txt ](images/9-2.png)

![Rename friends.txt  to bestfriends.txt ](images/9-3.png)

![Rename friends.txt  to bestfriends.txt ](images/9-1.png)

## Exercise 07

###  Create file cars.txt with a list of 5 brands of cars on separate lines. 

* Open terminal and type
 
            nano cars.txt
            touch cars.txt


![Rename friends.txt  to bestfriends.txt ](images/10-1.png)

![Rename friends.txt  to bestfriends.txt ](images/10-2.png)

![Rename friends.txt  to bestfriends.txt ](images/10-3.png)


## Exercise 08

###  Check how many bytes are taken up by the file. 

* Open terminal and type
 
            $ ls -l cars.txt | awk '{print $5}'
             

![Check file size ](images/12.png)

 
 
 ## Exercise 09

###  Copy the file cars.txt into directory /tmp. 

 
            $ cars.txt /tmp/
             

![Check file size ](images/13.png)
 

  ## Exercise 10

###  List all files with extension *.txt in directory /tmp and verify that the file was copied properly. 

 
            $ sudo find /tmp -type f -name "*.txt"
             

![Find all files with extension *.txt ](images/14.png)



  ## Exercise 11

###  Without leaving your home directory rename file cars.txt located in /tmp to vehicles.txt in /tmp 

 
            $ mv /tmp/cars.txt /tmp/vehnicles.txt
             

![Change file name](images/15.png)
 

 ## Exercise 12

###  Display the contents of /etc/passwd file on the screen interactively (so you can search, scroll up and down). 

            $ less /etc/passwd
             

![less man page ](images/16.png)
![less man page ](images/17.png)

 