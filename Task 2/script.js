const taskForm = document.getElementById('taskForm');
const taskTable = document.getElementById('taskTable').getElementsByTagName('tbody')[0];

// Fetch and display tasks
async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    taskTable.innerHTML = '';
    tasks.forEach(task => {
        const row = taskTable.insertRow();
        row.innerHTML = `
            <td>${task.id}</td>
            <td>${task.title}</td>
            <td>${task.description}</td>
            <td>${task.status}</td>
            <td>
                <button onclick="deleteTask(${task.id})">Delete</button>
            </td>`;
    });
}

// Add task
taskForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description })
    });
    fetchTasks();
});

// Delete task
async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
}

// Initialize
fetchTasks();