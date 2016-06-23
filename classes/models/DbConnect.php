<?php
namespace classes\models;

if(!defined('CROWLER-API')) die ("Hacking attempt!");

class DbConnect
{
	public static $_instanse;
	public $db;
	
	private function __construct() {
		$this->connect();
	}
	
	private function __clone() {}
	
	public static function getInstanse()
	{
		if(!empty(self::$_instanse))
		{
			return self::$_instanse;
		}
		else
		{
			self::$_instanse = new self;
			return self::$_instanse;
		}
	}
	
	private function connect()
	{
		global $config;
		
		try
		{
			$this->db = new \PDO($config['db']['dsn'], $config['db']['username'], $config['db']['password']);
			
			if($this->db->errorCode > 0) throw new PDOException($this->db->errorInfo);
		}
		catch(\PDOException $e)
		{
			die("Ошибка подключения к БД!<br>" . $e->getMessage());
		}
	}
}
?>