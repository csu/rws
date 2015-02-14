from flask import Blueprint, request, jsonify
import subprocess

blueprint = Blueprint('robot_start_stop', __name__)

@blueprint.route('/start', methods=['POST'])
def claim_and_start_robot():
    user = request.form['user']

    subprocess.check_call('robot claim -f --username ' + user + ' --email ' + user + ' -m "teleoperating the robot (claimed via Robot Web Server)"', shell=True)
    subprocess.check_call('robot start -f', shell=True)

    return jsonify({'status': 'success'})

@blueprint.route('/start', methods=['POST'])
def stop_robot():
    subprocess.check_call('robot stop -f', shell=True)
    
    return jsonify({'status': 'success'})

@blueprint.route('/check', methods=['GET'])
def check_robot_claim():
    if os.path.exists('/var/lib/robot/active_user.yaml'):
        fp = open(filename, "r")
        content = fp.read()
        fp.close()

        # TODO(csu): need to modify this, depending on how active_user.yaml is formatted
        return {'claim': content}
    else:
        return {'claim': None}