 
function formatText(command, value = null) {
    document.execCommand(command, false, value);
}

function insertLink() {
    var url = prompt("Enter the URL:");
    if (url) {
        document.execCommand("createLink", false, url);
    }
}

function handleInput() {
    var textArea = document.getElementById('text-area');
    var placeholder = textArea.getAttribute('data-placeholder');

    if (textArea.textContent.trim() === '') {
      textArea.innerHTML = '<span style="color: #888;">' + placeholder + '</span>';
    } else {
      textArea.innerHTML = textArea.textContent;
    }
  }
 
