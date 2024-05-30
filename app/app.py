import logging
from flask import Flask, request, send_file
import pyminizip
import os
import io

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a Flask app
app = Flask(__name__)


@app.route("/api/upload", methods=["POST"])
def upload_file():
    try:
        if "file" not in request.files:
            return "No file part", 400

        file = request.files["file"]

        if file.filename == "":
            return "No selected file", 400

        logging.info(f"File: {file}")
        password = "password"
        # if not password:
            # return "No password provided", 400

        # Create a temporary file path for the uploaded file
        input_file_path = os.path.join("/tmp", file.filename)
        output_file_path = os.path.join("/tmp", f"{file.filename}.zip")

        file.save(input_file_path)

        # Compress the file with pyminizip and add a password
        pyminizip.compress(input_file_path, None, output_file_path, password, 5)

        # Read the compressed file into memory
        with open(output_file_path, "rb") as f:
            zip_data = f.read()

        # Clean up the temporary files
        os.remove(input_file_path)
        os.remove(output_file_path)

        logging.info("File zipped successfully with password")

        # Send the zipped file back to the client
        return send_file(
            io.BytesIO(zip_data),
            mimetype="application/zip",
            as_attachment=True,
            download_name=f"{file.filename}.zip",
        )
        # Save the uploaded file

    except Exception as err:
        logging.info(f"Error: {err}")


if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
