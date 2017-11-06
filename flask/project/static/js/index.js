$(document).ready(function() {

    $("#urlForm").submit(function(event) {
        event.preventDefault();
        
        $.ajax({
            url: '/api/v0.0/createcover',
            type: 'POST',
            data: $("#urlForm").serialize(),
            success: function(data) {
                console.log(data)
            }
        })
    })
});
