# AI Checkout Call Processor

## Overview

This project is a **prototype backend** that explores how voice-agent platforms like Simple AI can be extended into real operational workflows.

Instead of treating AI calls as just conversations, this system demonstrates how **post-call automation** can transform technician voice interactions into structured business actions such as:

- Updating inventory automatically
- Logging work done
- Generating invoices instantly

## The Hands-Free Checkout Workflow (Concept)

This prototype explores a simple idea:

Instead of technicians manually scrolling through long parts lists or filling digital forms after a job, the checkout process becomes voice-first and hands-free.

### 1. The Call

After finishing a job, the technician starts an AI checkout call.

Example:
"Hey AI, start checkout."

The agent asks for a natural summary of the work completed.

---

### 2. Natural Work Summary

The technician speaks normally:

"I replaced two standard chrome bathroom taps and one rubber washer on the hot water line. The leak is fixed and I tested the pressure. Bill for parts and one hour of labor."

No menus. No checkboxes.

---

### 3. AI Processing

The analyzer extracts structured data:

- Quantity: 2  
  Item: Standard Chrome Tap

- Quantity: 1  
  Item: Rubber Washer

- Service: 1 Hour Labor

This mirrors how voice platforms like Simple AI process transcripts into automation-ready outputs.

---

### 4. Instant Invoice Draft

By the time the technician leaves the site:

- Inventory is updated
- Work notes are logged
- A draft invoice appears in the field ops system

Minimal friction, no manual entry.

---

## Why Voice Checkout Beats Manual Forms

- **Zero Data Entry**  
  Technicians describe work while packing tools instead of tapping through long parts lists.

- **More Accurate Notes**  
  Voice narration captures richer internal details that are often skipped when typing.

- **Safety and Cleanliness**  
  No need to handle a phone with dirty hands during field work.

### Core Idea

> A technician finishes a job narrates what they did during an AI checkout call the backend extracts structured data inventory updates + invoice generation happen automatically.

This repository simulates how a real customer integration could be built on top of a Simple AI style architecture using:

- `transcripts`
- `analyzers`
- `analysis_results`
- `summary`

## Fast Setup

**1. Install**
```bash
pip install -r requirements.txt
```

**2. Run Server**
```bash
uvicorn app.main:app --reload
```

**3. Test Simulation**
```bash
python test_simulation.py
```

This sends a simulated call payload, updates the database, and generates an PDF invoice in `generated_invoices/`.

"I replaced the P-trap and used two one-inch copper fittings."

---

## Setup & Usage

### 1 Install Dependencies
```bash
pip install -r requirements.txt
```

### 2 Run the Server
Start the FastAPI server with hot-reloading:

```bash
uvicorn app.main:app --reload
```
- **Webhook Endpoint**: `http://127.0.0.1:8000/calls/webhook`
- **Interactive Docs**: `http://127.0.0.1:8000/docs`

### 3 Test the Full Flow
A simulation script is included to replicate a technician checkout call.

Step 1  Start Server
```bash
uvicorn app.main:app --reload
```

Step 2  Run Simulation
```bash
python test_simulation.py
```

The script will:
- Send a simulated call payload
- Trigger analyzer processing
- Update inventory
- Generate an invoice PDF

Generated files appear in:
`generated_invoices/`

---

## Internal Architecture

```text
app/
 +-- main.py                # FastAPI entrypoint
 +-- api/                   # Routes and webhook handling
 +-- services/              # CallProcessor + AnalyzerEngine
 +-- workers/               # Background automation tasks
 +-- schemas/               # Call + business models
 +-- db/                    # Inventory database logic
 +-- utils/                 # Invoice generation
 +-- core/                  # Config + logging
```

### Core Components
**CallProcessor**
- Orchestrates the lifecycle of a call event
- Coordinates analyzers and automation

**AnalyzerEngine**
- Runs analysis modules similar to Simple AI analyzers
- Generates structured `analysis_results`

**Extractor Service**
- Converts technician narration into structured data

**Background Tasks**
- Handles inventory updates and invoice generation asynchronously

## Future Improvements

- Plug real LLM structured extraction into extractor layer
- Support multilingual technician narration
- Add streaming transcript processing
- Replace SQLite with production database
- Integrate directly with Simple AI webhook events

