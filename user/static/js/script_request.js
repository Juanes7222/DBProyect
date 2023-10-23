
$(document).ready(function() {
    $(".request").click(function(){
        let id = $(this).attr("id")
        let user = $(this).attr("name")
        console.log(id, user)
        
        $.ajax({
            url: "save-message/",
            method: "POST",
            data: {
                // Datos que deseas enviar al backend
                csrfmiddlewaretoken: csrfToken,
                title: title,
                message: message,
                form_id: formId
            },
            success: function(response) {
                console.log("Respuesta del servidor:", response);
                mostrarToast()
            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        })
    })
})