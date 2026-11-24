
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../services/api'

interface Task {
  id: string
  title: string
  description?: string
  completed: boolean
}

function Dashboard() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const navigate = useNavigate()

  async function loadTasks() {
    try {
      const response = await api.get('/tasks/')
      setTasks(response.data)
    } catch {
      localStorage.removeItem('access_token')
      navigate('/login')
    }
  }

  async function addTask(e: React.FormEvent) {
    e.preventDefault()

    if (!title.trim()) return

    await api.post('/tasks/', { title, description })
    setTitle('')
    setDescription('')
    loadTasks()
  }

  async function toggleTask(task: Task) {
    await api.patch(`/tasks/${task.id}`, {
      completed: !task.completed,
    })
    loadTasks()
  }

  async function deleteTask(id: string) {
    await api.delete(`/tasks/${id}`)
    loadTasks()
  }

  function logout() {
    localStorage.removeItem('access_token')
    navigate('/login')
  }

  useEffect(() => {
    loadTasks()
  }, [])

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <div className="max-w-3xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">TaskFlow</h1>
          <button onClick={logout} className="bg-red-500 text-white px-4 py-2 rounded-lg">
            Logout
          </button>
        </div>

        <form onSubmit={addTask} className="bg-white p-5 rounded-xl shadow mb-6">
          <input
            className="w-full border p-3 rounded-lg mb-3"
            placeholder="Task title"
            value={title}
            onChange={e => setTitle(e.target.value)}
            required
          />

          <input
            className="w-full border p-3 rounded-lg mb-3"
            placeholder="Description"
            value={description}
            onChange={e => setDescription(e.target.value)}
          />

          <button className="bg-blue-600 text-white px-5 py-2 rounded-lg">
            Add Task
          </button>
        </form>

        <div className="space-y-3">
          {tasks.map(task => (
            <div key={task.id} className="bg-white p-4 rounded-xl shadow flex justify-between items-center">
              <div>
                <h3 className={`font-semibold ${task.completed ? 'line-through text-slate-400' : ''}`}>
                  {task.title}
                </h3>
                <p className="text-slate-500 text-sm">{task.description}</p>
              </div>

              <div className="flex gap-2">
                <button onClick={() => toggleTask(task)} className="bg-green-500 text-white px-3 py-2 rounded-lg">
                  {task.completed ? 'Undo' : 'Complete'}
                </button>
                <button onClick={() => deleteTask(task.id)} className="bg-red-500 text-white px-3 py-2 rounded-lg">
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Dashboard
