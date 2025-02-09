# 0x0B. SSH

## DevOps | SSH | Network | SysAdmin | Security  

### Background Context

This project involves setting up and working with SSH (Secure Shell) to connect to remote servers securely using an RSA key pair. Unlike previous levels, authentication will be done using an SSH key instead of a password. An Ubuntu 20.04 LTS server has been assigned for this project.

---

## Resources

### Read or Watch:
- [What is a (physical) server - text](#)
- [What is a (physical) server - video](#)
- [SSH essentials](#)
- [SSH Config File](#)
- [Public Key Authentication for SSH](#)
- [How Secure Shell Works](#)
- [SSH Crash Course](#)

### Reference:
- [Understanding the SSH Encryption and Connection Process](#)
- [Secure Shell Wiki](#)
- [IETF RFC 4251 (Description of the SSH Protocol)](#)
- [Internet Engineering Task Force](#)
- [Request for Comments](#)

### Man Pages:
- `ssh`
- `ssh-keygen`
- `env`

---

## Learning Objectives

By the end of this project, you should be able to:

- Explain what a server is and where they usually reside.
- Describe SSH and its purpose.
- Generate an SSH RSA key pair.
- Connect to a remote server using an SSH RSA key.
- Understand why `#!/usr/bin/env bash` is preferred over `/bin/bash`.

---

## Requirements

- **Allowed Editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS
- **All scripts must be executable.**
- **All files must end with a new line.**
- **Bash scripts must begin with:**
  ```bash
  #!/usr/bin/env bash
