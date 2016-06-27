<?php
namespace app\controllers;

use app\models\Site;

class SiteController
{
	public function AdminSitesAll()
	{
		$model = new Site;
		$sites = $model->getSites();
		
		foreach($sites as $site)
		{
			$response['sites'][] = $site->name;
		}
		
		return $response;
	}
	
	public function AdminAddSite($name)
	{
		
	}
	
	public function AdminUpdateSite($id)
	{
		
	}
	
	public function AdminDeleteSite($id)
	{
		
	}
}
?>