let comments = document.getElementsByName('comment');
let commentContainer = document.getElementById('comment-container');

let deleteButtons = []

for(let i = 0; i < comments.length; i++) {
    let comment = comments[i];
    // crappy way to do it, but it works
    let deleteButton = comment.childNodes[1].childNodes[3].childNodes[7];
    deleteButton.onclick = function() {
        commentContainer.removeChild(comment);
        console.log(comments)
    }
    deleteButtons.push(deleteButton);
}

function showDeleteButtons() {
    for(let i = 0; i < deleteButtons.length; i++) {
        show(deleteButtons[i]);
    }
}

function hideDeleteButtons() {
    for(let i = 0; i < deleteButtons.length; i++) {
        hide(deleteButtons[i]);
    }
}