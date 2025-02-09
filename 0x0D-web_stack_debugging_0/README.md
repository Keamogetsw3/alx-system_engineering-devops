# 0x0D. Web Stack Debugging #0

## DevOps | SysAdmin | Scripting | Debugging

### In a Nutshell
The Webstack debugging series trains you in the art of debugging. Software and systems rarely work perfectly, and debugging is a crucial skill for Full-Stack Software Engineers. 

In this project, broken web stacks will be provided, and the goal is to debug them and create a Bash script that, when executed, brings the system to a working state.

### Example Debugging Scenario
A simple example of debugging involves ensuring that:
- A copy of the \`/etc/passwd\` file exists in \`/tmp\`
- A file named \`/tmp/isworking\` contains the string \`OK\`

#### Steps to Fix:
\`\`\`bash
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
\`\`\`

### Installing Docker
For this project, a container will be provided. If you want to install Docker for local testing, you can install it on:
- Mac OS
- Windows
- Ubuntu 14.04 (deprecated, with necessary adjustments)
- Ubuntu 16.04

### Resources
Use \`man\` or \`help\` for:
- \`curl\`

### Requirements
- Allowed editors: \`vi\`, \`vim\`, \`emacs\`
- Scripts must run on Ubuntu 14.04 LTS
- All files must end with a new line
- A \`README.md\` file is mandatory at the root of the project
- All Bash script files must be executable
- Bash scripts must pass \`Shellcheck\` without errors
- Scripts must run without errors
- The first line of all Bash scripts should be:
  \`\`\`bash
  #!/usr/bin/env bash
  \`\`\`
- The second line should be a comment explaining the script's purpose