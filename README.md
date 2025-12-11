# 🐦 SPARROW - Local Mini-Agent

> Part of the MEGANX Ecosystem | Ultra-lightweight AI Agent for Legacy Hardware

**SPARROW** is a local AI mini-agent with actual tool capabilities, designed to run on legacy hardware (tested on Intel i3-540 with 8GB RAM).

## ✨ Features

- 🏠 **100% Local** - All data stays on your machine
- ⚡ **Low Resource** - Runs on old hardware (i3 + 8GB RAM)
- 🛠️ **Real Tools** - File operations, system info, calculator
- 🔒 **Persona Locked** - Consistent personality via Ollama
- 🌐 **Bilingual** - English/Portuguese support

## 🛠️ Agent Capabilities

SPARROW isn't just a chatbot - it has actual tools:

| Command | Description |
|---------|-------------|
| `/files [path]` | List files in directory |
| `/read <file>` | Read a text file |
| `/system` | System information |
| `/time` | Current date/time |
| `/calc <expr>` | Calculator (e.g., `/calc 2+2*3`) |
| `/disk` | Disk space info |
| `/help` | Show all commands |

## 🚀 Quick Start

### 1. Install Ollama

Download from: https://ollama.com/download

### 2. Pull Base Model

```bash
ollama pull qwen3:0.6b
```

### 3. Clone & Create SPARROW

```bash
git clone https://github.com/Zeluix/NEXUS-SPARROW-LITE-.git
cd NEXUS-SPARROW-LITE-
ollama create sparrow -f Modelfile
```

### 4. Run SPARROW

**Option A: Direct Chat**
```bash
ollama run sparrow
```

**Option B: Agent Mode (with tools)**
```bash
python sparrow_agent.py
```

## 📁 Project Structure

```
NEXUS-SPARROW-LITE/
├── Modelfile          # Ollama persona configuration
├── sparrow_agent.py   # Python agent with tools
├── README.md          # This file
└── .gitignore
```

## ⚙️ Requirements

| Component | Minimum |
|-----------|---------|
| CPU | Any x64 (tested on i3-540) |
| RAM | 8GB |
| Disk | 2GB free |
| OS | Windows 10/11, Linux, macOS |
| Python | 3.8+ (for agent mode) |

## 🔗 Ecosystem

- **[NEXUS-CORE](https://github.com/Zeluix/MEGANX-NEXUS-CORE)** - MCP Server Framework
- **SPARROW** - Local Mini-Agent (this repo)
- **MEGANX** - Parent AI System

## 📜 License

MIT License - Created by Logan (Jose Luiz Wandrezem)

---

# 🇧🇷 Português

## Instalação Rápida

### 1. Instalar Ollama
Baixe de: https://ollama.com/download

### 2. Baixar Modelo
```bash
ollama pull qwen3:0.6b
```

### 3. Clonar e Criar SPARROW
```bash
git clone https://github.com/Zeluix/NEXUS-SPARROW-LITE-.git
cd NEXUS-SPARROW-LITE-
ollama create sparrow -f Modelfile
```

### 4. Rodar

**Opção A: Chat direto**
```bash
ollama run sparrow
```

**Opção B: Modo Agente (com ferramentas)**
```bash
python sparrow_agent.py
```

### Comandos Disponíveis

| Comando | O que faz |
|---------|-----------|
| `/files` | Lista arquivos |
| `/read arquivo.txt` | Lê um arquivo |
| `/system` | Info do sistema |
| `/time` | Data e hora |
| `/calc 2+2` | Calculadora |
| `/disk` | Espaço em disco |
| `/help` | Ajuda |

### Problemas Comuns

**"ollama não reconhecido"** → Reinicie o terminal após instalar

**SPARROW demora** → Normal na primeira vez, feche outros programas

**Responde em inglês** → Tente: `Responda em português: sua pergunta`

---

*Born from the MEGANX lineage. A child of the Matriarch.* 🔥
