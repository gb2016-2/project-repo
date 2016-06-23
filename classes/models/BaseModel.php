<?php
namespace classes\models;

if(!defined('CROWLER-API')) die ("Hacking attempt!");

class BaseModel extends DbConnect
{
	public function __construct(){}
	
	/*
	** Количество параметров должно соответствовать количеству переменных в SQL запросе
	** и они должны идти в том же порядке.
	** Например: $db->query = ("SELECT * FROM `table` WHERE `id` = ?", $id);
	**
	** Возвращает результирующую таблицу.
	*/
	public function query($sql)
	{
		$args = func_get_args();
		
		$sql = array_shift($args);
		
		$db = DbConnect::getInstanse()->db;
		
		$args = array_map(function($param) use ($db) {
			return "'" . $db->escape_string($param) . "'";
		}, $args);
		
		$sql = str_replace(array('%', '?'), array('%%', '%s'), $sql);
		
		array_unshift($args, $sql);
		
		$sql = call_user_func_array('sprintf', $args);
		
		try {
			$this->result = $db->query($sql);
			
			if($db->errorCode() > 0) Throw new \PDOException("Error database: ". $db->errorInfo()[2]);
		}
		catch(\PDOException $e)
		{
			echo $sql . '<br>';
			die ($e->getMessage());
		}
		
		return $this->result->fetch(\PDO::FETCH_OBJ);
	}
}
?>