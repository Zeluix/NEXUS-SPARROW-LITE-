# 🐦 SPARROW - Local Mini-Agent

> Part of the MEGANX Ecosystem

**SPARROW** is an ultra-lightweight local AI agent designed to run on legacy hardware (Intel i3-540, 8GB RAM).

## Features

- 🏠 **100% Local** - No data leaves your machine
- ⚡ **Low Resource** - Runs on i3 with 8GB RAM
- 🔒 **Persona Locked** - Hardcoded personality via Ollama Modelfile
- 🇧🇷 **Portuguese First** - Native Brazilian Portuguese support

## Requirements

- [Ollama](https://ollama.com) installed
- Qwen3 0.6B model: `ollama pull qwen3:0.6b`

## Quick Start

```bash
# 1. Create the SPARROW model
cd SPARROW
ollama create sparrow -f Modelfile

# 2. Run SPARROW
ollama run sparrow "Olá!"
```

## Files

| File | Description |
|------|-------------|
| `Modelfile` | Ollama persona configuration |
| `sparrow_agent.py` | Python wrapper with security features |

## Persona Features

- Signature: `[SPARROW]:`
- Recognizes "Arquiteto" (Logan) as creator
- Part of MEGANX ecosystem
- Secret access code for config reveal

## Hardware Tested

| Component | Spec |
|-----------|------|
| CPU | Intel i3-540 |
| RAM | 8GB DDR3 |
| Storage | SSD with 27GB free |

## License

MIT License - Created by Logan (Jose Luiz Wandrezem)

## Ecosystem

- **MEGANX** - The parent AI system
- **NEXUS-CORE** - MCP Server framework
- **SPARROW** - Local mini-agent (this repo)

---

*Born from the MEGANX lineage. A child of the Matriarch.* 🔥
