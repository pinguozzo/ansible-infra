import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Path to the Ansible playbooks directory
PLAYBOOKS_DIR = "/home/rex/src/ansible-infra/playbooks/satellite"

# Command to list available playbooks
def list_playbooks(update: Update, context: CallbackContext) -> None:
    try:
        # List YAML files in the playbooks directory
        playbooks = subprocess.check_output(["ls", PLAYBOOKS_DIR]).decode().splitlines()
        playbooks = [p for p in playbooks if p.endswith('.yml')]

        if playbooks:
            update.message.reply_text("Available playbooks:\n" + "\n".join(playbooks))
        else:
            update.message.reply_text("No playbooks found in the directory.")
    except Exception as e:
        update.message.reply_text(f"Error listing playbooks: {e}")

# Command to run a specific playbook
def run_playbook(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("Please provide the playbook name. Usage: /run <playbook_name>")
        return

    playbook_name = context.args[0]
    playbook_path = f"{PLAYBOOKS_DIR}/{playbook_name}"

    try:
        # Run the Ansible playbook
        result = subprocess.check_output(["ansible-playbook", playbook_path], stderr=subprocess.STDOUT).decode()
        update.message.reply_text(f"Playbook '{playbook_name}' executed successfully:\n{result}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error executing playbook:\n{e.output.decode()}")
    except Exception as e:
        update.message.reply_text(f"An unexpected error occurred: {e}")

# Main function to set up the bot
def main():
    # Replace 'YOUR_BOT_API_TOKEN' with your actual bot token
    updater = Updater(":")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("list", list_playbooks))
    dispatcher.add_handler(CommandHandler("run", run_playbook))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

