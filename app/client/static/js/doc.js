 
function formatText(command, value = null) {
    document.execCommand(command, false, value);
}

function insertLink() {
    var url = prompt("Enter the URL:");
    if (url) {
        document.execCommand("createLink", false, url);
    }
}  
 
function updateHiddenInput() { 
  let textAreaContent = document.getElementById('text-area').innerText; 
  document.getElementById('document_content_input').value = textAreaContent;
}
 
