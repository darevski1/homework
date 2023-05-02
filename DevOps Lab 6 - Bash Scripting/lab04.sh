#!/bin/bash


#Get user input 
echo "Hi, please type name of file or dicrectory"
read name

#find -name $name
# check if is regualr file -f 
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
    #ls -l $name
fi
 