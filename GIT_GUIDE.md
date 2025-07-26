# Git Setup Guide for Guild Manager 🗡️

This guide will help you set up Git for your Fantasy Guild Manager project and deploy it to GitHub Pages for easy hosting!

## What is Git?
Git is a version control system that:
- Tracks changes to your files over time
- Lets you backup your project online
- Makes it easy to deploy websites to GitHub Pages
- Allows collaboration if you want others to help

## Step 1: Install Git

### Windows:
1. Download Git from: https://git-scm.com/download/win
2. Run the installer with default settings
3. Open Command Prompt or PowerShell to test: `git --version`

### Already have Git?
Check if it's installed: `git --version`

## Step 2: Configure Git (First Time Only)

Open Command Prompt/PowerShell and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

## Step 3: Initialize Your Guild Manager Repository

Navigate to your project folder and set up Git:

```bash
cd "c:\Users\tech\Documents\Guild manager"
git init
```

## Step 4: Create a .gitignore File

Some files shouldn't be tracked by Git. Let's create a `.gitignore` file:

```bash
# Create .gitignore file
echo __pycache__/ > .gitignore
echo *.pyc >> .gitignore
echo .DS_Store >> .gitignore
echo guild_data.json >> .gitignore
```

**Note:** We're ignoring `guild_data.json` because it contains your actual guild data. You probably don't want to share your private guild info publicly!

## Step 5: Add and Commit Your Files

```bash
# Add all files to Git
git add .

# Create your first commit
git commit -m "Initial commit: Fantasy Guild Manager CLI"
```

## Step 6: Create a GitHub Repository

1. Go to https://github.com and sign up/login
2. Click the "+" button → "New repository"
3. Name it something like `fantasy-guild-manager`
4. Make it **Public** (required for free GitHub Pages)
5. Don't initialize with README (we already have files)
6. Click "Create repository"

## Step 7: Connect Local Repository to GitHub

GitHub will show you commands like this (replace with your actual username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/fantasy-guild-manager.git
git branch -M main
git push -u origin main
```

## Step 8: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Choose "main" branch and "/ (root)" folder
6. Click "Save"

Your website will be available at:
`https://YOUR_USERNAME.github.io/fantasy-guild-manager/guild_page.html`

## Daily Workflow

### When you update your guild:

1. **Update guild data** using the menu CLI:
   ```bash
   python guild_menu.py
   ```

2. **Generate new webpage** (option 6 in menu)

3. **Commit and push changes**:
   ```bash
   git add guild_page.html
   git commit -m "Update guild page - [describe what changed]"
   git push
   ```

4. **Your website updates automatically!** (takes 1-2 minutes)

## Useful Git Commands

### Check status:
```bash
git status
```

### See what changed:
```bash
git diff
```

### View commit history:
```bash
git log --oneline
```

### Undo changes to a file:
```bash
git checkout -- filename.py
```

### Create a backup branch:
```bash
git branch backup-branch-name
```

## Advanced: Automatic Updates

Create a batch file called `update-and-deploy.bat`:

```batch
@echo off
echo Updating guild webpage...
python guild_menu.py

echo.
echo Deploying to GitHub...
git add guild_page.html
git commit -m "Auto-update guild page - %date% %time%"
git push

echo.
echo Done! Your website will update in 1-2 minutes.
echo Visit: https://YOUR_USERNAME.github.io/fantasy-guild-manager/guild_page.html
pause
```

## Troubleshooting

### "Permission denied" error:
You might need to set up SSH keys or use a personal access token. GitHub has guides for this.

### Website not updating:
- Check the "Actions" tab in your GitHub repository
- Make sure the file is named exactly `guild_page.html`
- GitHub Pages can take 1-2 minutes to update

### Merge conflicts:
If you edit files on GitHub and locally:
```bash
git pull
# Resolve any conflicts
git add .
git commit -m "Resolve conflicts"
git push
```

## Benefits of Using Git

✅ **Automatic backups** - Your code is safe on GitHub
✅ **Easy website hosting** - GitHub Pages is free and automatic
✅ **Version history** - See what changed and when
✅ **Collaboration** - Others can contribute to your guild manager
✅ **Professional workflow** - Learn industry-standard tools

## Quick Reference

```bash
# Daily workflow
git add .
git commit -m "Description of changes"
git push

# Check what's happening
git status
git log --oneline

# Get latest changes
git pull
```

## Your Guild Website URL

Once set up, your guild website will be:
`https://YOUR_USERNAME.github.io/fantasy-guild-manager/guild_page.html`

Share this URL with your party members - it updates automatically whenever you push changes!

---

**Pro Tip:** Bookmark your guild website URL and share it with your party. Every time you update your guild data and push to GitHub, the website updates automatically! 🚀
