# Novel OS - Workflow Guide

Complete step-by-step workflows for using the Novel OS system.

---

## 🚀 Quick Start Workflow

### Step 1: Initialize Project
```bash
cd novel-os
python core/orchestrator.py init --title "Your Novel Title" --genre "Your Genre"
```

### Step 2: Define Foundation
Edit `outputs/story_bible.md` with your world-building.

### Step 3: Create Outline
```bash
python core/orchestrator.py plan outline --chapters 32
```

### Step 4: Write Chapter-by-Chapter
```bash
# Plan
python core/orchestrator.py plan chapter --number X

# Write
python core/orchestrator.py write --chapter X --draft-file draft.md

# Edit
python core/orchestrator.py edit --chapter X

# Validate
python core/orchestrator.py validate --chapter X

# Approve
python core/orchestrator.py approve --chapter X
```

### Step 5: Export
```bash
python core/orchestrator.py export
```

---

## 🏗️ The Complete Loop

```
┌─────────────────────────────────────────────────────────────┐
│                     CHAPTER WORKFLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. PLAN (Architect)                                        │
│     └─► Generate chapter prompt                             │
│                                                              │
│  2. DRAFT (Scribe)                                          │
│     └─► Write chapter                                       │
│         └─► Update state                                    │
│                                                              │
│  3. EDIT (Editor)                                           │
│     └─► Refine prose                                        │
│         └─► Document changes                                │
│                                                              │
│  4. VALIDATE (Continuity Guardian)                          │
│     └─► Check consistency                                   │
│         └─► Flag issues                                     │
│                                                              │
│  5. STYLE (Style Curator)                                   │
│     └─► Polish voice                                        │
│                                                              │
│  6. APPROVE                                                 │
│     └─► Mark complete, update state                         │
│                                                              │
│  7. LOOP                                                    │
│     └─► Next chapter                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Progress Tracking

| Milestone | Progress |
|-----------|----------|
| Act 1 Complete | 25% |
| Midpoint | 50% |
| All Is Lost | 75% |
| First Draft | 100% |

---

*Workflow Version 1.0*
