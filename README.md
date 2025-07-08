# 🧪 Sprint 8 — Automação de Testes Web com Python e Selenium

Este repositório contém o projeto desenvolvido durante a **Sprint 8** do Bootcamp de Qualidade de Software da [Tripleten], com foco na **automação de testes de aplicações web** utilizando **Python** e **Selenium WebDriver**.

---

## 🎯 Objetivos da Sprint

- Compreender os fundamentos da automação de testes
- Aplicar **programação orientada a objetos (POO)** em Python
- Automatizar casos de teste para aplicações web
- Utilizar o padrão **Page Object Model (POM)**
- Localizar elementos da interface usando diferentes estratégias

---

## 🛠️ Tecnologias e Ferramentas

- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **VS Code / PyCharm**
- **Git & GitHub**

---

## 🧱 Estrutura do Projeto

```
📁 QA-Brazil_Python_Automation_S8
├── 📁 pages/          # Arquivos de Page Object Model (POM)
├── 📁 tests/          # Scripts de teste com Pytest
├── 📁 utils/          # Utilitários (ex: métodos auxiliares, setup)
├── conftest.py        # Configurações globais do Pytest
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

---

## ▶️ Como Executar os Testes

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/DRACKRAGE/QA-Brazil_Python_Automation_S8.git
   cd QA-Brazil_Python_Automation_S8
   ```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes**:
   ```bash
   pytest tests/
   ```

---

## 📌 Conceitos Aplicados

- **Page Object Model (POM)**: padrão de projeto que melhora a manutenibilidade dos testes.
- **Localização de elementos**: uso de `find_element` com estratégias como `By.ID`, `By.XPATH`, `By.CSS_SELECTOR`, entre outras.
- **Pytest**: estrutura de testes simples e eficaz com suporte a fixtures, asserts e relatórios.
- **Organização modular**: separação de responsabilidades entre testes, páginas e utilitários.

---

## 👨‍💻 Autor

**Bruno dos Santos Souza**  
📍 São José dos Campos, SP  
🔗 [LinkedIn](https://www.linkedin.com/in/bruno-dos-santos-souza/)  
🎓 QA | Automação de testes com Python, Selenium e Pytest

---

> Este projeto representa a aplicação prática de conceitos de automação de testes aprendidos na Sprint 8 do Bootcamp de QA da Tripleten.