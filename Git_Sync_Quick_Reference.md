# Git Branch Sync — Quick Reference

A short guide to sync a local branch with a remote `main` when histories diverge (e.g., local project vs. empty/initial remote repo).

---

## Goal
Keep your local files, sync them to GitHub `main`, and stop using the old local `master` branch.

---

## Commands — Step by step

1. **Confirm where you are**
```bash
cd ~/Blowing_Smoke
git status
git branch
git remote -v
```

2. **(Optional) Rename local `master` → `main`**
```bash
git branch -m master main
```

3. **Stage & commit your local files**
```bash
git add .
git commit -m "Initial commit — local project files"
```

4. **Set merge (not rebase) behavior for pulls**
```bash
git config pull.rebase false
# or for all repos:
# git config --global pull.rebase false
```

5. **Pull & merge remote `main` (allow unrelated histories)**
```bash
git pull origin main --allow-unrelated-histories
```
- If an editor opens for a merge message, save & close to complete the merge commit.
- If conflicts occur, Git will show which files need resolution.

6. **Resolve conflicts (if any)**
```bash
git status
# edit conflicted files, then:
git add <file(s)>
git commit      # completes the merge commit
# if you want to abort the merge:
# git merge --abort
```

7. **Push the unified branch to GitHub**
```bash
git push -u origin main
```
- `-u` sets the upstream so future `git push` / `git pull` work from `main`.

---

## Quick checks & useful commands
- See what changed / staged:
```bash
git status
```
- View recent commits:
```bash
git log --oneline --graph --decorate -n 20
```
- Show remote branches & details:
```bash
git remote show origin
```
- If something goes wrong during merge:
```bash
git merge --abort
```

---

## Short explanations / tips
- `--allow-unrelated-histories` is needed when both repos have separate root commits (common when a GitHub repo has an initial README or license).
- Setting `pull.rebase false` keeps the default pull behavior as a **merge**. If you prefer a linear history, use rebase (`pull.rebase true`) — but merge is simplest for resolving divergent histories safely.
- Avoid `--force` pushes unless you intentionally want to overwrite remote history. If you must overwrite (rare), use `git push --force` with caution.
- Use `git status` frequently — it tells you exactly what Git expects next.
- If you want a global preference for merging not rebasing:
```bash
git config --global pull.rebase false
```

---

## Common scenario (compact)
```bash
cd ~/Blowing_Smoke
git branch -m master main
git add .
git commit -m "Initial commit"
git config pull.rebase false
git pull origin main --allow-unrelated-histories
# resolve conflicts if prompted
git push -u origin main
```

---

## When to ask for help
If `git pull` reports many conflicts or you see unexpected commits, copy and paste the output of:
```bash
git status
git branch -vv
git log --oneline --decorate -n 10
```
and someone can guide you through the exact conflict resolution.
