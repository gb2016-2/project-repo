<?php
namespace app\models;

use app\models\Model;

if(!defined('CROWLER-API')) die ("Hacking attempt!");

class Site extends Model
{
	public $id;
	public $name;
	public $tableName = 'sites';
	private $sites = [];
	
	public function getSites()
	{
		$this->sites = parent::findAll();
		return $this->sites;
	}
}
?>