document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const schClass = document.getElementById('class').value;

    const data = {
        username: username,
        password: password,
        first_name: firstName,
        last_name: lastName,
        sch_class: schClass
    };

    fetch('http://188.92.199.214:7555/api/v1/users/register'/*'https://zwloader.ru/api/v1/chat/'*/, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert('Регистрация прошла успешно!');
        window.location.href = "http://zwloader.ru/login/";
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Произошла ошибка при регистрации. Попробуйте еще раз.');
    });


});
const loginButton = document.getElementById('login-button');
loginButton.addEventListener('click', function() {
    window.location.href = "http://zwloader.ru/login/";
});