const server_url = 

document.getElementById("get-home").addEventListener("click", function(event) {
    event.preventDefault();

    fetch("HTTP://ec2-13-43-90-147.eu-west-2.compute.amazonaws.com")
        console.log("Sending GET request")
        .then(response =>{
            if(!response.ok) {
                throw new Error ("Request was not ok"& response.statusText)
            }
            console.log("Responce recived")
            return response.text();
        })
        .then (html => {
            document.getElementById("card-container").innerHTML = html;
            console.log("Homepage requested and recived")
        })
        .catch(error => {
            console.error("There was a problem witht he get request")
        })
})