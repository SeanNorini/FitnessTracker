const settings = document.querySelector(".form_container");

settings.addEventListener("submit", (e) =>{
    e.preventDefault();

    // Pull data from form
    const formElements = document.querySelector("#settings_form").querySelectorAll("input");
    const formData = new FormData();
    formElements.forEach((element) => {
        formData.append(element.name, element.value);
    });

    const gender = document.querySelector("#id_gender_0");
    if (gender.checked) {
      formData.set("gender", gender.value);
    }
    // Add CSRF token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('csrfmiddlewaretoken', csrftoken)

    // Send form, redirect to index on success otherwise display error.
    const errorOutput = document.querySelector('#form-error')
    fetch('./settings', {
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
        errorOutput.innerText = "Sorry! There was an error updating your information. ";
    });

});

settings.addEventListener("click", (e) => {
    if (e.target.id === "edit_workouts"){
        fetch("../edit_workouts", {method:"GET"})
        .then(response => response.text())
        .then(template => {
            const container = document.querySelector(".form_container");
            const token = container.querySelector("[name=csrfmiddlewaretoken]");
            container.innerHTML = "";
            container.appendChild(token);
            const editForm = document.createElement("template");
            editForm.innerHTML = template.trim();    
            container.appendChild(editForm.content);
        });
    }

    if (e.target.id === "done_editing"){
        console.log("test");
        fetch("user_settings", {method:"GET"})
        .then(response => response.text())
        .then(template => {
            const container = document.querySelector(".form_container");
            const token = container.querySelector("[name=csrfmiddlewaretoken]");
            container.innerHTML = "";
            container.appendChild(token);
            const editForm = document.createElement("template");
            editForm.innerHTML = template.trim();    
            container.appendChild(editForm.content);
        });
    }

    if (e.target.classList.contains("delete_exercise")){
        e.target.closest(".exercise_container").remove(); 

        if (!document.querySelector(".add_set")){
            set_message("Please select a workout or add an exercise to get started.");
        }
    } 
    
    if (e.target.classList.contains("add_set")){
        
        fetch("../add_set", {method: "GET"})
        .then(response => response.text())
        .then( template => {
            const setRow = document.createElement("template");
            setRow.innerHTML = template.trim();
            const container = e.target.closest(".exercise_container");
            container.querySelector(".sets").appendChild(setRow.content.firstChild);
            update_set_number(container);
        })
    }

    if (e.target.classList.contains("add_exercise")){
        const exercise = document.querySelector(".exercise").value;
        const exercises = document.querySelector("#exercises");

        fetch(("../add_exercise/") + exercise, {method: "GET"})
        .then(response => response.text())
        .then(template => {
            const exercise = document.createElement("template");
            exercise.innerHTML = template.trim();    
            exercises.appendChild(exercise.content.firstChild);
        });

        const placeholder = document.querySelector("#placeholder");
        if (placeholder){placeholder.remove();}
    }

    if (e.target.classList.contains("delete_set")){
        e.target.closest(".set").remove();
    }

    if (e.target.classList.contains("save_workout")){
        // Check for workout to save
        const exercises = document.querySelectorAll(".exercise_name");
        if (exercises.length == 0){
            set_message("You must add at least one exercise before saving a workout.");
            return
        }

        console.log("test");
        // Create form to gather data
        const workout = new FormData();
        const workoutName = window.prompt("Please enter the workout name:");
        const workouts = document.querySelector(".workout");

        let duplicate = false;
        for (let i = 0; i < workouts.options.length; i++){
            if (workouts.options[i].value == workoutName){
                duplicate = true;
            }  
        }

        if (duplicate){
            const confirm = window.confirm("This will override the previously saved workout, " + workoutName + ". Are you sure?");   
            if (!confirm){
                return;
            }
        }

        selectOption = document.createElement("option");
        selectOption.value = workoutName;
        selectOption.innerText = workoutName;
        workouts.appendChild(selectOption);

        workout.append("name", workoutName);

        // Get exercise sets
        const sets = document.querySelectorAll(".set");
        const setWeights= [];
        const setReps = [];
        const setExercises = [];
        sets.forEach(element => {
            const exercise = element.closest(".exercise_container").querySelector("#exercise_name");
            setExercises.push(exercise.textContent.trim());

            const weight = element.querySelector(".weight").value;
            setWeights.push(weight);

            const reps = element.querySelector(".reps").value;
            setReps.push(reps);
        });
        workout.append("exercises", setExercises);
        workout.append("weights", setWeights);
        workout.append("reps", setReps);
 
        // Add CSRF token
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        workout.append('csrfmiddlewaretoken', csrftoken);

        // Send workout data and display response
        fetch("../save_workout", {method: "POST", body: workout})
        .then(response => response.text())
        .then(data => {
            if (data.success){
                set_message("Workout saved.");
            }
        });
    }
});

function update_set_number(container) {
    const sets = container.querySelectorAll(".set");
    const test = sets[sets.length - 1].querySelector(".set_number").innerText = "Set " + sets.length + ":";

    }

function set_message(message) {
    if (!document.querySelector("#placeholder")){
        const placeholder = document.createElement("div")
        placeholder.id = "placeholder";
        placeholder.style.minHeight = "15rem";
        placeholder.style.display = "flex";
        placeholder.style.alignItems = "center";
        placeholder.style.justifyContent ="center";
        document.querySelector("#exercises").prepend(placeholder);
    }

    placeholder.innerText = message;
}

settings.addEventListener("change", (e) => {
    if (e.target.classList.contains("workout")){
        workout = document.querySelector(".workout").value;
        if (workout == "custom"){
            return
        }

        const confirm = window.confirm("Any unsaved changes will be lost, are you sure?")

        if (confirm){
            fetch("../select_workout/" + workout, {method:"GET"})
            .then(response => response.text())
            .then(workoutHTML => {
                const exercises = document.querySelector("#exercises");
                exercises.innerHTML = workoutHTML;
            });
        }
    }
});

