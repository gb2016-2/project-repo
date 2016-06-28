<?php
namespace app\controllers;

use app\Controller;
use app\models\Site;

class SiteController extends Controller
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