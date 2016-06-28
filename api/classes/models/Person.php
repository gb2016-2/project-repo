<?php
namespace app\models;

use app\models\Model;

if(!defined('CROWLER-API')) die ("Hacking attempt!");

class Person extends Model
{
	public $id;
	public $name;
	public $tableName = 'persons';
	private $persons = [];
	
	public function getPersones()
	{
		$this->persons = parent::findAll();
		return $this->persons;
	}
}
?>