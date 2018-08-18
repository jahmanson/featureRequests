$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
      data: {
        title: $('#title').val(),
        description: $('#description').val(),
        client: $('#client').val(),
        priority: $('#priority').val(),
        targetDate: $('#targetDate').val(),
        productArea: $('#productArea').val()
      },
      url: '/add_request',
      type: 'POST'
    }).done(function(data) {
        
    }).fail(function() {

    }); //end of ajax
  }) // end of form submit
})
