$(document).ready(function () {
    //
    // $("#uploadCV").on('click', function() {
    //     $.ajax({
    //         type: 'POST',
    //         url: '/api/v0.0/uploadcv',
    //         data: new FormData($('#CVform')[0]),
    //
    //         success: function() {
    //
    //         }
    //     })
    // });

    $("#addTag").click(function () {
        $.ajax({
            url: '/api/v0.0/addtag',
            type: 'GET',
            data: {tag: $("#tagInput").val()},
            success: function (payload) {
                if (payload) {
                    $("#tagList").prepend("<div class=\"tag\">" + payload +
                        "<span aria-hidden=\"true\" class=\"removeTag\">&times;</span></div>")
                } else {
                    alert('error')
                }
            },
            failure: function (response) {
                console.log(response)
            }

        })
    });

    $("#tagList").on('click', '.removeTag', function() {
        var tag = $(this);
        $.ajax({
            url: '/api/v0.0/removeTag',
            type: 'GET',
            data: {tag: tag.prev().text().trim()},
            success: function (payload) {
                if (payload) {
                    tag.parent().remove()
                } else {
                    alert('error')
                }
            },
            failure: function (response) {
                console.log(response)
            }

        })
    })
});
