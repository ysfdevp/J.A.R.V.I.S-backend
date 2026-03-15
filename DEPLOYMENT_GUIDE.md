# 🚀 Jarvis Web — Complete Deployment Guide for Vercel

## Overview
Your **Jarvis** system is now split into:
- **Frontend**: React + Vite + Glassmorphism UI (deploys to **Vercel**)
- **Backend**: Python FastAPI (deploys to **Render**, **Railway**, or **Fly.io**)

---

## 🎯 Step 1: Deploy Backend (Python API)

### Option A: Deploy to **Render** (Recommended)
1. **Sign up** at [render.com](https://render.com)
2. **Create a new Web Service** → Connect your GitHub repo
3. **Build Command**: `pip install -r backend/requirements.txt`
4. **Start Command**: `python -m uvicorn app:app --port $PORT --host 0.0.0.0` 
   - (Or use the backend folder with `--app-dir backend`)
5. **Environment Variables**: Add your `GEMINI_API_KEY` from `config/api_keys.json`
6. **Deploy** → You'll get a URL like `https://jarvis-backend.onrender.com`

### Option B: Deploy to **Railway** (Fast)
1. Sign up at [railway.app](https://railway.app)
2. Create new project → Select from your GitHub repo
3. Set root to `backend/`
4. Add environment variable: `GEMINI_API_KEY`
5. Railway auto-detects Python and deploys
6. Note your generated URL (e.g., `https://jarvis-backend-production.up.railway.app`)

### Option C: Deploy to **Fly.io**
1. Install [flyctl](https://fly.io/docs/getting-started/installing-flyctl/)
2. From backend folder: `fly launch`
3. Choose Python runtime
4. Set `GEMINI_API_KEY` secret via `fly secrets set GEMINI_API_KEY=xxx`
5. Deploy: `fly deploy`

**After deployment**, copy your backend URL (e.g., `https://jarvis-backend.onrender.com`) for the next step.

---

## 🎯 Step 2: Update Frontend URL

Edit [frontend/.env.production](frontend/.env.production):
```env
VITE_API_BASE_URL=https://your-backend-url-here.onrender.com
```

Or leave it as-is if you already deployed to Render with the name `jarvis-backend`.

---

## 🎯 Step 3: Deploy Frontend to Vercel

### Option 1: Deploy via GitHub (Recommended)
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Add Jarvis web app"
   git remote add origin https://github.com/YOUR_USERNAME/jarvis-web.git
   git branch -M main
   git push -u origin main
   ```

2. **Link to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Select your repo
   - Set **Root Directory** to `frontend/`
   - Vercel auto-detects Vite
   - Add env variable: `VITE_API_BASE_URL=https://your-backend-url.onrender.com`
   - **Deploy**

### Option 2: Deploy via Vercel CLI
```bash
npm install -g vercel
cd frontend
vercel --prod
```

---

## ✅ Verify Deployment

After both deployments complete:

1. **Open your Vercel frontend URL** (e.g., `https://jarvis-web.vercel.app`)
2. **Select a tool** (Web Search, Weather, etc.)
3. **Type a query** and click Send
4. **Check browser console** (F12 → Console) for any errors
5. **Backend should respond** with results

---

## 🔧 Troubleshooting

### **Frontend shows "Failed to reach backend"**
- ✅ Verify backend is running: Visit `https://your-backend-url.onrender.com/` in browser
- ✅ Check Vercel env variable: Settings → Environment Variables → `VITE_API_BASE_URL`
- ✅ Check browser console for exact error

### **CORS errors in browser console**
- The backend already has `CORSMiddleware` enabled
- If still issues, add this to `backend/app.py`:
  ```python
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # Allow all origins (for dev); restrict in production
      allow_methods=["*"],
      allow_headers=["*"],
  )
  ```

### **Backend timeouts or slow responses**
- Some tools like `desktop_control`, `computer_control`, `code_helper` are **Windows-only**
  - They won't work when backend runs on Linux/cloud
  - Best for running locally
- Test with simple tools: `web_search`, `weather_report`, `open_app` (if backend is local)

---

## 📦 Local Development

### Run locally before deploying:

**Terminal 1 — Backend**:
```bash
cd backend
python -m uvicorn app:app --reload --port 8000
```

**Terminal 2 — Frontend**:
```bash
cd frontend
npm run dev
```

Open `http://localhost:5173` in your browser.

---

## 🎨 Next Steps: Enhance Your UI

The frontend already has **glassmorphism** and **Framer Motion animations**. You can:

1. **Add more tools** to the dropdown in `frontend/src/App.jsx`:
   ```javascript
   const TOOLS = [
     { id: "web_search", label: "Web Search" },
     { id: "weather_report", label: "Weather" },
     { id: "flight_finder", label: "Flight Finder" },
     // Add more here...
   ];
   ```

2. **Customize colors** in `frontend/src/App.css`:
   - `:root` CSS variables (`--accent`, `--bg`, `--card`, etc.)

3. **Add more UI components** in `frontend/src/` (e.g., sidebar, voice input, history)

---

## 📝 File Structure After Setup

```
JUST A RATHER VERY INTELLIGENT SYSTEM/
├── backend/                      (Python FastAPI)
│   ├── app.py
│   ├── requirements.txt
│   └── vercel.json (optional)
├── frontend/                     (React + Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── .env                      (local: http://localhost:8000)
│   ├── .env.production           (Vercel: https://backend-url)
│   ├── vercel.json
│   └── package.json
├── actions/                      (Existing actions)
├── agent/
├── config/
├── core/
├── memory/
├── main.py
└── README.md
```

---

## 🚀 Final Checklist Before Sharing

- [ ] Backend deployed to Render/Railway/Fly.io → note the URL
- [ ] Frontend `.env.production` updated with backend URL
- [ ] Frontend deployed to Vercel
- [ ] Test frontend at Vercel URL → can send messages and get responses
- [ ] Browser console shows no errors
- [ ] Share your Vercel frontend URL with others!

---

## 💡 Pro Tips

1. **Use env vars**: Never hardcode API keys. Use Vercel/Render environment variables.
2. **Monitor logs**: Check Render/Railway/Vercel dashboards for real-time logs.
3. **Serverless runtime**: On free tiers, cold starts may cause 30-60s delays on first call.
4. **Add more tools**: Each tool in your `actions/` folder can be exposed via the `/api/tool` endpoint.
5. **User feedback**: Show loading states while waiting for responses (already implemented via `loading` state in React).

---

**Happy deploying! 🎉**
