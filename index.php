<?php
require_once("config.php");
if(!defined('CROWLER-API')) die ("Hacking attempt!");

require_once("functions/autoload.php");
require_once("functions/debug.php");

use classes\models\BaseModel;

$model = new BaseModel;

$sql = "SELECT * FROM keywords";

$result = $model->query($sql);

debug($result);
?>