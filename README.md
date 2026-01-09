# Notes Converter Agent

An intelligent AI assistant built using **Google ADK** and **NVIDIA NIM**, designed to answer user queries with the **Llama 3.1 Nemotron Nano 8B** model.

---

## Overview

This project implements a lightweight and efficient AI agent that leverages NVIDIA’s optimized inference platform together with Google’s Agent Development Kit to deliver fast and reliable responses.

---

## Key Features

- 🤖 Agent-based architecture powered by **Google ADK**
- ⚡ Low-latency inference using **NVIDIA NIM**
- 🦙 Backed by **Llama 3.1 Nemotron Nano 8B**
- 🧩 Simple setup and easy extensibility
- 📝 Clean, minimal, and developer-friendly codebase

---

## Requirements

- Python **3.8 or higher**
- An active **NVIDIA NIM API key**  
  Get one at: https://build.nvidia.com/

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aabhaskhandelwal/Notes-converter.git
cd notes-converter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. **Set up environment variables**

Copy the sample environment file:

```bash
cp .env.sample .env
```

Edit `.env` and add your NVIDIA NIM API key:

```properties
NVIDIA_NIM_API_KEY=your_actual_api_key_here
NVIDIA_NIM_API_BASE="https://integrate.api.nvidia.com/v1/"
```

### Usage

```python
from my_agent.agent import root_agent

# The agent is ready to use
# Add your implementation here to interact with the agent
```

## My Implementation

```Input: YouTube URL
↓
Transcript Fetcher (tool)
↓
Notes Agent (LLM)
↓
Structured Notes (Markdown)
```
