# Novel OS - API Reference

## Python API

### StoryState Class

```python
from core.state_manager import StoryState, Character, PlotThread

state = StoryState("/path/to/project")

# Characters
char = Character(id="char_001", full_name="Maya Chen", role="protagonist")
state.add_character(char)

# Plot threads
thread = PlotThread(id="plot_001", name="The Discovery", thread_type="main")
state.add_plot_thread(thread)

# Chapters
chapter = state.create_chapter(1, "The Beginning")
state.update_chapter(1, {"status": "complete"})

# Save
state.save_state()
```

### NovelOrchestrator Class

```python
from core.orchestrator import NovelOrchestrator

orch = NovelOrchestrator("/path/to/project")

orch.init_project("My Novel", "Science Fiction")
orch.plan_outline(32, 80000)
orch.write_chapter(1, draft_text)
orch.edit_chapter(1, mode="line")
orch.validate_chapter(1)
orch.approve_chapter(1)
orch.export(format="markdown")
```

---

## CLI Reference

```bash
# Initialize
python core/orchestrator.py init --title "Title" --genre "Genre"

# Characters
python core/orchestrator.py character add --name "Name" --role protagonist
python core/orchestrator.py character list

# Plot
python core/orchestrator.py plot add --name "Thread" --description "Desc"

# Planning
python core/orchestrator.py plan outline --chapters 32
python core/orchestrator.py plan chapter --number 1

# Writing
python core/orchestrator.py write --chapter 1 --draft-file draft.md

# Editing
python core/orchestrator.py edit --chapter 1 --mode line

# Validation
python core/orchestrator.py validate --chapter 1
python core/orchestrator.py approve --chapter 1

# Status & Export
python core/orchestrator.py status
python core/orchestrator.py export
```

---

*API Version 1.0*
