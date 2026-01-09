# Git Notes - Quick Reference for Python Mastery 2026

This file is a comprehensive cheat sheet for Git, tailored for our project. Use it for quick lookups. Sections include common commands, concepts like pull requests and branching, troubleshooting, and best practices. Pro Tip: Practice these in a test repo to build muscle memory (active learning via repetition).

## What is Git?
Git is a distributed version control system created by Linus Torvalds in 2005 for Linux development. It tracks changes in code, enables collaboration, and allows branching for safe experimentation. Who uses it? Virtually all tech companies (Google, Microsoft, Amazon) and open-source projects (e.g., Python itself on GitHub). Career note: Git proficiency is essential for devs – entry-level roles expect it, seniors use advanced features like rebasing. Wages boost with GitHub portfolio (beginner +10-20k, senior managers oversee Git workflows for teams).

## Common Git Commands

# See what Git thinks is tracked on your local main branch
git ls-tree -r main --name-only

# Initialize a new repo (do this once per project)
git init

# Clone a remote repo to local
git clone https://github.com/username/repo.git

# Check status (uncommitted changes, branch)
git status

# Add files to staging
git add .  # All files
git add file.py  # Specific file

# Commit staged changes with message
git commit -m "Descriptive message like 'Add Lesson 1 code'"

# Push commits to remote branch
git push origin main  # Or your branch name

# Pull updates from remote
git pull origin main  # Merges remote changes into local

# Switch branches
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch

# List branches
git branch

# Merge branch into current (e.g., from main)
git merge branch-name

# View commit history
git log --oneline  # Short format

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git restore file.py

Pro Tip: Always commit often with meaningful messages – helps in debugging and collaboration. For learning, use `git log` to review history and see how changes build.

## What is a Pull Request (PR)?
A pull request is a GitHub feature (not native Git) to propose changes from one branch/repo to another. It allows review, discussion, and approval before merging.

- **Why use it?** Promotes code review (catch bugs early), collaboration (team feedback), and history (tracks why changes were made). In professional teams, PRs are mandatory for quality control. For our project, use PRs for major lessons to simulate real-world workflow – e.g., develop on "lesson-2" branch, PR to main.

- **How to use it?**
    1. Commit and push to a branch: git push origin lesson-2
    2. On GitHub, go to repo → Pull requests → New pull request.
    3. Select base: main, compare: lesson-2.
    4. Add title/description, create PR.
    5. Review/comment, then merge.

Pro Tip: Use PR templates (add .github/PULL_REQUEST_TEMPLATE.md in repo) for structure. In AI projects, PRs are used to review model code before deployment.

## Branching and Merging (Git Flow)
Branching allows working on features without affecting main code – key for professional development.

- **Why branch?** Isolates changes (e.g., "lesson-3-dictionaries"), avoids breaking main, enables parallel work.

- **Common Flow**:
    - Main: Stable code.
    - Feature branch: git checkout -b feature-name
    - Work, commit, push.
    - Merge back: git checkout main, git merge feature-name
    - Delete branch: git branch -d feature-name

- **Conflicts**: If merge has conflicts, Git marks files – edit, add, commit.

Pro Tip: Use `git rebase` for cleaner history (advanced – ask for details later). In LLM projects, branch for "model-training" to test without risking production code.

## Troubleshooting Common Errors
- "Fatal: not a git repository": Run `git init` or clone again.
- "No such remote 'origin'": Add remote with `git remote add origin url`.
- "Rejected (non-fast-forward)": Pull first with `git pull` to sync.
- "Permission denied (403)": Check PAT scopes (repo), regenerate if expired.
- "Branch 'main' set up to track": Normal – means tracking remote.

Pro Tip: Use `git help command` for docs. For learning, intentionally cause errors in a test repo to practice fixing (experiential learning).

## Best Practices and Other Useful Info
- **Commit Often**: Small, atomic commits – easier to rollback.
- **Meaningful Messages**: "Fix bug in Lesson 2 test" > "Update".
- **.gitignore**: Ignore .venv, .idea, __pycache__ (we have it).
- **GitHub Features**: Issues for bugs/tasks, Projects for kanban, Actions for CI/CD (auto-tests on push).
- **Security**: Never commit secrets (use .env files, ignore them).
- **Collaboration**: Fork repos for contributions, use PRs for open-source.
- **Tools**: GitHub Desktop for GUI, VS Code Git integration for ease.
- **Learning Resources**: "Pro Git" book (free online), GitHub Docs, Codecademy Git course.

- **Career Tip**: GitHub profile is your resume – star repos, contribute to open-source for visibility. Managers value Git flow knowledge for team coordination.

# Reminder: Push After Changes
git add .
git commit -m "Add git_notes.md"
git push origin main

End of Git Notes – refer back as needed. Update this file as we learn more!