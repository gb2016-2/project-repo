<?php
require_once(__DIR__ . "/../config.php");
if(!defined('CROWLER-API')) die ("Hacking attempt!");

require_once(__DIR__ . "/functions/autoload.php");
require_once(__DIR__ . "/functions/debug.php");

use app\Application;

$app = new Application;

echo $app->response;
//return $app->response;
?>