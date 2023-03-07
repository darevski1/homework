## SF DevOps Academy Homework - Exercise: Shell scripts 

#### 1. Write a shell script to get the current date, time, username and current working directory. 
    #!/bin/bash

    getdate=$(date +'%d/%m/%Y)
    gettime=$(date +'%T')

    echo "The current date is " $getdate " and current time is" $gettime

#### 2. Write a shell script that prints “I love learning about DevOps” on the screen. Message should be a variable.  
    #!/bin/bash

    message="I love learning about DevOps"
    echo $message

#### 3. Write a shell script that displays “plan code build test release deploy” on the screen with each appearing on a separate line.  
    #!/bin/bash
    echo -e 'plan\ncode\nbuild\ntest\nrelease\ndeploy'  

#### 4. Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular  file, a  directory, or another  type  of  file.  Also  perform a ls command against the  file or directory with the long listing option.  

    #!/bin/bash

    #Get user input 
    echo "Hi, please type name"
    read name
    
    if [ -f $name ]
    then
        echo $name "its a regular file"; 
        ls -l $name
    elif [ -d $name ]
    then
        echo $name "a is directory"
        ls -l $name
    else
        echo $name "Another type of file"
        ls -l $name
    fi

#### 5. Use arguments in a script.  Total number of arguments should be three.  

    #!/bin/bash

    echo "HI, enter your name"
    read name

    echo "Enter your lastname"
    read lastname

    echo "City name"
    read city

    echo "Hi, my name is" $name $lastname "i live in " $city


#### 6. Write a script that till output your name out of a variable and will display the server uptime 
    #!/bin/bash 
    
    echo "My name is " $USER
    echo "Server its running for:"  uptime


