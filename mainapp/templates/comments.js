let comments = document.getElementsByName('comment');
// let commentContainer = document.getElementById('comment-container');

let deleteButtons = []

for(let i = 0; i < comments.length; i++) {
    let comment = comments[i];

    let commentContainer = comment.parentNode;

    let deleteButton = comment.childNodes[1].childNodes[3].childNodes[7];
    deleteButton.onclick = function() {
        commentContainer.removeChild(comment);
        console.log(comments)

         let xml_http = new XMLHttpRequest();
        xml_http.open("POST", "");

        xml_http.send('comment: ' + comment.id.substr(8));

        console.log('comment: ' + comment.id.substr(8));

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