<?php
namespace app;

class ErrorController
{
	public function error_404()
	{
		header('HTTP/1.1 404 Not Found');
		return [
			'error' => 'Error 404: This page is not exists!',
		];
	}
}
?>