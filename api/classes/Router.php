<?php
namespace app;

if(!defined('CROWLER-API')) die ('Hacking attempt!');

class Router
{
	public $request;
	public $action;
	public $controller;
	
	public function __construct()
	{
		$this->request = $this->request();
		$this->run();
	}
	
	public function request()
	{
		return (!empty($_SERVER['REQUEST_URI'])) ? urldecode($_SERVER['REQUEST_URI']) : NULL;
	}
	
	public function run()
	{
		$action = $this->getAction();
		$controller = $this->getController($action);
		$this->controller = new $controller;
		$this->action = $action;
	}
	
	public function getAction()
	{
		$request = explode('/', $this->request);
		return ($request[2] != NULL) ? $request[2] : NULL;
	}
	
	public function getController($action)
	{
		switch($action)
		{
			case 'PersonStatsAll':
				return 'app\controllers\PersonController';
				break;
			case 'PersonStatsByDate':
				return 'app\controllers\PersonController';
				break;
			case 'AdminPersonesAll':
				return 'app\controllers\PersonController';
				break;
			case 'AdminAddPerson':
				return 'app\controllers\PersonController';
				break;
			case 'AdminUpdatePerson':
				return 'app\controllers\PersonController';
				break;
			case 'AdminDeletePerson':
				return 'app\controllers\PersonController';
				break;
			case 'AdminSitesAll':
				return 'app\controllers\SiteController';
				break;
			case 'AdminAddSite':
				return 'app\controllers\SiteController';
				break;
			case 'AdminUpdateSite':
				return 'app\controllers\SiteController';
				break;
			case 'AdminDeleteSite':
				return 'app\controllers\SiteController';
				break;
		}
	}
}
?>