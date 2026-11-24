
// import { useState } from 'react'
import { useState, type FormEvent } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import api from '../services/api'
import axios from 'axios'

<h1 className="text-3xl font-bold text-slate-900 text-center mb-2">
  TaskFlow
</h1>

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  
async function handleLogin(e: React.FormEvent<HTMLFormElement>) {
  e.preventDefault()
  setError('')

  const formData = new URLSearchParams()
  formData.append('username', email.trim())
  formData.append('password', password)

  try {
    const response = await api.post('/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    localStorage.setItem('access_token', response.data.access_token)

    navigate('/dashboard')
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Login error:', error.response?.data)
      setError(
        error.response?.data?.detail || 'Login failed. Please check your credentials.'
      )
    } else {
      console.error(error)
      setError('An unexpected error occurred.')
    }
  }
}


  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form onSubmit={handleLogin} className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md">
        <h1 className="text-3xl font-bold text-center mb-2">TaskFlow</h1>
        <p className="text-slate-500 text-center mb-6">Sign in to your account</p>

        <input
          className="w-full border p-3 rounded-lg mb-4"
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />

        <input
          className="w-full border p-3 rounded-lg mb-4"
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />

        {error && <p className="text-red-500 mb-3">{error}</p>}

        <button className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700">
          Login
        </button>

        <p className="text-center mt-5">
          Don't have an account? <Link className="text-blue-600" to="/register">Register</Link>
        </p>
      </form>
    </div>
  )
}

export default Login
