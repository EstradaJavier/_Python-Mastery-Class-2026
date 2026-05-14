# Git Cheatsheet - Javier's Python Mastery Course

Useful Git commands and troubleshooting guide.

## 📍 Basic Commands

| Command | Description |
|---------|-----------|
| `git status` | Show current status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit with message |
| `git push origin main` | Push to GitHub |
| `git pull origin main` | Pull latest changes |

## 🌿 Branching

| Command | Description |
|---------|-----------|
| `git branch` | List local branches |
| `git branch -a` | List all branches (local + remote) |
| `git checkout -b feature/name` | Create and switch to new branch |
| `git checkout main` | Switch to main |
| `git branch -d branch-name` | Delete local branch |

## 🔄 Pull Request Workflow

1. `git checkout -b feature/new-feature`
2. Make changes
3. `git add . && git commit -m "message"`
4. `git push origin feature/new-feature`
5. Go to GitHub → Create Pull Request

## 🧹 Cleanup

| Command | Description |
|---------|-----------|
| `git branch -d branch-name` | Delete local branch |
| `git fetch --prune` | Clean deleted remote branches |
| `git pull origin main` | Update main branch |

## ⚠️ Common Errors & Fixes

| Error | Fix |
|------|-----|
| `remote: Invalid username or token` | Use Personal Access Token instead of password |
| `branch 'name' not found` | Branch was already deleted or wrong name |
| `Your branch is ahead of 'origin/main'` | `git push origin main` |
| `Everything up-to-date` | You're already synced |
| `failed to push some refs` | Do `git pull origin main` first, then push |
| `Permission denied` | Check if you're using the correct token |

## ⚙️ Git Configuration Commands

| Command | Description |
|---------|-----------|
| `git config --global user.name "Your Name"` | Set your name |
| `git config --global user.email "your@email.com"` | Set your email |
| `git config user.email` | Check current email |
| `git config --global credential.helper osxkeychain` | Remember token on Mac |
| `git config --global core.editor "code --wait"` | Set VS Code as default editor |

## 📋 Working with Kanban / Issues

| Action | How to Do It |
|--------|-------------|
| Create Issue | GitHub → Issues → New Issue |
| Link Issue to PR | Put `Closes #12` in PR description |
| Move card on Project Board | Drag & drop on Projects tab |
| Auto-close Issue on Merge | Use keywords: `Closes`, `Fixes`, `Resolves` + issue number |

## 💡 Pro Tips

- Always run `git status` before committing
- Pull from `main` before starting new work
- Use clear branch names (`feature/`, `bugfix/`, `docs/`)
- Write meaningful commit messages
- Keep your `docs/` folder organized

---

### Next Steps for You:

1. Create the `docs/` folder
2. Create `git-cheatsheet.md` inside it with the content above
3. (Optional) Move `emojis.md` into the `docs/` folder too

