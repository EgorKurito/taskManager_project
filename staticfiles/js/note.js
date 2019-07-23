$(document).ready(function() {

  var csrftoken = $("input[name=csrfmiddlewaretoken]").val()

  $('#sort').change(function() {
    $.ajax({
      type: 'POST',
      url: 'filters/',
      data: {
        "sort": $('#sort').val(),
        "csrfmiddlewaretoken": csrftoken
      },
      success: show_notes,
    })
  })

  $('#filter').change(function() {
    $.ajax({
      type: 'POST',
      url: 'filters/',
      data: {
        "filter": $('#filter').val(),
        "csrfmiddlewaretoken": csrftoken
      },
      success: show_notes,
    })
  })

  $('#query').keyup(function() {
    $.ajax({
      type: 'POST',
      url: 'filters/',
      data: {
        "query": $('#query').val(),
        "csrfmiddlewaretoken": csrftoken
      },
      success: show_notes,
    })
  })

  function show_notes(data) {
    console.log(data);
    $('#list').html(data);
}

});
