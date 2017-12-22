$(document).ready(function () {

    // $("#urlForm").submit(function(event) {
    //     event.preventDefault();
    //
    //     $.ajax({
    //         url: '/api/v0.0/createcover',
    //         type: 'GET',
    //         data: $("#urlForm").serialize()
    //     })
    // })

    $("#addTag").click(function () {
        $.ajax({
            url: '/api/v0.0/addtag',
            type: 'GET',
            data: {tag: $("#tagInput").val()},
            success: function (payload) {
                if (payload) {
                    $("#tagList").append("<div class=\"tag\">" + payload +
                        "<span aria-hidden=\"true\" class=\"removeTag\">&times;</span></div>")
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
