<?php
namespace app;

if(!defined('CROWLER-API')) die ('Hacking attempt!');

class Controller
{
	private $attributes;
	
	public static function ClassName()
	{
		return get_called_class();
	}
	
	public static function getAttributes($className)
	{
		return get_class_vars($className);
	}
	
	public function request()
	{
		return ($_SERVER['REQUEST_URI']) ? true : false;
	}
	
	public function post()
	{
		if(isset($_POST))
		{
			return $_POST;
		}
	}
}
?>