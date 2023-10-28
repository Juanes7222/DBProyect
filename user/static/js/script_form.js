let csrfToken = $("input[name='csrfmiddlewaretoken']").val();


function addListenerDate(){
    $("#select-view").off("change")
    $("#select-view").change(function() {
        // Realizar una solicitud AJAX al backend
        let select = document.getElementById("select-view")
        let date = new Date()
        let selectValue = parseInt(select.value)
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
                reloadPage(response["files"], response["dates"], response["forms_ids"]);
            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });
}


function addListenerButton(){
    $(".button-message").off("click")
    $(".button-message").click(function(){
        let formId = $(this).attr("name")

        $.ajax({
            url: `get_message/${formId}`,
            method: "GET",
            success: function(response) {
                showMessage(response, formId)
            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        })
    })
}

function addListenerBack(){
    $("#back-button").click(function() {
        window.history.back();
    });
}


function reloadPage(files, dates, formsIds){
    let imgContainer = document.getElementById("img-container")
    imgContainer.innerHTML = ""
    for (let i=0; i<files.length; i++){
        let newImgElement = document.createElement("img")
        newImgElement.setAttribute("src", `${files[i]}`)
        newImgElement.setAttribute("class", "img-fluid rounded")
        newImgElement.setAttribute("alt", "wheel of life")

        let newDivElement = document.createElement("div")
        newDivElement.setAttribute("class", "alert alert-info")
        newDivElement.setAttribute("role", "alert")
        let textContent = document.createTextNode(`Fecha: ${dates[i]}`)
        newDivElement.appendChild(textContent)

        let newButton = document.createElement("button")
        let newModal = document.createElement("div")

        newButton.setAttribute("class", "btn btn-primary button-message")
        newButton.setAttribute("name", `${formsIds[i]}`)
        newButton.setAttribute("data-bs-toggle", "modal")
        newButton.setAttribute("data-bs-target", `#messagemodal_${formsIds[i]}`)

        let textButton = document.createTextNode("Ver comentarios")
        newButton.appendChild(textButton)

        newModal.setAttribute("class", "modal fade")
        newModal.setAttribute("id", `messagemodal_${formsIds[i]}`)
        newModal.setAttribute("tabindex", "-1")
        newModal.setAttribute("aria-labelledby", "messagemodallabel")
        newModal.setAttribute("aria-hidden", "true")

        newModal.innerHTML = `
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 id="title_${formsIds[i]}" class="modal-title"></h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <p id="message-text_${formsIds[i]}"></p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
        `

        imgContainer.appendChild(newDivElement)
        imgContainer.appendChild(newImgElement)
        imgContainer.appendChild(newButton)
        imgContainer.appendChild(newModal)

    }
    addAllListeners()
    // addListenerButton()
}


function mostrarToast() {
    // Crea un elemento de toast utilizando Bootstrap
    let myToastEl = document.getElementById('myToast');
    let myToast = new bootstrap.Toast(myToastEl);
    myToast.show();

}

function showMessage(response, formId){
    let title = document.getElementById(`title_${formId}`)
    let message = document.getElementById(`message-text_${formId}`)

    let textTitle = response["title"]
    let textMessage = response["message"]

    if (textTitle == null){
        textTitle = ""
        textMessage = "Nada todavia"

    }
    message.textContent = ""
    title.textContent = ""

    let textContentTitle = document.createTextNode(`Titulo: ${textTitle}`)
    let textContentMessage = document.createTextNode(`${textMessage}`)

    title.appendChild(textContentTitle)
    message.appendChild(textContentMessage)
    
    addAllListeners()

}

function addAllListeners(){
    $(document).ready(function(){
    addListenerDate()
    addListenerButton()
    addListenerDate()
})
}

addAllListeners()


