<?php
class CRUD{ 
	$person = $_GET['person'];
	$site = $_GET['site'];
	$table = $_POST['table'];
	$id = $_POST['id'];
	$name = $_POST['name'];
	$siteName = $_POST['siteName'];
	$personName = $_POST['personName'];


	function PersonStatsAll()
	{
		$result = mysqli_query("SELECT * FROM person_page_rank WHERE person_id IN(SELECT id FROM persons WHERE name = '$person') AND page_id IN(SELECT id FROM pages WHERE site_id IN(SELECT id FROM sites WHERE name = '$site'))");
		return $result;
	}

	function PersonStatsByDate()
	{
		$result = mysqli_query("");
		return $result;
	}

	function AdminPersonesAll()
	{
		$result = mysqli_query("SELECT * FROM persons ");
		return $result;
	}

	function AdminAddPerson()
	{
		$query = mysqli_query("INSERT INTO $table($personName) values ('$name')");
	}

	function AdminUpdatePerson()
	{
		$query = mysqli_query("UPDATE FROM persons set name = '$personName' WHERE id = '$id'");
	}

	function AdminDeletePerson()
	{
		$query = mysqli_query("DELETE FROM persons WHERE id = '$id'");
	}

	function AdminSitesAll()
	{
		$result = mysqli_query("SELECT * FROM sites ");
		return $result;
	}

	function AdminAddSite()
	{
		$query = mysqli_query("INSERT INTO $table($siteName) values ('$name')");
	}

	function AdminUpdateSite()
	{
		$query = mysqli_query("UPDATE FROM sites set name = '$siteName' WHERE id = '$id'");
	}

	function AdminDeleteSite()
	{
		$query = mysqli_query("DELETE FROM sites WHERE id = '$id'");
	}
}
?>