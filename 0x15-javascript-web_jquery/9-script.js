let url = 'https://fourtonfish.com/hellosalut/';
$.get(url, 'lang=' + $('html').attr('lang'), function (data) {
  $('DIV#hello').text(data.hello);
});
