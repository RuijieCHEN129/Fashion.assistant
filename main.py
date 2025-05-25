from modules.ui import get_user_preferences, display_suggestions
from modules.engine import FashionAssistantFactory
from modules.config import load_config
from modules.history import display_history


def main():
    # Load configuration
    config = load_config('config/settings.json')
    print("=== Welcome to Fashion Assistant ===")

    # Optionally display history
    view_hist = input("Would you like to view past suggestions history? (y/n): ").strip().lower()
    if view_hist == 'y':
        display_history()

    prefs = get_user_preferences()

    assistant = FashionAssistantFactory.get_assistant(prefs['age'])
    suggestions = assistant.suggest_outfits(prefs)

    display_suggestions(suggestions)

    # Email notification if enabled
    if config.get('email_notify'):
        from modules.notifier import EmailNotifier
        notifier = EmailNotifier(config)
        notifier.send_email(prefs, suggestions)


if __name__ == '__main__':
    main()


