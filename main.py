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
    if "ref" in data:
        master = data["repository"]["master_branch"] if "master_branch" in "master_branch" in data["repository"] else "master"
        if data["repository"]["default_branch"] == master:
            subprocess.check_output(
                [
                    SHELL_SCRIPT, 
                    " ".join([
                        data["repository"]["clone_url"], # repository url
                        data["repository"]["name"].lower() + ":" + VERSION_TYPE, # image name
                        data["repository"]["name"]
                    ])
                ]) # container name
        else:
            logging.info("Not a push to the masterbranch --> not building")
    else:
        logging.info("Probably not usefull, no reference in request")

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')