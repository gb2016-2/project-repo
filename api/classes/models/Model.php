<?php
namespace app\models;

use \PDO;
use app\db\DbConnect;
use app\models\ModelInterface;

if(!defined('CROWLER-API')) die ("Hacking attempt!");

class Model implements ModelInterface
{
	private $objects = [];
	private $db;
	private $clssName;
	private $sql;
	private $result;
	
	public function __construct(){}
	
	public function getTableName()
	{
		return $this->tableName;
	}
	
	/*
	** Количество параметров должно соответствовать количеству переменных в SQL запросе
	** и они должны идти в том же порядке.
	** Например: $db->query = ("SELECT * FROM `table` WHERE `id` = ?", $id);
	**
	** Возвращает результирующую таблицу.
	*/
	private function query($sql)
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
		
		$result = $db->query($sql);
		return $result;
	}
	
	public function find()
	{
		$className = debug_backtrace();
		$this->className = $className[0]['class'];
		
		$this->tableName = $this->getTableName();
		
		$this->sql = "SELECT * FROM {$this->tableName}";
		
		$result = $this->query($this->sql);
		
		$result->setFetchMode(PDO::FETCH_CLASS, $this->className);
		
		
		return $result->fetch();
	}
	
	public function findById($id)
	{
		
	}
	
	public function findAll()
	{
		$className = debug_backtrace();
		$this->className = $className[0]['class'];
		
		$this->tableName = $this->getTableName();
		
		$this->sql = "SELECT * FROM {$this->tableName}";
		
		$result = $this->query($this->sql);
		
		$result->setFetchMode(PDO::FETCH_CLASS, $this->className);
		
		/* while($row = $result->fetch())
		{
			$arr[$row->id] = $row;
		} */
		
		//$result = $this->result;
		return $result->fetchAll();
	}
	
	public function where($key, $value)
	{
		
	}
	
	public function save($object)
	{
		
	}
}
?>