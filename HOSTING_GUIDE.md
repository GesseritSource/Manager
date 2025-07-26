# How to Host Your Guild Website 🌐

Your Fantasy Guild Manager generates beautiful HTML pages that your party members can view. Here are several ways to share these pages:

## Option 1: Simple File Sharing (Easiest)
Just share the generated `guild_page.html` file directly with your party members:
- Email the file as an attachment
- Share via Discord, Slack, or other messaging platforms
- Put it in a shared folder (Google Drive, Dropbox, OneDrive)
- Your party members can open it in any web browser

## Option 2: Local Web Server (For Testing)
Run a simple web server on your computer:

```bash
# Navigate to your guild folder
cd "c:\Users\tech\Documents\Guild manager"

# Start a local web server
python -m http.server 8000
```

Then your party can visit: `http://your-ip-address:8000/guild_page.html`

**Note:** This only works while your computer is on and connected to the same network.

## Option 3: Free Web Hosting Services

### GitHub Pages (Free & Easy)
1. Create a GitHub account at https://github.com
2. Create a new repository called `my-guild-page`
3. Upload your `guild_page.html` file
4. Go to Settings → Pages
5. Enable GitHub Pages
6. Your page will be available at: `https://yourusername.github.io/my-guild-page/guild_page.html`

### Netlify (Free & Drag-and-Drop)
1. Go to https://netlify.com
2. Sign up for a free account
3. Drag and drop your `guild_page.html` file onto their deploy area
4. Get an instant URL like: `https://random-name-12345.netlify.app`

### Vercel (Free & Simple)
1. Go to https://vercel.com
2. Sign up for a free account
3. Import your project or drag-and-drop the HTML file
4. Get a URL like: `https://my-guild.vercel.app`

## Option 4: Traditional Web Hosting
If you want a custom domain (like `myawesomeguild.com`):
- Use services like Hostinger, Bluehost, or GoDaddy
- Upload your HTML file via FTP or file manager
- Usually costs $3-10/month

## Auto-Update Workflow

To keep your website updated:

1. **Update your guild data** using the menu CLI
2. **Regenerate the webpage** (option 6 in the menu)
3. **Re-upload** the new HTML file to your hosting service

### Pro Tip: Batch File for Quick Updates
Create a file called `update_website.bat`:

```batch
@echo off
echo Generating new guild webpage...
python guild_menu.py
echo.
echo Don't forget to upload the new guild_page.html to your hosting service!
pause
```

## Security Notes
- The generated HTML contains no sensitive data
- It's completely static (no server-side code)
- Safe to host anywhere
- No login system needed - it's just a display page

## Mobile-Friendly
Your generated webpage automatically works great on:
- Desktop computers
- Tablets  
- Mobile phones
- Any device with a web browser

## Customization
Want to customize the look? Edit the CSS in `web_generator.py` and regenerate!

---

**Quick Start Recommendation:** 
Start with **Option 1** (file sharing) for immediate use, then try **Netlify** (Option 3) for a permanent web address your party can bookmark! 🗡️✨
