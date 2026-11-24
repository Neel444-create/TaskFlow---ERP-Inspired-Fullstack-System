
import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import api from '../services/api'

function Register() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  async function handleRegister(e: React.FormEvent) {
    e.preventDefault()
    setError('')

    try {
      await api.post('/auth/register', {
        name,
        email,
        password,
      })
      navigate('/login')
    } catch {
      setError('Registration failed. Check your details or try another email.')
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form onSubmit={handleRegister} className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md">
        <h1 className="text-3xl font-bold text-center mb-2">Create Account</h1>
        <p className="text-slate-500 text-center mb-6">Join TaskFlow</p>

        <input
          className="w-full border p-3 rounded-lg mb-4"
          placeholder="Full name"
          value={name}
          onChange={e => setName(e.target.value)}
          required
        />

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
          minLength={8}
        />

        {error && <p className="text-red-500 mb-3">{error}</p>}

        <button className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700">
          Register
        </button>

        <p className="text-center mt-5">
          Already registered? <Link className="text-blue-600" to="/login">Login</Link>
        </p>
      </form>
    </div>
  )
}

export default Register
