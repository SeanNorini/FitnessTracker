const controls = document.querySelector("#workout_form");

controls.addEventListener("click", (e) => {
    e.preventDefault();

    if (e.target.classList.contains("delete_exercise")){
        e.target.closest(".exercise_container").remove(); 

        if (!document.querySelector(".add_set")){
            set_message("Please select an exercise routine or add an exercise to get started.");
        }
    } 
    
    if (e.target.classList.contains("add_set")){
        
        fetch("add_set", {method: "GET"})
        .then(response => response.text())
        .then( set_template => {
            const setRow = document.createElement("template");
            setRow.innerHTML = set_template.trim();
            const container = e.target.closest(".exercise_container");
            container.querySelector(".sets").appendChild(setRow.content.firstChild);
            update_set_number(container);
        })
    }

    if (e.target.classList.contains("add_exercise")){
        const exercise = document.querySelector(".exercise").value;
        const exercises = document.querySelector("#exercises");

        fetch(("add_exercise/") + exercise, {method: "GET"})
        .then(response => response.text())
        .then(exercise_template => {
            const exercise = document.createElement("template");
            exercise.innerHTML = exercise_template.trim();    
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
            set_message("You must add at least one exercise before saving a workout session.");
            return
        }

        // Create form to gather data
        const workout = new FormData();

        // Get workout name
        const workoutName = document.querySelector(".workout").value;
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
        fetch("save_workout", {method: "POST", body: workout})
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

controls.addEventListener("change", (e) => {
    if (e.target.classList.contains("workout")){
        workout = document.querySelector(".workout").value;
        if (workout == "custom"){
            return
        }

        const confirm = window.confirm("This will erase the current workout session, are you sure?")

        if (confirm){
            fetch("select_workout/" + workout, {method:"GET"})
            .then(response => response.text())
            .then(workoutHTML => {
                const exercises = document.querySelector("#exercises");
                exercises.innerHTML = workoutHTML;
            });
        }
    }
});