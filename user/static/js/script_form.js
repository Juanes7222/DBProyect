
// select.addEventListener("change", selectView)

// function selectView(){
//     select.ajax()
// }

let csrfToken = $("input[name='csrfmiddlewaretoken']").val();

// import fetch from 'fetch'

// // Descarga el archivo ZIP
// fetch('/backend/generate_zip').then(response => {
//     // Obtiene el archivo ZIP como un objeto Blob
//     const blob = response.blob()

//     // Descarga el archivo ZIP
//     const url = window.URL.createObjectURL(blob)
//     const a = document.createElement('a')
//     a.href = url
//     a.download = 'archivo.zip'
//     a.click()
// })

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
        let textContent = document.createTextNode(dates[i])
        newDivElement.appendChild(textContent)

        imgContainer.appendChild(newDivElement)
        imgContainer.appendChild(newImgElement)
    }
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

    // $("#all").click(function() {
    //     // Realizar una solicitud AJAX al backend
    //     $.ajax({
    //         url: "download_wheels/",
    //         method: "GET",
    //         dataType: "blob",
    //         data: {
    //             // Datos que deseas enviar al backend
    //             csrfmiddlewaretoken: csrfToken,
    //             date: "all"
    //         },
    //         headers: {
    //             // Especifica el tipo de archivo MIME en el encabezado `Content-Type`
    //             "Content-Type": "application/zip"
    //         },
    //         success: function(data) {
    //             let blob = new Blob([data]);
    //             let url = window.URL.createObjectURL(blob);
    //             let link = document.createElement('a');
    //             link.style = "none"
    //             link.href = url;
    //             link.download = 'archivo.zip'; // Nombre del archivo ZIP
    
    //             // Simula un clic en el enlace para iniciar la descarga
    //             link.click();
    //             window.URL.revokeObjectURL(url);
    
    //         },
    //         error: function(xhr, errmsg, err) {
    //             console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
    //         }
    //     });
    // });

    $("#all").click(function() {
        // Realizar una solicitud AJAX al backend
        $.ajax({
            url: "download_wheels/",
            method: "GET",
            datatype: "blob",
            data: {
                // Datos que deseas enviar al backend
                csrfmiddlewaretoken: csrfToken,
                date: "all"
            },
            success: function(data) {
                let blob = new Blob([data], { type: 'application/zip' });
                let url = window.URL.createObjectURL(blob);
                let link = document.createElement('a');
                link.style = "none"
                link.href = url;
                link.download = 'archivo.zip'; // Nombre del archivo ZIP

                // Simula un clic en el enlace para iniciar la descarga
                link.click();
                window.URL.revokeObjectURL(url);

            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });

    $("#date").click(function() {
        // Realizar una solicitud AJAX al backend
        let date = document.getElementById("value-date").value

        $.ajax({
            url: "download_wheels/",
            method: "GET",
            datatype: "arraybuffer",
            data: {
                // Datos que deseas enviar al backend
                csrfmiddlewaretoken: csrfToken,
                date: date.value
            },
            success: function(data) {
                // Manejar la respuesta del backend
                // console.log("Respuesta del servidor:", data);
                // reloadPage(response["files"], response["dates"]);
                // Manejar la respuesta del backend aquí
                // Descargar el archivo ZIP
                let blob = new Blob([data], { type: 'application/zip' });
                let url = window.URL.createObjectURL(blob);
                let link = document.createElement('a');
                link.style = "none"
                link.href = url;
                link.download = 'archivo.zip'; // Nombre del archivo ZIP

                // Simula un clic en el enlace para iniciar la descarga
                link.click();
                window.URL.revokeObjectURL(url);

            },
            error: function(xhr, errmsg, err) {
                console.log("Error:", errmsg, "err: ", err, "xhr: ", xhr);
            }
        });
    });
});

