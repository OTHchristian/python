<?php

function login(){
    $response = readline("what do you want 1)connect 2)create account\n");
    switch($response){
        case 1:
            $name = readline("enter your name : ");
            $passwd = readline("enter your password : ");
            connection($name,$passwd);
        break;
        case 2:
            $name = readline("enter your name : ");
            $passwd = readline("enter your password : ");
            create($name,$passwd);
        break;
        default:
            echo "bad option\n";
    }
}