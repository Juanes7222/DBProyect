

let csrfToken = $("input[name='csrfmiddlewaretoken']").val();

$(document).ready(function() {
    $("#integrate").click(function() {
        // Realizar una solicitud AJAX al backend
        let userId = "{{ user_id }}";
        let psiId = "{{ psi_id }}";
        $.ajax({
            url: "integrate/",
            method: "POST",
            data: {
                // Datos que deseas enviar al backend
                csrfmiddlewaretoken: csrfToken,
                user_id: userId,
                psi_id: psiId 
            },
            success: function(response) {
                // Manejar la respuesta del backend
                let cont = document.getElementById("cont")
                cont.innerHTML = ""
                let newElement = document.createElement("h2")
                newElement.setAttribute("role", "alert")
                if (response["result"]){
                    newElement.setAttribute("class", "alert alert-success")
                    let textContent = document.createTextNode("Realizado con exito")
                    newElement.appendChild(textContent)
                }
                else{
                    newElement.setAttribute("class", "alert alert-danger")
                    let textContent = document.createTextNode("Ya te encuentras integrado")
                    newElement.appendChild(textContent)
                }
                

            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });
})