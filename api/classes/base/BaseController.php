<?php
namespace app\base;

abstract class BaseController
{
	public $response;
	public $format;
	
	abstract protected function __construct();
	
	abstract protected function before();
	
	abstract protected function setHeader();
	
	abstract protected function response();
	
	protected function Request()
	{
		$this->before();
		$this->setHeader();
		$this->response();
	}	
}
?>