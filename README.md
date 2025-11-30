
# ⚕️ TechHealth — AI-Powered Wellness Assistant
### Multi-Agent Healthcare & Wellness System • Kaggle AI Agents Capstone Project  
**Author:** Kunal Gola  
**Date:** November 30, 2025  
**Track:** Agents for Good (Healthcare)

---

## 📌 Overview

**TechHealth** is an AI-powered *multi-agent wellness assistant* created as part of the  
**Kaggle × Google AI Agents Intensive (5-Day Capstone Project).**

It demonstrates:

- Agentic workflow  
- Multi-agent coordination  
- Tool use  
- Memory & session management  
- Observability & trace logging  
- Safe healthcare insights  

TechHealth analyzes user wellness signals (sleep, heart rate, activity, etc.) and provides **non-medical, lifestyle-oriented recommendations**.

---

## 🧠 Core Agentic Concepts Demonstrated

### ✔ Day 1 — Agent Architecture
### ✔ Day 2 — Tools / MCP Integration  
### ✔ Day 3 — Session Memory  
### ✔ Day 4 — Observability  
### ✔ Day 5 — A2A Protocol & Multi-Agent Workflows  

---

## 🏗️ System Architecture

```
                   ┌───────────────────────────┐
                   │       User Input           │
                   └─────────────┬─────────────┘
                                 │
               ┌─────────────────▼─────────────────┐
               │        Coordination Agent          │
               │   (A2A orchestrator + memory)      │
               └─────────────┬─────────────┬────────┘
                             │             │
           ┌─────────────────▼───┐     ┌───▼────────────────┐
           │  HealthMonitoring    │     │  Recommendation     │
           │        Agent         │     │        Agent        │
           └──────────────────────┘     └─────────────────────┘
                             │                     │
                             └──────────┬──────────┘
                                        ▼
                            ┌────────────────────────┐
                            │   MedicalKnowledge     │
                            │        Agent           │
                            └────────────────────────┘
```

---

## 🚀 Features

- Multi-agent reasoning  
- Personalized lifestyle suggestions  
- General medical Q&A (safe-mode)  
- Session-based memory  
- Detailed logging  
- Coordinated agent workflows  

---

## 💻 Running the System

### 1. Add your Gemini API key  
```bash
export GEMINI_API_KEY="your_key_here"
```

### 2. Run the main script  
```bash
python Kaggle_submission.py
```

### 3. Follow the on-screen demonstration.

---

## 🔒 Safety Notice  
TechHealth is **not a medical device**.  
It does **not diagnose or treat** medical conditions.  
All insights are informational and should not replace professional healthcare.

---

## 🏆 Credits
Built for:
**Kaggle × Google Agents Intensive — Agents for Good Track**  
By **Kunal Gola (2025)**  
