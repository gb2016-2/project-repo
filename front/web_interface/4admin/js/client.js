
//add person
function addNewPerson() {
    var person = prompt("Наименование", "");
    if (!person) {
        alert("Введите наименование");
   }
   else {
        var table = document.getElementById("persons-table");
var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(-1);
        cell1.innerHTML = person;
        cell1.className = "table-row";
        cell2.insertAdjacentHTML("beforeEnd", '<button class="delete-row">Delete</button>');
    }
}

//add site
function addNewSite() {
    var person = prompt("Наименование", "");
    if (!person) {
        alert("Введите наименование");
   }
   else {
        var table = document.getElementById("sites-table");
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(-1);
        cell1.innerHTML = person;
        cell1.className = "table-row";
        cell2.insertAdjacentHTML("beforeEnd", '<button class="delete-row">Delete</button>');
        console.log(row);

    }
}

//add key
function addNewKey() {
    var person = prompt("Наименование", "");
    if (!person) {
        alert("Введите наименование");
   }
   else {
        var table = document.getElementById("key-words-table");
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(-1);
        cell1.innerHTML = person;
        cell1.className = "table-row";
        cell2.insertAdjacentHTML("beforeEnd", '<button class="delete-row">Delete</button>');
    }
}


//delete row button (for all catalogs)
var deleteRow =  document.getElementsByClassName("delete-row");

for (var i = 0; i < deleteRow.length; i++) {
deleteRow[i].addEventListener('click', delFunction, false); //bind delFunction on click to eraseables
}

function delFunction(){        
    var msg = confirm("Вы хотите удалить элемент?");      
    if (msg == true) { 
    var test = this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
                        //remove the clicked element if confirmed
    
    }   
};



// -------------edit row function for Persons table-------------------------
var table = document.getElementById('persons-table');

var editingTd;

table.onclick = function(event) {

    var target = event.target;

    if (target.className == 'edit-cancel') {
      finishTdEdit(editingTd.elem, false);
      return;
    }

    if (target.className == 'edit-ok') {
      finishTdEdit(editingTd.elem, true);
      return;
    }

    if (target.nodeName == 'TD') {
      if (editingTd) return; // already editing

      makeTdEditable(target);
      return;

    target = target.parentNode;
    }
}

function makeTdEditable(td) {
  editingTd = {
    elem: td,
    data: td.innerHTML
};

td.classList.add('edit-td'); // td, not textarea! the rest of rules will cascade

var input = document.createElement('input');
input.style.width = td.clientWidth + 'px';
input.style.height = td.clientHeight + 'px';
input.className = 'edit-area';

input.value = td.innerText;
td.innerHTML = '';
td.appendChild(input);
input.focus();

td.insertAdjacentHTML("beforeEnd",
'<div class="edit-controls"><button class="edit-ok">OK</button><button class="edit-cancel">CANCEL</button></div>'
);
}

function finishTdEdit(td, isOk) {
  if (isOk) {
    td.innerHTML = td.firstChild.value;
  } else {
    td.innerHTML = editingTd.data;
  }
  td.classList.remove('edit-td'); // remove edit class
  editingTd = null;
}
// -------------edit row function for Persons table-------------------------



// -------------edit row function for Sites table-------------------------
var table = document.getElementById('sites-table');

var editingTd;

table.onclick = function(event) {

    var target = event.target;

    if (target.className == 'edit-cancel') {
      finishTdEdit(editingTd.elem, false);
      return;
    }

    if (target.className == 'edit-ok') {
      finishTdEdit(editingTd.elem, true);
      return;
    }

    if (target.nodeName == 'TD') {
      if (editingTd) return; // already editing

      makeTdEditable(target);
      return;

    target = target.parentNode;
    }
}

function makeTdEditable(td) {
  editingTd = {
    elem: td,
    data: td.innerHTML
};

td.classList.add('edit-td'); // td, not textarea! the rest of rules will cascade

var input = document.createElement('input');
input.style.width = td.clientWidth + 'px';
input.style.height = td.clientHeight + 'px';
input.className = 'edit-area';

input.value = td.innerText;
td.innerHTML = '';
td.appendChild(input);
input.focus();

td.insertAdjacentHTML("beforeEnd",
'<div class="edit-controls"><button class="edit-ok">OK</button><button class="edit-cancel">CANCEL</button></div>'
);
}

function finishTdEdit(td, isOk) {
  if (isOk) {
    td.innerHTML = td.firstChild.value;
  } else {
    td.innerHTML = editingTd.data;
  }
  td.classList.remove('edit-td'); // remove edit class
  editingTd = null;
}
// -------------edit row function for Sites table-------------------------



// -------------edit row function for key-words table-------------------------
var table = document.getElementById('key-words-table');

var editingTd;

table.onclick = function(event) {

    var target = event.target;

    if (target.className == 'edit-cancel') {
      finishTdEdit(editingTd.elem, false);
      return;
    }

    if (target.className == 'edit-ok') {
      finishTdEdit(editingTd.elem, true);
      return;
    }

    if (target.nodeName == 'TD') {
      if (editingTd) return; // already editing

      makeTdEditable(target);
      return;

    target = target.parentNode;
    }
}

function makeTdEditable(td) {
  editingTd = {
    elem: td,
    data: td.innerHTML
};

td.classList.add('edit-td'); // td, not textarea! the rest of rules will cascade

var input = document.createElement('input');
input.style.width = td.clientWidth + 'px';
input.style.height = td.clientHeight + 'px';
input.className = 'edit-area';

input.value = td.innerText;
td.innerHTML = '';
td.appendChild(input);
input.focus();

td.insertAdjacentHTML("beforeEnd",
'<div class="edit-controls"><button class="edit-ok">OK</button><button class="edit-cancel">CANCEL</button></div>'
);
}

function finishTdEdit(td, isOk) {
  if (isOk) {
    td.innerHTML = td.firstChild.value;
  } else {
    td.innerHTML = editingTd.data;
  }
  td.classList.remove('edit-td'); // remove edit class
  editingTd = null;
}
// -------------edit row function for key-words table-------------------------
