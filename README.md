# onPrep

Interview prep for software engineers. Study Python (more languages coming) with 424 questions, dual study modes, and deadline-based scheduling.

**Links:** [Buy Me a Coffee](https://buymeacoffee.com/prakersh)

## What it does

- **Study mode** — Pick a topic, read detailed explanations with runnable code. Switch to quick recap when revising.
- **424 questions** across 28 Python modules (data types to design patterns).
- **Schedule interviews** — Add multiple upcoming interviews with dates. Get a daily study plan auto-generated for each.
- **Track progress** — See what you've completed, what's in progress, and what's left.
- **Light/Dark mode** — Toggle between themes. Dark mode uses pitch black for OLED screens.

## Quick start

```bash
# Clone and setup
git clone https://github.com/prakersh/onPrep.git
cd onPrep
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create database and load questions
flask db upgrade
flask seed python

# Start the app
flask run
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## How to use

1. **Dashboard** — Overview of your progress, upcoming interviews, and today's study plan.
2. **Study** — Pick Python, browse 28 topics. Click any question in the sidebar to read the answer. Toggle between Detailed and Quick modes.
3. **Planner** — Add interviews (company, role, date). A study schedule is auto-generated. You can track multiple interviews at once.

## Tech stack

| Layer | Tool |
|-------|------|
| Backend | Flask, SQLAlchemy, SQLite |
| Frontend | Tailwind CSS, Jinja2, Highlight.js |
| Markdown | mistune (tables, code, lists) |
| Tests | pytest (67 tests, 93% coverage) |

## Run tests

```bash
pytest --cov=app -v
```

## Project layout

```
app/
  blueprints/    # Routes: dashboard, study, planner, api
  models/        # DB models: content, progress
  services/      # Scheduler logic
  templates/     # Jinja2 HTML templates
seeds/
  python/        # 28 JSON files with questions + answers
  seed_runner.py # Loads JSON into the database
tests/           # Mirrors app/ structure
```

## Adding content

Each topic is a JSON file in `seeds/python/`. To add questions:

1. Edit or create a numbered JSON file (e.g., `29_new_topic.json`)
2. Add the concept to `seeds/python/_meta.json`
3. Run `flask seed python`

Every question needs two answers: `detailed` (full explanation + code) and `quick` (key points only).

## Support

If onPrep helps your interview prep, consider buying me a coffee:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/prakersh)
