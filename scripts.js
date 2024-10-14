
document.getElementById("get-home").addEventListener("click", function(event) {
    event.preventDefault();

    console.log("Sending GET request")

    fetch("http://ec2-13-43-90-147.eu-west-2.compute.amazonaws.com")
        
        .then(response =>{
            if(!response.ok) {
                throw new Error ("Request was not ok" + response.statusText)
            }
            console.log("Response received")
            return response.text();
        })
        .then (html => {
            document.getElementById("card-container").innerHTML = html;
            console.log("Homepage requested and received")
        })
        .catch(error => {
            console.error("There was a problem witht he get request")
        })
})