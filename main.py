from flask import Flask, request, jsonify
app = Flask(__name__)

import logging
import subprocess

SHELL_SCRIPT = "build_image.sh"
VERSION_TYPE = "daily"

@app.route('/github', methods=['POST'])
def push():
    logging.info("Received new push!")
    data = request.get_json()

    if data["repository"]["default_branch"] == data["repository"]["master_branch"]:
        subprocess.call(
            [
                SHELL_SCRIPT, data["repository"]["clone_url"]], # repository url
                data["repository"]["name"].lower() + ":" + VERSION_TYPE, # image name
                data["repository"]["name"]) # container name
    else:
        logging.info("Not a push to the masterbranch --> not building")

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')