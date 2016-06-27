<?php
if(!defined('CROWLER-API')) die ("Hacking attempt!");

function autoload($className)
{
	$file = preg_replace('/^app/', 'classes', $className) . '.php';
	
	if(!file_exists($file))
	{
		header('HTTP/1.1 404 Not found!');
		die('Error 404: Page not found!');
	}
	require_once($file);
}

spl_autoload_register('autoload');
?>