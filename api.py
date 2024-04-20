from flask import Flask, request, jsonify
from src.together import Together

app = Flask(__name__)

@app.route('/fine-tuning/create', methods=['POST'])
def fine_tuning_create():
    # Extract data from the incoming request
    data = request.json
    training_file = data.get('training_file')
    model = data.get('model')
    n_epochs = data.get('n_epochs', 1)
    n_checkpoints = data.get('n_checkpoints', 1)
    batch_size = data.get('batch_size', 32)
    learning_rate = data.get('learning_rate', 3e-5)
    suffix = data.get('suffix')
    wandb_api_key = data.get('wandb_api_key')

    # Ensure the required parameters are present
    if not training_file or not model:
        return jsonify({"error": "Missing required parameters"}), 400

    # Initialize the Together client
    client = Together(api_key='your_api_key_here')  # Ensure you handle API key securely

    # Call the create method
    try:
        response = client.fine_tuning.create(
            training_file=training_file,
            model=model,
            n_epochs=n_epochs,
            n_checkpoints=n_checkpoints,
            batch_size=batch_size,
            learning_rate=learning_rate,
            suffix=suffix,
            wandb_api_key=wandb_api_key,
        )
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
