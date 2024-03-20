import os
import uuid
import argparse
import socket
from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Directory to store the uploaded files
UPLOAD_DIRECTORY = "uploads"

# Create the upload directory if it doesn't exist
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route("/paste/<filename>")
def get_file(filename):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return render_template_string("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Pasted File</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 20px;
                        background-color: #f0f0f0;
                    }
                    h1 {
                        color: #333;
                    }
                    pre {
                        background-color: #fff;
                        padding: 10px;
                        border-radius: 5px;
                        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                        overflow-x: auto;
                    }
                </style>
            </head>
            <body>
                <h1>Pasted File</h1>
                <pre>{{ content }}</pre>
            </body>
            </html>
            """, content=content)
    else:
        abort(404)

def paste_file(file_path):
    # Generate a unique filename
    filename = str(uuid.uuid4())
    # Copy the file to the upload directory
    destination_path = os.path.join(UPLOAD_DIRECTORY, filename)
    with open(file_path, "rb") as source_file, open(destination_path, "wb") as destination_file:
        destination_file.write(source_file.read())
    # Generate the URL for accessing the file
    url = f"http://localhost:55554/paste/{filename}"
    return url

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paste a file and generate a unique URL.")
    parser.add_argument("filename", help="Path to the file to be pasted.")
    args = parser.parse_args()

    file_path = os.path.abspath(args.filename)
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        exit(1)

    url = paste_file(file_path)
    print(f"File pasted successfully. Access it at: {url}")

    local_ip = get_local_ip()
    if local_ip:
        print(f"Access it at: http://{local_ip}:55554/paste/{os.path.basename(url)}")
        print(f"Warning: You might be under a NAT. You may wish to access the page at: http://{local_ip}:55554/paste/{os.path.basename(url)}")
    else:
        print("Unable to determine the local IP address.")

    app.run(host="0.0.0.0", port=55554)
