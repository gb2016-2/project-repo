<?php
function debug($params = [])
{
	if(!empty($params))
	{
		echo "<pre>";
		print_r($params);
		echo "<pre>";
		exit;
	}
}
?>