<?php
namespace app;

use app\Router;
use app\base\BaseController;
use app\controllers\PersonController;
use app\controllers\SiteController;
use app\controllers\Array2XML;

if(!defined('CROWLER-API')) die ('Hacking attempt!');

class Application extends BaseController
{
	public function __construct(){
		$this->Request();
	}
	
	public function before(){
		$router = new Router;
		$this->controller = $router->controller;
		$this->action = $router->action;
		
		$params = ($this->getParamsRequest()) ? $this->getParamsRequest() : NULL;
		$this->format = (isset($params['format'])) ? $params['format'] : 'json';
	}
	
	public function setHeader(){
		($this->format == 'json') ? header('Content-Type: application/json;charset=utf-8') : header('Content-type: application/xml;charset=utf-8');
	}
	
	public function response(){
		$action = $this->action;
		
		if(!method_exists($this->controller, $action))
		{
			$this->controller = new ErrorController;
			$response = $this->controller->error_404();
		}
		else
		{
			$response = $this->controller->$action();
		}
		
		$this->response = ($this->format == 'json') ? json_encode($response, JSON_UNESCAPED_UNICODE) : (new Array2XML)->convert($response, 'item-');
	}
	
	public function getParamsRequest()
	{
		if(isset($_GET)) return $_GET;
		elseif($_POST) return $_POST;
		elseif($_PUT) return $_PUT;
		elseif($_DELETE) return $_DELETE;
		else return false;
	}
}
?>