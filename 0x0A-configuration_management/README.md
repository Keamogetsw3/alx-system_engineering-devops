# 0x0A. Configuration Management

## DevOps | SysAdmin | Scripting | CI/CD

### Project Overview
This project focuses on **Configuration Management** using **Puppet** to automate infrastructure setup and management. Configuration management ensures consistency across servers, making deployments efficient, reliable, and scalable.

### Background Context
While working with large-scale infrastructure, automation tools like **Puppet** help in managing server configurations, reducing manual workload, and preventing errors. This project provides hands-on experience in writing Puppet manifests to manage files, packages, and services.

### Resources
To successfully complete this project, you should review the following materials:

- [Intro to Configuration Management](https://puppet.com/docs/puppet/latest/config_intro.html)
- [Puppet resource type: file](https://puppet.com/docs/puppet/latest/types/file.html)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/docs/puppet/latest/lang_summary.html)
- [Puppet lint](https://github.com/rodjek/puppet-lint)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

### Requirements
#### General
- All files will be interpreted on **Ubuntu 20.04 LTS**.
- Files should end with a **new line**.
- A `README.md` file is **mandatory** at the root of the project folder.
- Puppet manifests must:
  - Pass `puppet-lint` **version 2.1.1** without errors.
  - Run **without errors**.
  - Begin with a comment explaining the purpose of the manifest.
  - Have a `.pp` file extension.

