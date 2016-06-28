<?php
namespace app\models;

class ArrayPersonRepository implements PersonRepository {
    private $persones = [];

    public function save(Person $person) {
        $this->persones[(string)$person->getId()] = $person;
    }

    public function getAll() {
        return $this->persones;
    }

    public function findById(PersonId $personId) {
        if (isset($this->persones[(string)$personId])) {
            return $this->persones[(string)$personId];
        }
    }
}
?>