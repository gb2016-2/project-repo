<?php
if(!defined('CROWLER-API')) die ("Hacking attempt!");

function autoload($className)
{
	$file = preg_replace('/^app/', 'classes', $className) . '.php';
	
	if(file_exists($file))
		require_once($file);
}

spl_autoload_register('autoload');
?>