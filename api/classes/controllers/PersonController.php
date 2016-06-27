<?php
namespace app\controllers;

use app\models\Person;

class PersonController
{
	public function PersonStatsAll()
	{
		$model = new Person;
		$persones = $model->getPersones();
		
		foreach($persones as $person)
		{
			$response['persones'][$person->id] = $person->name;
		}
		
		return $response;
	}
	
	public function PersonStatsByDate()
	{
		
	}
	
	public function AdminPersonesAll()
	{
		
	}
	
	public function AdminAddPerson()
	{
		
	}
	
	public function AdminUpdatePerson()
	{
		
	}
	
	public function AdminDeletePerson()
	{
		
	}
}
?>