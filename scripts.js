document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('get-home').addEventListener("click", function(event) {
        event.preventDefault();

        console.log("Sending GET request");

        fetch("http://localhost:8000")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Request was not ok: " + response.status);
                }
                console.log("Response received");
                return response.text();
            })
            .then(html => {
                console.log("Card Container Found:", cardContainer);
                console.log('HTML found:', html)
                document.querySelector("#cardContainer").innerHTML = html;
                console.log("Homepage requested and received");
            })
            .catch(error => {
                console.error("There was a problem with the GET request:", error);
            });
    });
});