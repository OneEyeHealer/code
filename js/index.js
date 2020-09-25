fetch("./assets/code.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log("error: " + err);
    });

function appendData(data) {
    var mainContainer = document.getElementById("myData");
    for (var i = 0; i < data.length; i++) {
        // crating dom elements
        var div = document.createElement("div");
        var card = document.createElement("div");
        var image = document.createElement("img");
        var card_body = document.createElement("div");
        var heading = document.createElement("h5");
        var anchor = document.createElement("a");
        var para = document.createElement("p");
        var file_info = document.createElement("div");

        // styling
        div.classList.add("col", "mb-4");
        card.classList.add("card");
        image.classList.add("d-inline-block", "mr-2", "logo");
        card_body.classList.add("card-body", 'text-align');
        anchor.classList.add("title-anchor")
        heading.classList.add("card-title", "d-inline-block");
        para.classList.add("card-text");
        file_info.classList.add("file-info", "text-center");
        // fetching data
        heading.innerHTML = data[i].data.statement;
        // para.innerHTML = data[i].data.p;
        //   seting values
        image.src = './assets/img/logo.svg';
        image.setAttribute("width", "25");
        anchor.href = data[i].data.url;

        // appending created dom elements.
        mainContainer.append(div);
        div.append(card);
        card.append(card_body);
        // card_body.appendChild(image);
        card_body.appendChild(anchor);
        anchor.appendChild(image);
        anchor.append(heading);
        // card_body.appendChild(para);
        for (let [key, value] of Object.entries(data[i].data.details)) {
            let classes = "";
            let icon = "";
            //   classes += key === "github" ? "text-secondary" : "text-success";
            //  text-colors
            if (key === "Github") classes += "text-secondary";
            else if (key === "Download") classes += "text-success";
            else classes += "text-info";
            // icons
            if (key === "Github") icon += `<i class="fab fa-github" aria-hidden="true"></i>`;
            else if (key === "Download") icon += `<i class="fas fa-file-download"; aria-hidden="true"></i>`;
            else icon += `<i class="fab fa-readme"></i>`;
            //   icon +=
            //     key === "github" ?
            //     `<i class="fab fa-github" aria-hidden="true"></i>` :
            //     `<i class="fas fa-code"; aria-hidden="true"></i>`;
            var links = document.createElement("a");
            var span = document.createElement("span");
            links.href = value;
            links.setAttribute("target", "_blank");
            links.classList.add(classes);
            span.classList.add("iconPos");
            span.innerHTML = icon + " " + key;
            card_body.append(file_info);
            file_info.appendChild(links);
            links.appendChild(span);
        }
    }
}