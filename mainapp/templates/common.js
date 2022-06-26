let inEditMode = false;
let changeButton = document.getElementById("changeBtn");

function onEditModeEnter() {}
function onEditModeExit() {}

changeButton.onclick = function () {
    if(inEditMode) {
        onEditModeExit()
        changeButton.classList.remove("btn-success");
        changeButton.classList.add("btn-outline-success");
    }
    else {
        onEditModeEnter()
        changeButton.classList.remove("btn-outline-success");
        changeButton.classList.add("btn-success");
    }
    inEditMode = !inEditMode;
}

function hide (element) {
    let classList = element.classList;
    if (!classList.contains("hidden"))
        classList.add("hidden");
}

function show (element) {
    element.classList.remove("hidden");
}
