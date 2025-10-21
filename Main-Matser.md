Git Branch Sync & Merge Quick Reference
This guide helps you sync your local Git branch with a remote GitHub repository when you have
divergent branches (e.g., local files vs. empty or changed GitHub repo).
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 1nn Rename Your
Local Branch If your local branch is "master" and remote is "main": git branch -m master main
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 2nn Check Remote
Make sure your local repo points to the correct GitHub remote: git remote -v
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 3nn Add and Commit
Local Files git add . git commit -m "Initial commit or update"
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 4nn Allow Merge of
Unrelated Histories If GitHub has an initial commit (like a README), merge safely: git config
pull.rebase false git pull origin main --allow-unrelated-histories
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 5nn Resolve Merge
Prompt If a text editor opens, save and close the default merge message.
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 6nn Push Your Local
Files to GitHub git push -u origin main
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 7nn Set Global
Default Merge Behavior Avoid future prompts about rebase vs merge: git config --global pull.rebase
false nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 8nn Verify
Check your repo online — your local files should appear under the "main" branch.
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn Quick Summary |
Step | Action | Command | |------|---------|----------| | Rename | Local master → main | git branch -m
master main | | Add files | Stage & commit | git add . && git commit -m "msg" | | Merge | Combine
remote + local | git pull origin main --allow-unrelated-histories | | Push | Upload local → GitHub | git
push -u origin main | | Verify | Check remote | git status / GitHub site |
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn Tips - Use `git status`
often to understand what’s staged, modified, or untracked. - `git log --oneline` shows your commit
history. - If a merge goes wrong, use `git merge --abort` to undo it.
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn End of Guide — ©
2025 Git Study Reference
