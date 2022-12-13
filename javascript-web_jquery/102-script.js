$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang_code = $('INPUT#language_code').val();
    $.get(
      `https://stefanbohacek.com/hellosalut/?lang=${lang_code}`,
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  });
});
