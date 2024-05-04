<?php
require 'deconnection.php';

function connection($name,$password){

    $admin = [
        'christian'=>'oth christian',
        'neymar'=>'do brazil',
        'cristiano'=>'sui'
    ];
    
    foreach($admin as $n => $p){
        if($name==$n && $password==$p){
            echo "hello $name\n";
            $response = readline("what do you want? 1)work in my workspace 2)disconnect\n");
            switch($response){
                case 1 :
                    /* c'est ici qu'il faut ecrire le code des manipulations a effectuer */
                break;
                case 2 :
                    disconnect();
                break;
            }
            break;
        }elseif(($name==$n && $password!=$p) || ($name!=$n && $password==$p)){
            echo "the password or the name is not write correctly\n";
            break;
        }
    }
}

