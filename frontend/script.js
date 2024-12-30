document.addEventListener('DOMContentLoaded', function () {
    const taskInput = document.getElementById('input-box');
    const addButton = document.getElementById('addButton');
    const taskList = document.getElementById('tasks-List');

    let tasks = [];

    function renderTasks() {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.classList.toggle('checked', task.completed);

            const taskContent = document.createElement('div');
            taskContent.classList.add('task-content');

            const spanText = document.createElement('span');
            spanText.textContent = task.text;
             taskContent.appendChild(spanText);

            li.appendChild(taskContent);


            const editButton = document.createElement('button');
            editButton.textContent = 'Ред.';
            editButton.classList.add('edit-button');
            li.appendChild(editButton);


            const spanDelete = document.createElement('span');
             spanDelete.textContent = '\u00d7';
            li.appendChild(spanDelete);



           if (task.editing) {
                spanText.style.display = 'none';
                 editButton.style.display = 'none';
                const input = document.createElement('input');
                input.type = 'text';
                input.value = task.text;
                taskContent.insertBefore(input, spanText)

                 input.focus();

                   input.addEventListener('blur', () => {
                     tasks[index].editing = false;
                     tasks[index].text = input.value;
                     renderTasks();
                });
                 input.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        tasks[index].editing = false;
                         tasks[index].text = input.value;
                         renderTasks();
                    }
                });

            }

            li.addEventListener('click', (e) => {
                if ((e.target.tagName === 'LI' || e.target.tagName === 'SPAN') && !task.editing) {
                    tasks[index].completed = !tasks[index].completed;
                     renderTasks();
                }
            });

           editButton.addEventListener('click', (e) => {
                 e.stopPropagation();
                 tasks[index].editing = true;
                renderTasks();
           });

            spanDelete.addEventListener('click', (e) => {
                e.stopPropagation();
                tasks.splice(index, 1);
                renderTasks();
            });



            taskList.appendChild(li);

        });
    }

    addButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            tasks.push({ text: taskText, completed: false, editing: false });
            taskInput.value = '';
            renderTasks();
        }
    });

    renderTasks();
});
