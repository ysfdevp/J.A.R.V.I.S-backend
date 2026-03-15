import { useMemo, useState } from "react"
import { AnimatePresence, motion } from "framer-motion"
import axios from "axios"
import "./App.css"

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"

const TOOLS = [
  { id: "web_search", label: "Web Search" },
  { id: "open_app", label: "Open App" },
  { id: "weather_report", label: "Weather" },
  { id: "computer_settings", label: "Computer Control" },
]

function ChatMessage({ message }) {
  const isUser = message.role === "user"
  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -12 }}
      className={`chat-message ${isUser ? "user" : "assistant"}`}
    >
      <div className="avatar" aria-hidden="true">
        {isUser ? "👤" : "🤖"}
      </div>
      <div className="bubble">
        <pre>{message.text}</pre>
      </div>
    </motion.div>
  )
}

function App() {
  const [messages, setMessages] = useState([
    {
      id: "welcome",
      role: "assistant",
      text: "Welcome! Pick a tool, ask something, and watch Jarvis do the work.",
    },
  ])
  const [tool, setTool] = useState("web_search")
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const toolLabel = useMemo(
    () => TOOLS.find((t) => t.id === tool)?.label || tool,
    [tool]
  )

  const addMessage = (msg) => {
    setMessages((prev) => [...prev, { id: crypto.randomUUID(), ...msg }])
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError("")
    const trimmed = input.trim()
    if (!trimmed) return

    addMessage({ role: "user", text: trimmed })
    setInput("")
    setLoading(true)

    try {
      const resp = await axios.post(
        `${API_BASE}/api/tool`,
        {
          name: tool,
          parameters: { query: trimmed },
        },
        { timeout: 60000 }
      )

      addMessage({ role: "assistant", text: resp.data.result })
    } catch (err) {
      console.error(err)
      setError("Failed to reach backend. Ensure the backend is running on port 8000.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="title">
          <h1>Jarvis Web</h1>
          <p className="subtitle">Glassmorphism UI · AI tools · Web search</p>
        </div>
        <div className="selectors">
          <label className="select-label">
            Tool
            <select
              value={tool}
              onChange={(e) => setTool(e.target.value)}
              className="select"
            >
              {TOOLS.map((t) => (
                <option key={t.id} value={t.id}>
                  {t.label}
                </option>
              ))}
            </select>
          </label>
        </div>
      </header>

      <main className="chat">
        <AnimatePresence initial={false}>
          {messages.map((msg) => (
            <ChatMessage key={msg.id} message={msg} />
          ))}
        </AnimatePresence>
      </main>

      <form className="composer" onSubmit={handleSubmit}>
        <input
          className="composer-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={`Ask Jarvis to ${toolLabel.toLowerCase()}...`}
          disabled={loading}
          autoFocus
        />
        <button className="composer-send" type="submit" disabled={loading}>
          {loading ? "Thinking…" : "Send"}
        </button>
      </form>

      {error ? <div className="error">{error}</div> : null}
    </div>
  )
}

export default App
