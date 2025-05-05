import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Path where the ConfigMap volume is mounted
CONFIG_FILE_PATH = '/config/shape-color.txt'
DEFAULT_COLOR = 'white' # Default if file is missing or empty

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/config')
def get_config():
    """Reads the color from the mounted ConfigMap file and returns it as JSON."""
    color = DEFAULT_COLOR
    try:
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, 'r') as f:
                file_content = f.read().strip()
                if file_content: # Use content only if not empty
                    color = file_content
                else:
                    print(f"Warning: Config file '{CONFIG_FILE_PATH}' is empty, using default.")
        else:
            print(f"Warning: Config file '{CONFIG_FILE_PATH}' not found, using default.")
    except Exception as e:
        print(f"Error reading config file '{CONFIG_FILE_PATH}': {e}")
        # Keep default color on error

    return jsonify({'color': color})

@app.route('/healthz')
def healthz():
    """Basic health check endpoint."""
    return "OK", 200

if __name__ == '__main__':
    # Use 0.0.0.0 to be accessible within the container network
    # Port 5000 is the Flask default
    app.run(host='0.0.0.0', port=5000) 