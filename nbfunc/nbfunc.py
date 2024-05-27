import os
import re
from nbconvert import ScriptExporter
from traitlets.config import Config

def convert_notebook_to_script(notebook_path):
    # Create a configuration to adjust the nbconvert settings
    config = Config()
    config.ScriptExporter.exclude_input_prompt = True

    # Create a ScriptExporter instance with the specified configuration
    exporter = ScriptExporter(config=config)

    # Convert the notebook to a script
    script, resources = exporter.from_filename(notebook_path)
    return script

def find_python_functions(script):
    # Regular expression to find function definitions
    pattern = r'def\s+\w+\s*\([^)]*\)\s*:'
    functions = re.findall(pattern, script)
    return functions

def main():
    # Process each .ipynb file in the current directory
    for file_name in os.listdir('.'):
        if file_name.endswith('.ipynb'):
            print(f"Processing {file_name}...")
            script = convert_notebook_to_script(file_name)
            functions = find_python_functions(script)
            
            if functions:
                print(f"Functions found in {file_name}:")
                for function in functions:
                    print(function)
            else:
                print("No functions found.")

if __name__ == '__main__':
    main()