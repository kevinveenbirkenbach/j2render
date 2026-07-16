# 🧩 j2render
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


**j2render** is a minimal CLI tool to render [Jinja2](https://palletsprojects.com/p/jinja/) templates into final output files (YAML, config files, Markdown, etc.). It's ideal for templating Ansible variables, configuration files, and other structured data.

---

## 🚀 Installation

You can install **j2render** via [Kevin's Package Manager (pkgmgr)](https://github.com/kevinveenbirkenbach/package-manager):

```bash
pkgmgr install j2render
```

This will automatically make the `j2r` command available in your system, pointing to `main.py`.

---

## ⚙️ Usage

```bash
j2r <template-file> <output-file>
```

### Example:

```bash
j2r templates/config.yml.j2 output/config.yml
```

This command will render `config.yml.j2` using Jinja2 and save the result as `config.yml`.

---

## 📝 Features

- 🔄 Simple and clean rendering pipeline
- 📁 Template file discovery via Jinja2 `FileSystemLoader`
- ✅ Supports any text-based output (YAML, JSON, Markdown, etc.)
- 🧠 Useful for Ansible, Docker, templated documentation, and more

---

## 🧑‍💻 Author

**Kevin Veen-Birkenbach**  
🌐 [https://www.veen.world/](https://www.veen.world/)  
📦 [GitHub – @kevinveenbirkenbach](https://github.com/kevinveenbirkenbach)

---

## 📄 License

This project is licensed under the **MIT License**.
