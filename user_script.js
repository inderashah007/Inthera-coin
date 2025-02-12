function getITC() {
    var userId = document.getElementById('user_id').value;
    fetch(`http://localhost:5000/get_itc?user_id=${userId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('itc_amount').innerText = data.itc;
        })
        .catch(error => console.error('Error:', error));
}
