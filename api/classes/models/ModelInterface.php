<?php
namespace app\models;

interface ModelInterface
{
    public function find();
	
	public function findById($id);
	
	public function findAll();
	
	public function save($object);
}
?>