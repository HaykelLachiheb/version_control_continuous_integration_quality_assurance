# Reflection Report

## Student Name: Haykel Lachiheb

## Course: Introduction to Software Development Practices

---

### Challenges Faced

The biggest challenge I faced while learning Git was understanding merge conflicts. When two people modify the same file on different branches, resolving the conflicting sections felt intimidating at first. I learned to look for the `<<<<<<<`, `=======`, and `>>>>>>>` markers and carefully decide which changes to keep. Another difficulty was setting up the GitHub Actions CI pipeline — I initially forgot to specify the correct Python version and the build failed because `pip` wasn't upgraded. Debugging the YAML syntax was also tricky at first. For the QA part, writing comprehensive unit tests was harder than expected. I had to think about edge cases like dividing by zero, negative inputs for square root, and empty lists for the average function. The linter flagged several style issues like trailing whitespace and missing blank lines, which taught me to pay attention to code formatting. Overall, these challenges were valuable learning experiences that made me more careful and deliberate when writing code.

### How the CI Pipeline Streamlined Development

The CI pipeline was a game-changer. Every time I pushed code, GitHub Actions automatically ran all 18 tests and the flake8 linter. This gave me immediate feedback — I didn't have to manually run tests on my machine every time. When I forgot to export `average` in `__init__.py`, the CI caught the import error instantly. This automated safety net caught bugs early, saved time, and gave me confidence that my changes didn't break existing functionality. It also ensured consistency: every team member's code goes through the same checks before merging.

### How Version Control and QA Improved Collaboration and Code Quality

Git branches allowed me to develop the `average()` feature in isolation on `feature/average-function` without touching the stable `main` branch. After merging, the Git history clearly shows the feature's entire lifecycle. The pull request process encouraged knowledge sharing — my peer reviewer spotted that I should handle empty lists, which I then added. Automated testing and linting enforced quality standards objectively: no one could merge code that broke tests or violated style rules. This workflow made collaboration smoother, reduced integration headaches, and produced a more reliable codebase overall.

---

*(Word count: ~280)*
