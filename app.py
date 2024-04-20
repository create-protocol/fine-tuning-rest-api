from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from together import Together
import tempfile
app = Flask(__name__)

# Initialize Together client with your API key
client = Together(api_key="35a1728aef770370b31b29fbd6572d5f7f89770a17cf1a1f941b967c71c85905")


@app.route('/upload', methods=['POST'])
def upload_file():
    
    file_path = "/Users/B0295868/Downloads/together-1.1.2/testing.jsonl"
    # Upload the file using the Together client
    try:
        response = client.files.upload(file=file_path)
        
        # Construct a serializable response
        serializable_response = {
            "id": response.id,
            "object": response.object,
            "created_at": response.created_at,
            "filename": response.filename,
            "bytes": response.bytes,
            "line_count": response.line_count,
            "processed": response.processed,
            # Add more fields as needed
        }
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify(serializable_response), 201

@app.route('/list-uploaded-files', methods=['GET'])
def list_uploaded_files():
    # Call the .list() method to get a list of uploaded files
    files_list = client.files.list()
    
    # Convert the files_list into a list of dictionaries
    # Adjust the attributes ('id', 'name') based on your File object's actual structure
    files_data = files_list.data
    
    # Return the list of files as a JSON response
    return jsonify(files_data)

if __name__ == '__main__':
    app.run(debug=True)
