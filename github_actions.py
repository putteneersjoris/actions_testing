import os
import datetime

# Read the content of 'text.txt'
with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

# Generate the text with the current time
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
generated_text = f"generated with python on {time}\n{content}"

# Save the generated text to 'actions.txt'
with open('actions.txt', 'w') as file:
    file.write(generated_text)

# Check if 'actions.txt' exists and print its path if it does, or print "file not found" if it doesn't
if os.path.exists('blabla.txt'):
    file_path = os.path.abspath('actions.txt')
    print("Path of 'actions.txt':", file_path)
else:
    print("File not found.")

print("Script executed successfully.")