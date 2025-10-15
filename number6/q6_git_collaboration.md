## 🤝 SECTION 4 — Version Control & Collaboration (5 marks)

### ✅ Question 6
> Explain how you would use Git to collaborate on a team project.

#### 🗂 File name:
`q6_git_collaboration.md`

#### 📄 Content:
# Git Collaboration

### Common Git command I use often:
`git pull` — This updates my local code with the latest changes from teammates on the remote repository.

### How I collaborate:
1. Clone the repository using `git clone <repo_url>`.
2. Create a new branch for my work using `git checkout -b feature-name`.
3. Make changes, commit them, and push using `git push origin feature-name`.
4. Open a Pull Request (PR) on GitHub for review before merging to the main branch.

### Problem I faced:
Once, I tried to push but got a "merge conflict" error because my teammate had made changes to the same file.

### How I solved it:
I ran `git pull origin main` to fetch the latest updates, fixed the conflicting lines manually, committed the fix, and pushed again.
