$('.commonstat').click(function() {
  $('.common-stats').show();
  $('.daily-stats').hide();
  $(this).addClass('active').siblings().removeClass('active');
  //$(this).addClass('active').siblings().removeClass('active');
});
$('.dailystat').click(function() {
  $('.daily-stats').show();
  $('.common-stats').hide();
  $(this).addClass('active').siblings().removeClass('active');
});