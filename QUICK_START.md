# 🚀 Quick Start — 3 Steps to Deploy

## Step 1️⃣ Deploy Backend (Choose One)

### **Render** (Simplest)
1. Go to [render.com](https://render.com/) → Sign up
2. New "Web Service" → Connect your GitHub repo
3. Set **Root Directory**: `backend/`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `python -m uvicorn app:app --port $PORT --host 0.0.0.0`
6. Add **Environment Variable**:
   - Name: `GEMINI_API_KEY`
   - Value: (copy from `config/api_keys.json`)
7. Deploy
8. **Copy your Render URL** (e.g., `https://jarvis-backend.onrender.com`)

### **Railway** (Fast Alternative)
1. Sign up: [railway.app](https://railway.app)
2. New Project → Select GitHub repo
3. Select `backend/` folder
4. Add env var: `GEMINI_API_KEY`
5. Deploy → Note the URL

### **Fly.io** (Advanced)
1. Install [flyctl](https://fly.io/docs/getting-started/installing-flyctl/)
2. From backend folder: `fly launch`
3. `fly secrets set GEMINI_API_KEY=xxx`
4. `fly deploy`

---

## Step 2️⃣ Update Frontend URL

Edit `frontend/.env.production`:
```env
VITE_API_BASE_URL=https://jarvis-backend.onrender.com
```
(Replace with your actual Render/Railway/Fly.io URL)

---

## Step 3️⃣ Deploy Frontend to Vercel

### **Via GitHub (Recommended)**
1. Push code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Jarvis web app"
   git remote add origin https://github.com/YOUR_USERNAME/jarvis-web.git
   git branch -M main
   git push -u origin main
   ```

2. Go to [vercel.com](https://vercel.com/) → New Project
3. Select your repo
4. Set **Root Directory**: `frontend/`
5. Vercel auto-detects Vite ✓
6. Add **Environment Variable**:
   - Name: `VITE_API_BASE_URL`
   - Value: `https://your-backend-url.onrender.com`
7. Click **Deploy**

### **Via Vercel CLI**
```bash
npm install -g vercel
cd frontend
vercel --prod
```

---

## ✅ Done!

Your Vercel URL is live! (e.g., `https://jarvis-web.vercel.app`)

### Test It:
1. Open your Vercel URL
2. Pick a tool from the dropdown
3. Type a query
4. Hit Send
5. Get results from the backend! 🎉

---

## 🐛 Quick Fixes

**Railway build failed in all regions?**
- ✅ I've updated `app.py` to handle missing imports gracefully
- ✅ Updated `requirements.txt` with only cross-platform dependencies
- **Push your changes**: 
  ```bash
  git add backend/app.py backend/requirements.txt
  git commit -m "Fix Railway build - cross-platform imports"
  git push
  ```
- Railway will auto-redeploy → should work now!
- If still fails, check Railway logs for the actual error

**Railway: "User does not have access to region asia-southeast1"?**
- Railway's free tier has limited region access
- **Fix**: In Railway dashboard → Project Settings → Region → change to `us-west` or `us-east`
- **Easier**: Use **Render** instead (no region restrictions on free tier)

**"Failed to reach backend" error?**
- Check backend is running: Visit your Render/Railway URL in browser
- Verify `VITE_API_BASE_URL` in Vercel Settings → Environment Variables
- Check browser console (F12) for actual error

**CORS errors?**
- Already configured in the backend ✓
- If issues, verify `CORSMiddleware` in `backend/app.py`

**Slow responses on first call?**
- Free tier = cold start (30-60s first time)
- Subsequent calls are fast

---

## 📚 Full Docs

See [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md) for complete details.

---

**That's it! You now have a production-ready web AI assistant deployed to Vercel. 🚀**
