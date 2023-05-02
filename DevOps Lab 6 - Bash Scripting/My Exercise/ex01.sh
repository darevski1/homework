#!/bin/bash

# if Statements

read -p "Enter your password:"

    if [ "$password" = "darko" ] 
    then
        echo "Zdravo darko"
    else
        echo "Ajde doma"
    fi

