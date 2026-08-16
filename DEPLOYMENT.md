# 🚀 Streamlit Cloud Deployment Checklist

## Pre-Deployment Verification
- [x] GitHub repository created and accessible
- [x] All changes pushed to `main` branch
- [x] requirements.txt contains all dependencies
- [x] .streamlit/config.toml configured
- [x] .env file in .gitignore (NOT committed)
- [x] .env.example provided for reference
- [x] API keys NOT hardcoded in source files
- [x] App runs locally without errors

## Deployment Steps

### Step 1: Streamlit Cloud Setup
1. Go to https://share.streamlit.io
2. Sign in with GitHub (or create account)
3. Click "New app"

### Step 2: Configure Deployment
- **Repository**: udayrastogi0531/Multi-Agent-Research-System
- **Branch**: main
- **Main file path**: app.py

### Step 3: Set Secrets
After deployment starts:
1. Click Settings (⚙️) → "Secrets"
2. Add secrets in this format:
   ```
   GROQ_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   ```
3. Save (auto-redeploy will trigger)

### Step 4: Monitor Deployment
- Check "Logs" tab for any errors
- Wait for "App is running" message
- Test the deployed URL

## Deployment URL
```
https://share.streamlit.io/udayrastogi0531/Multi-Agent-Research-System/main/app.py
```

## After Deployment

### Automatic Updates
- Push changes to `main` branch on GitHub
- Streamlit Cloud automatically detects and redeploys
- No manual action needed!

### Manual Redeploy (if needed)
1. Go to your app settings
2. Click "Reboot app" button

## Troubleshooting

| Issue | Solution |
|-------|----------|
| App won't start | Check Logs tab for error messages |
| API keys not found | Verify in Settings → Secrets (not in .env) |
| Import errors | Run locally first: `streamlit run app.py` |
| App sleeps after inactivity | Free tier limitation - just refresh page |
| Timeout errors | May need to optimize data fetching |

## Performance Tips

- Keep API calls minimal during UI rendering
- Cache results when possible
- Use `st.spinner()` for long operations
- Monitor API rate limits

## Support

- Streamlit Docs: https://docs.streamlit.io
- Deploy Docs: https://docs.streamlit.io/streamlit-cloud/deploy-your-app
- GitHub Issues: Report bugs at your repo
