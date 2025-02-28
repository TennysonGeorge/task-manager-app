document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const taskForm = document.getElementById('task-form');
    const tasksContainer = document.getElementById('tasks-container');
    const taskTemplate = document.getElementById('task-template');
    
    // Load tasks when page loads
    loadTasks();
    
    // Add event listener for form submission
    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        
        addTask(title, description);
    });
    
    // Function to load all tasks
    function loadTasks() {
        fetch('/tasks')
            .then(response => response.json())
            .then(tasks => {
                tasksContainer.innerHTML = '';
                tasks.forEach(task => {
                    renderTask(task);
                });
            })
            .catch(error => console.error('Error loading tasks:', error));
    }
    
    // Function to add a new task
    function addTask(title, description) {
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                description: description
            })
        })
        .then(response => response.json())
        .then(task => {
            renderTask(task);
            taskForm.reset();
        })
        .catch(error => console.error('Error adding task:', error));
    }
    
    // Function to update a task
    function updateTask(id, data) {
        fetch(`/tasks/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .catch(error => console.error('Error updating task:', error));
    }
    
    // Function to delete a task
    function deleteTask(id) {
        fetch(`/tasks/${id}`, {
            method: 'DELETE'
        })
        .then(() => {
            const taskElement = document.querySelector(`.task-item[data-id="${id}"]`);
            if (taskElement) {
                taskElement.remove();
            }
        })
        .catch(error => console.error('Error deleting task:', error));
    }
    
    // Function to render a task
    function renderTask(task) {
        const taskElement = document.importNode(taskTemplate.content, true).querySelector('.task-item');
        
        taskElement.dataset.id = task.id;
        taskElement.querySelector('.task-title').textContent = task.title;
        taskElement.querySelector('.task-description').textContent = task.description || 'No description';
        
        if (task.created_at) {
            const date = new Date(task.created_at);
            taskElement.querySelector('.task-date').textContent = `Created: ${date.toLocaleString()}`;
        }
        
        const statusElement = taskElement.querySelector('.task-status');
        if (task.completed) {
            taskElement.classList.add('completed');
            statusElement.textContent = 'Completed';
        } else {
            statusElement.textContent = 'Pending';
        }
        
        // Add event listeners for buttons
        const completeBtn = taskElement.querySelector('.complete-btn');
        completeBtn.addEventListener('click', function() {
            const completed = !task.completed;
            updateTask(task.id, { completed: completed });
            
            if (completed) {
                taskElement.classList.add('completed');
                statusElement.textContent = 'Completed';
            } else {
                taskElement.classList.remove('completed');
                statusElement.textContent = 'Pending';
            }
            
            task.completed = completed;
        });
        
        const deleteBtn = taskElement.querySelector('.delete-btn');
        deleteBtn.addEventListener('click', function() {
            if (confirm('Are you sure you want to delete this task?')) {
                deleteTask(task.id);
            }
        });
        
        tasksContainer.appendChild(taskElement);
    }
}); 