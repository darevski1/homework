#! /bin/bash


# Get current date

getdate=$(date +'%d/%m/%Y')
gettime=$(date +'%T')

echo "The current date is " $getdate " and the time is" $gettime


# Get the current login user

echo "The current user that is logged in is:" $USER  


#get current working directory

echo "The current working directory is:" 
pwd

