$(document).ready(function() {
  $('.find-many-persons').click(function() {
    if ($(this).prop('checked')) {
      $('.find-many-sites').prop('checked', false);
      $('.person-sites select').add('.person-sites input').not('.find-many-sites').prop('disabled', true);
      $('.site-persons select').add('.site-persons input').prop('disabled', false);
    } else {
      $('.site-persons select').add('.site-persons input').not('.find-many-persons').prop('disabled', true);
    }
  });
  
  $('.find-many-sites').click(function() {
    if ($(this).prop('checked')) {
      $('.find-many-persons').prop('checked', false);
      $('.site-persons select').add('.site-persons input').not('.find-many-persons').prop('disabled', true);
      $('.person-sites select').add('.person-sites input').prop('disabled', false);
    } else {
      $('.person-sites select').add('.person-sites input').not('.find-many-sites').prop('disabled', true);
    }
  });
  
  
});