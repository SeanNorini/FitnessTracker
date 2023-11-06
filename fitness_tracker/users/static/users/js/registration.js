document.getElementById("registration_form").addEventListener("submit", (e) =>{
    e.preventDefault();

    // Pull data from form
    const formElements = document.querySelector("#registration_form").querySelectorAll("input");
    const formData = new FormData();
    formElements.forEach((element) => {
        formData.append(element.name, element.value)
    });

    // Add CSRF token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('csrfmiddlewaretoken', csrftoken)

    const errorOutput = document.querySelector('#form-error')

    // Send form, redirect to index on success otherwise display error.
    fetch('./registration', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) 
        {
            window.location.href = "";
        }
        else
        {
            errorOutput.innerText = data['message'];
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorOutput.innerText = "Sorry! There was an error submitting your registration. "
    });   
});

