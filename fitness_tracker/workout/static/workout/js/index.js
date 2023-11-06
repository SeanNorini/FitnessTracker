const controls = document.querySelector("#workout_form");

controls.addEventListener("click", function(e) {
    e.preventDefault();

    if (e.target.classList.contains("delete_exercise")){
        e.target.closest(".exercise_container").remove(); 

        if (!document.querySelector(".add_set")){
          const placeholder = document.createElement("div");
          placeholder.innerText = "Please select an exercise routine or add an exercise to get started.";
          placeholder.id = "placeholder";
          placeholder.style.minHeight = "15rem";
          placeholder.style.display = "flex";
          placeholder.style.alignItems = "center";
          placeholder.style.justifyContent ="center";
          document.querySelector("#exercises").prepend(placeholder);
        }
    } 
    
    if (e.target.classList.contains("add_set")){
        
        fetch("add_set", {method: "GET"})
        .then(response => response.text())
        .then( setData => {
            let setRow = document.createElement("template");
            setRow.innerHTML = setData.trim();
            container = e.target.closest(".exercise_container");
            container.querySelector(".sets").appendChild(setRow.content.firstChild);
            update_set_number(container);
        })
    }

    if (e.target.classList.contains("add_exercise")){
        const exercise = document.querySelector("[name=exercise]").value;
        const exercises = document.querySelector("#exercises");

        fetch(("add_exercise/") + exercise, {method: "GET"})
        .then(response => response.text())
        .then(html => {      
            exercises.innerHTML += html;
        });

        const placeholder = document.querySelector("#placeholder");
        if (placeholder){placeholder.remove();};
    }

    if (e.target.classList.contains("delete_set")){
        e.target.closest(".set").remove();
    }

});

function update_set_number(container) {
    const sets = container.querySelectorAll(".set");
    console.log(sets);
    let setNumber = 1;
    sets.forEach(element => {
        element.querySelector(".set_number").innerText = "Set " + setNumber + ":";  
        console.log(setNumber)
        setNumber++;
        
    });
}