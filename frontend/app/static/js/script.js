document.addEventListener("DOMContentLoaded", () => {
    const schedule = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
    };

    const subjects = [
        "Математика",
        "Русский язык",
        "Физика",
        "Химия",
        "История",
        "Биология",
        "Информатика",
        "География"
    ];

    const topics = {
        "Математика": ["Алгебра", "Геометрия", "Тригонометрия"],
        "Русский язык": ["Грамматика", "Орфография", "Литература"],
        "Физика": ["Механика", "Оптика", "Электричество"],
        "Химия": ["Органическая химия", "Неорганическая химия", "Физическая химия"],
        "История": ["Древний мир", "Средние века", "Новая история"],
        "Биология": ["Ботаника", "Зоология", "Генетика"],
        "Информатика": ["Алгоритмы", "Программирование", "Сети"],
        "География": ["Физическая география", "Экономическая география", "Политическая география"]
    };

    const months = ["Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май"];

    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function spin() {
        document.getElementById("body").style.transform = "rotate(7200deg)";
        document.getElementById("body").style.transition = "5s";
    }

    function generateSchedule() {
        for (let day in schedule) {
            schedule[day] = [];
            const numberOfLessons = getRandomInt(5, 6);
            let usedSubjects = new Set();
            for (let i = 0; i < numberOfLessons; i++) {
                let subject;
                do {
                    subject = subjects[getRandomInt(0, subjects.length - 1)];
                } while (usedSubjects.has(subject));
                usedSubjects.add(subject);
                schedule[day].push({
                    subject: subject,
                    topic: topics[subject][getRandomInt(0, topics[subject].length - 1)]
                });
            }
        }
        renderSchedule();
    }

    function renderSchedule() {
        for (let day in schedule) {
            const dayContainer = document.getElementById(day);
            dayContainer.innerHTML = "";
            schedule[day].forEach((lesson, index) => {
                const lessonDiv = document.createElement("div");
                lessonDiv.className = "lesson";
                lessonDiv.textContent = `${index + 1} урок: ${lesson.subject}`;
                lessonDiv.addEventListener("click", () => openPopup(lesson.topic));
                dayContainer.appendChild(lessonDiv);
            });
        }
    }

    function openPopup(topic) {
        document.getElementById("topic-details").textContent = topic;
        document.getElementById("topic-popup").style.display = "block";
    }

    function closePopup() {
        document.getElementById("topic-popup").style.display = "none";
    }

    function generateGrades() {
        const gradesBody = document.getElementById("grades-body");
        gradesBody.innerHTML = "";
        subjects.forEach(subject => {
            const row = document.createElement("tr");
            const subjectCell = document.createElement("td");
            subjectCell.textContent = subject;
            row.appendChild(subjectCell);

            let total = 0;
            for (let i = 0; i < 3; i++) {
                const grade = getRandomInt(2, 5);
                total += grade;
                const gradeCell = document.createElement("td");
                gradeCell.textContent = grade;
                row.appendChild(gradeCell);
            }

            const average = (total / 3).toFixed(2);
            const averageCell = document.createElement("td");
            averageCell.textContent = average;
            row.appendChild(averageCell);

            gradesBody.appendChild(row);
        });
    }


    function updateMonth(weekNumber) {
        const monthDisplay = document.getElementById("month");
        const monthIndex = Math.floor((weekNumber - 1) / 4);
        monthDisplay.textContent = months[monthIndex];
    }

        
    async function sendAiMessage(message) {
        if (message) {
            try {
                const response = await fetch('http://188.92.199.214:7555/api/v1/chat/'/*'https://zwloader.ru/api/v1/chat/'*/, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message }),
                });
                const data = await response.json();
                return data.message;
            } catch (error) {
                console.error('Error:', error);
                return undefined;
            }
        }
    }
    
    function chatWithAi(message) {
        const chatMessages = document.getElementById("chat-messages");

        const userMessageElem = document.createElement("p");
        const aiMessageElem = document.createElement("p");
        
        const chance = getRandomInt(0, 100)

        if (chance <= 10) {
            alert("Вам повезло!")
            spin()
        }

        userMessageElem.textContent = `Вы: ${message}`;
        chatMessages.appendChild(userMessageElem);

        (async () => {
            const aiMessage = await sendAiMessage(message);

            aiMessageElem.textContent = `ИИ: ${aiMessage}`;
            chatMessages.appendChild(aiMessageElem);
        })();

        chatMessages.scrollTop = chatMessages.scrollHeight;
        closePopup();
    }

    document.getElementById("prev-week").addEventListener("click", () => {
        const weekDisplay = document.getElementById("week");
        let weekNumber = parseInt(weekDisplay.textContent.split(" ")[1]);
        if (weekNumber > 1) {
            weekNumber--;
            weekDisplay.textContent = `Неделя ${weekNumber}`;
            updateMonth(weekNumber);
        }
    });

    document.getElementById("next-week").addEventListener("click", () => {
        const weekDisplay = document.getElementById("week");
        let weekNumber = parseInt(weekDisplay.textContent.split(" ")[1]);
        if (weekNumber < 36) {
            weekNumber++;
            weekDisplay.textContent = `Неделя ${weekNumber}`;
            updateMonth(weekNumber);
        }
    });

    const initialWeekNumber = parseInt(document.getElementById("week").textContent.split(" ")[1]);
    updateMonth(initialWeekNumber);


    document.getElementById("collapse-chat").addEventListener("click", () => {
        document.querySelector(".chat").style.display = "none";
        document.getElementById("expand-chat").style.display = "block";
        document.getElementById("collapse-chat").style.display = "none";
    });

    document.getElementById("expand-chat").addEventListener("click", () => {
        document.querySelector(".chat").style.display = "block";
        document.getElementById("expand-chat").style.display = "none";
        document.getElementById("collapse-chat").style.display = "block";
    });

    document.querySelector(".close").addEventListener("click", closePopup);

    document.getElementById("ai-ask-button").addEventListener("click", () => {
        const topicDetails = document.getElementById("topic-details").textContent;
        const message = `Что такое ${topicDetails}?`

        chatWithAi(message)
    });


    document.getElementById("send-chat").addEventListener("click", () => {
        const chatInput = document.getElementById("chat-input");
        const message = chatInput.value;
        chatInput.value = '';

        chatWithAi(message)
    })

    

    // document.getElementById("registration-form").addEventListener("submit", (e) => {
    //     e.preventDefault();
    //     document.getElementById("registration-page").style.display = "none";
    //     document.getElementById("login-page").style.display = "block";
    // });

    // document.getElementById("login-form").addEventListener("submit", (e) => {
    //     e.preventDefault();
    //     const fullName = document.getElementById("full-name").value;
    //     const className = document.getElementById("class").value;
    //     const section = document.getElementById("section").value;

    //     document.getElementById("user-name").textContent = fullName;
    //     document.getElementById("user-class").textContent = `${className}${section}`;

    //     document.getElementById("login-page").style.display = "none";
    //     document.getElementById("index-page").style.display = "block";
    // });

    document.getElementById("logout").addEventListener("click", () => {
        window.location.href = "http://zwloader.ru/";
    });

    document.getElementById("epilepsy-btn").addEventListener("click", () => {
        spin()
    })

    generateSchedule();
    generateGrades();
});
