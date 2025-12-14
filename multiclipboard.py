import sys
import clipboard
import json
import os

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print(f"Data saved successfully under key: '{key}'")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print(f"Data copied to clipboard from key: '{key}'")
        else:
            print("Key does not exist.")

    elif command == "list":
        if data:
            print("Saved items:")
            for key, value in data.items():
                # Show first 50 chars of value for preview
                preview = (value[:47] + '...') if len(value) > 47 else value
                print(f"- {key}: {preview}")
        else:
            print("No items saved yet.")
    else:
        print("Unknown command")

elif len(sys.argv) == 3:
    # Support 'python multiclipboard.py save <key>' style
    command = sys.argv[1]
    key = sys.argv[2]
    data = load_data(SAVED_DATA)

    if command == "save":
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print(f"Data saved successfully under key: '{key}'")
    elif command == "load":
        if key in data:
            clipboard.copy(data[key])
            print(f"Data copied to clipboard from key: '{key}'")
        else:
            print("Key does not exist.")
    else: 
        print("Unknown command")

else: 
    print("Please pass exactly one command.")
    print("Usage: python multiclipboard.py [save|load|list]")