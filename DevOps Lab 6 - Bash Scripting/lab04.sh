#!/bin/bash


#Get user input 
echo "Hi, please type name"
read name

#find -name $name
 
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
 