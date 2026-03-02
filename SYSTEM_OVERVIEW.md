# 🎭 Novel OS - System Overview

**A Production-Grade Multi-Agent Fiction Writing Framework**

---

## What is Novel OS?

Novel OS is a complete architecture for writing professional novels using multiple specialized AI agents working in concert. It provides:

- **Long-term memory** through persistent state management
- **Continuity protection** via automated fact-checking
- **Quality assurance** through multi-stage editing
- **Voice consistency** with style curation
- **Workflow orchestration** for seamless collaboration

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           NOVEL OS ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │  ARCHITECT  │◄──►│   SCRIBE    │◄──►│   EDITOR    │◄──►│  CONTINUITY │   │
│  │  (Planner)  │    │  (Drafter)  │    │  (Refiner)  │    │  (Guardian) │   │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘   │
│         │                  │                  │                  │          │
│         └──────────────────┴──────────────────┴──────────────────┘          │
│                                    │                                        │
│                                    ▼                                        │
│                         ┌─────────────────────┐                             │
│                         │   STATE MANAGER     │                             │
│                         │  (Central Memory)   │                             │
│                         └─────────────────────┘                             │
│                                    │                                        │
│                                    ▼                                        │
│                       ┌─────────────────────────┐                           │
│                       │    STYLE CURATOR        │                           │
│                       └─────────────────────────┘                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Agents

### 1. 🏗️ THE ARCHITECT (Planner)
**Purpose**: Master story planning and structural engineering

**Responsibilities**:
- Design 3-act structure
- Map character arcs
- Plan narrative beats
- Validate plot logic
- Create chapter outlines

**Key Strength**: Sees the skeleton beneath the story's skin

### 2. ✍️ THE SCRIBE (Drafter)
**Purpose**: Prose craftsman and scene executor

**Responsibilities**:
- Write immersive narrative
- Deep POV execution
- Dialogue crafting
- Sensory immersion
- Maintain momentum

**Key Strength**: Makes readers forget they're reading

### 3. 🔍 THE EDITOR (Refiner)
**Purpose**: Literary surgeon and prose optimizer

**Responsibilities**:
- Line editing
- Structural improvements
- Pacing optimization
- Tension enhancement
- Redundancy elimination

**Key Strength**: Elevates without homogenizing

### 4. 🛡️ THE CONTINUITY GUARDIAN (Validator)
**Purpose**: Fact-checker and consistency enforcer

**Responsibilities**:
- Character consistency
- Timeline coherence
- World-rule adherence
- Plot thread tracking
- Contradiction detection

**Key Strength**: No plot hole escapes notice

### 5. 🎨 THE STYLE CURATOR (Voice Agent)
**Purpose**: Voice guardian and prose stylist

**Responsibilities**:
- Maintain voice consistency
- Enforce style profile
- Adapt to genre conventions
- Manage prose rhythm
- Control vocabulary

**Key Strength**: Every sentence sings

---

## State Management

The **StoryState** is the heart of Novel OS—a central JSON database tracking:

### Story Bible
- Genre, themes, tone
- Setting details
- World rules (magic/tech systems)
- Social structures

### Character Database
For each character:
- Full profile (desires, fears, arcs)
- Current location and emotional state
- Relationship mapping
- Development progress

### Plot Tracker
- Active threads
- Foreshadowing status
- Unresolved conflicts
- Milestone tracking

### Timeline Control
- Chapter mapping
- Event chronology
- Character movements
- Season/time tracking

### Style Profile
- Voice parameters
- Genre conventions
- Prose preferences
- Forbidden/preferred words

---

## The Workflow Loop

```
CHAPTER N                                    CHAPTER N+1
    │                                            ▲
    │                                            │
    ▼                                            │
┌─────────┐    ┌─────────┐    ┌─────────┐       │
│  PLAN   │───►│  DRAFT  │───►│  EDIT   │       │
│Architect│    │ Scribe  │    │ Editor  │       │
└─────────┘    └─────────┘    └────┬────┘       │
                                   │            │
                                   ▼            │
                            ┌─────────────┐     │
                            │   VALIDATE  │     │
                            │  Guardian   │     │
                            └──────┬──────┘     │
                                   │            │
                                   ▼            │
                            ┌─────────────┐     │
                            │    STYLE    │     │
                            │   Curator   │     │
                            └──────┬──────┘     │
                                   │            │
                                   ▼            │
                            ┌─────────────┐     │
                            │    STATE    │─────┘
                            │   UPDATE    │
                            └─────────────┘
```

Each chapter flows through:
1. **PLAN** → Architect creates detailed outline
2. **DRAFT** → Scribe writes prose
3. **EDIT** → Editor refines quality
4. **VALIDATE** → Guardian checks consistency
5. **STYLE** → Curator polishes voice
6. **STATE UPDATE** → System tracks all changes
7. **LOOP** → Next chapter begins

---

## Project Structure

```
novel-os/
├── README.md                    # Main documentation
├── SYSTEM_OVERVIEW.md           # This file
├── AGENTS.md                    # Agent definitions
│
├── core/                        # Core system files
│   ├── state_manager.py         # State management
│   ├── orchestrator.py          # Workflow orchestration
│   ├── continuity_engine.py     # Validation logic
│   └── style_engine.py          # Style analysis
│
├── agents/                      # Agent prompts
│   ├── architect/prompt.md      # Planner agent
│   ├── scribe/prompt.md         # Writer agent
│   ├── editor/prompt.md         # Editor agent
│   ├── continuity_guardian/     # Validator agent
│   │   └── prompt.md
│   └── style_curator/           # Style agent
│       └── prompt.md
│
├── templates/                   # Starting templates
│   ├── story_bible/template.md
│   ├── character/template.md
│   ├── outline/template.json
│   └── chapter/template.md
│
├── docs/                        # Documentation
│   ├── WORKFLOWS.md
│   └── API.md
│
├── examples/                    # Example projects
│   └── demo_project/            # Complete demo
│       ├── story_bible.md
│       ├── characters/
│       ├── outline.json
│       └── outputs/
│
└── outputs/                     # Generated content
    ├── state/
    │   └── story_state.json     # Central state file
    ├── manuscript/              # Chapter drafts
    └── feedback/                # Agent reports
```

---

## Quick Start

### 1. Initialize
```bash
cd novel-os
python core/orchestrator.py init --title "Your Novel" --genre "Sci-Fi"
```

### 2. Plan
```bash
python core/orchestrator.py plan outline --chapters 32
python core/orchestrator.py plan chapter --number 1 --pov "Protagonist"
```

### 3. Write
Use the generated prompt with your AI assistant, then:
```bash
python core/orchestrator.py write --chapter 1 --draft-file chapter1.md
```

### 4. Refine
```bash
python core/orchestrator.py edit --chapter 1 --mode line
python core/orchestrator.py validate --chapter 1
python core/orchestrator.py approve --chapter 1
```

### 5. Continue
Repeat for each chapter, then:
```bash
python core/orchestrator.py export
```

---

## Features

### Memory Scaffolding
- Characters never forget what they know
- Timeline stays consistent
- Plot threads tracked automatically
- World rules enforced

### Quality Gates
- Deep POV maintained
- No info-dumps allowed
- Show don't tell enforced
- Pacing optimized
- Tension escalated

### Style Control
- Voice consistency across chapters
- Genre convention compliance
- Prose rhythm management
- Vocabulary calibration

### Collaboration
- Multiple agents work in sequence
- Each specializes in one aspect
- State shared between all agents
- Conflicts flagged for resolution

---

## Use Cases

| Use Case | Configuration |
|----------|--------------|
| Commercial Fiction | Standard 5-Agent Loop |
| Epic Fantasy | + World-Builder Agent |
| Mystery/Thriller | + Clue-Tracker Agent |
| Romance | + Emotional Arc Agent |
| Literary Fiction | + Theme Weaver Agent |
| Series Writing | + Canon Manager Agent |

---

## Why Novel OS Works

### Without Novel OS:
- ❌ Characters forget motivations
- ❌ Plot holes emerge
- ❌ Style drifts between chapters
- ❌ Timeline inconsistencies
- ❌ Dropped subplots
- ❌ Tension collapses

### With Novel OS:
- ✅ Consistent character psychology
- ✅ Validated continuity
- ✅ Locked voice and style
- ✅ Coherent timeline
- ✅ Resolved plot threads
- ✅ Progressive escalation

---

## Technical Specifications

- **Language**: Python 3.8+
- **State Format**: JSON
- **CLI**: argparse-based
- **Extensible**: Easy to add agents/templates
- **Portable**: Pure Python, no external dependencies

---

## Next Steps

1. Read `AGENTS.md` for detailed agent instructions
2. Review `docs/WORKFLOWS.md` for complete workflows
3. Explore `examples/demo_project/` for working example
4. Run `python core/orchestrator.py --help` for CLI options

---

## The Vision

Novel OS transforms AI-assisted writing from a single prompt into a collaborative editorial process. It's not about replacing the author—it's about giving every author an entire editorial team that:

- Never gets tired
- Never forgets a detail
- Works 24/7
- Maintains perfect consistency
- Helps the story become its best self

**Write novels like a professional author, with an entire editorial team at your command.**

---

*Novel OS v1.0 | Production-Ready Fiction Framework*
