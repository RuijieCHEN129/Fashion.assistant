# Fashion.assistant
Fashion Assistant is a Python-based command-line application that helps users pick the perfect outfit by taking into account three key factors: age, current weather, and planned occasion. Whether you’re getting dressed for a casual weekend stroll, an important work meeting, or a fun night out, this tool curates age-appropriate combinations of tops, bottoms, and shoes to ensure you look—and feel—your best.

Key Features
Age-Aware Styling
The tool segments users into four age groups—Child (0–17), Youth (18–30), Adult (31–60), and Senior (61+)—and offers each group a tailored wardrobe palette to match generational preferences and comfort needs.

Weather & Occasion Matching
After entering just a few details (sunny/rainy/cold/hot and casual/work/outside for night), Fashion Assistant filters a built-in outfit database to recommend combinations that suit both the climate and the event.

Extensible Architecture
The code is organized into modular classes (ChildFashionAssistant, YouthFashionAssistant, etc.), making it easy to add new age groups, introduce fresh outfit entries, or plug in an external data source like a JSON file or online API.

History Tracking
Every set of user preferences and the resulting suggestions are logged to a local JSON file (data/history.json), enabling you to review past outfits and spot trends over time.

Optional Email Notifications
Configure SMTP settings in config/settings.json and flip an email_notify switch to automatically receive your personalized recommendations via email after each run.

Getting Started
Clone the repo and navigate into its directory.

Install any dependencies (currently only Python’s standard library is required).

The structure of this file is:
fashion-assistant/
├── main.py                  # Entry point
├── modules/                 # Package containing core modules
│   ├── __init__.py
│   ├── ui.py                # User interaction
│   ├── engine.py            # Core logic & factory
│   ├── storage.py           # Persist history
│   ├── history.py           # Display past suggestions
│   ├── config.py            # Load config settings
│   └── notifier.py          # Optional email notifications
├── assets/                  # Static assets
│   └── images/              # Outfit images
│       ├── sunny_relax.jpg
│       └── ...
├── data/                    # Data storage
│   └── history.json         # Saved preferences & suggestions
├── config/                  # Configuration files
│   └── settings.json        # email_notify flag, SMTP settings
└── logs/                    # Log files (if enabled)
    └── app.log
How to run: save all files and run the following command in your terminal: python main.py
 
