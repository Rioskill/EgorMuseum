{% include 'common.js' %}

let png = document.getElementById("vandalism");
png.onclick = function () {
    if (inEditMode)
        this.parentNode.removeChild(this);
}