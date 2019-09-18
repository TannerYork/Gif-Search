const searchBar = document.getElementById('search-input');
const https = new XMLHttpRequest();
const url = '/typeahead';

searchBar.addEventListener('input', (event) => {
    https.open('POST', url, true)
    https.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    https.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           document.getElementById('content').innerHTML = this.responseText;
        }
    }
    https.send(`user_input= ${searchBar.value}`)
})