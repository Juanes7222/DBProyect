
// select.addEventListener("change", selectView)

// function selectView(){
//     select.ajax()
// }

let csrfToken = $("input[name='csrfmiddlewaretoken']").val();


function reloadPage(files, dates){
    let imgContainer = document.getElementById("img-container")
    imgContainer.innerHTML = ""
    for (let i=0; i<files.length; i++){
        console.log(files[i])
        let newImgElement = document.createElement("img") //, `src="{% static "${response[i]}" %}" class="img-fluid rounded" alt="wheel of life"`
        newImgElement.setAttribute("src", `/${files[i]}`)
        newImgElement.setAttribute("class", "img-fluid rounded")
        newImgElement.setAttribute("alt", "wheel of life")

        let newDivElement = document.createElement("div")
        newDivElement.setAttribute("class", "alert alert-info")
        newDivElement.setAttribute("role", "alert")
        let textContent = document.createTextNode(`Fecha: ${dates[i]}`)
        newDivElement.appendChild(textContent)

        imgContainer.appendChild(newDivElement)
        imgContainer.appendChild(newImgElement)
    }
}


function mostrarToast() {
    // Crea un elemento de toast utilizando Bootstrap
    let myToastEl = document.getElementById('myToast');
    let myToast = new bootstrap.Toast(myToastEl);
    myToast.show();

  }
  

$(document).ready(function() {
    $("#select-view").change(function() {
        // Realizar una solicitud AJAX al backend
        let select = document.getElementById("select-view")
        let date = new Date()
        let selectValue = parseInt(select.value)
        console.log(selectValue)
        let dateValue
        if (selectValue == 1)
            date.setDate(date.getDate() - 7)
        else if (selectValue == 2)
            date.setMonth(date.getMonth() - 1)
        else if (selectValue == 3)
            date.setMonth(date.getMonth() - 2)
        else if (selectValue == 4)
            dateValue = "all"  
        if (dateValue != "all")
            dateValue = date.toISOString()
        console.log(dateValue)

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
                console.log("Respuesta del servidor:", response);
                reloadPage(response["files"], response["dates"]);

            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });

    $(".button-message").click(function(){
        let formId = $(this).attr("name")
        console.log(formId)
        let title = $(`#title_${formId}`).val();
        let message = $(`#message-text_${formId}`).val();

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

    $("#back-button").click(function() {
        window.history.back();
    });

});

