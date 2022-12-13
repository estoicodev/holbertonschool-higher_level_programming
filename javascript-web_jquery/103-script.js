function translateHello () {
  const lang_code = $('INPUT#language_code').val();
  $.get(
    `https://stefanbohacek.com/hellosalut/?lang=${lang_code}`,
    function (data) {
      $('DIV#hello').html(data.hello);
    }
  );
}

$('document').ready(function () {
  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translateHello();
      }
    });
  });
});
