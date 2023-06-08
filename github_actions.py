import os
import datetime

# Read the content of 'text.txt'
with open('text.txt', 'r') as file:
    content = file.read()
    print(content)

# Generate the text with the current time
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
generated_text = f"generated with python on {time}\n{content}"

# Save the generated text to 'actions.txt' or 'actions_testing.txt'
if os.path.exists('actions.txt'):
    file_path = 'actions.txt'
else:
    file_path = 'actions_testing.txt'
    with open(file_path, 'w') as file:
        file.write(generated_text)
    print(f"Created new file: {file_path}")

# Print the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()
    print(file_content)

print("Script executed successfully.")