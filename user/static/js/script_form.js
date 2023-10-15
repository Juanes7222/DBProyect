
// select.addEventListener("change", selectView)

// function selectView(){
//     select.ajax()
// }
let csrfToken = $("input[name='csrfmiddlewaretoken']").val();

$(document).ready(function() {
    $("#select-view").change(function() {
        // Realizar una solicitud AJAX al backend
        let select = document.getElementById("select-view")
        let date = new Date()
        let selectValue = select.value
        // console.log(selectValue, date.getDate())
        let dateValue
        if (selectValue == 1)
            date.setDate(date.getDate() - 7)
        else if (selectValue == 2)
            date.setMonth(date.getMonth() - 1)
        else if (selectValue == 3)
            date.setMonth(date.getMonth() - 2)
        else if (selectValue == 4)
            dateValue = "all"    
        if (date != "all")
            dateValue = date.toISOString()

        $.ajax({
            url: "/forms_views/",
            method: "POST",
            data: {
                // Datos que deseas enviar al backend
                csrfmiddlewaretoken: csrfToken,
                date: dateValue
            },
            success: function(response) {
                // Manejar la respuesta del backend
                // console.log("Respuesta del servidor:", response);
            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });
});

