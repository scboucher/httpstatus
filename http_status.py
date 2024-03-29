#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json
import os
app = Flask(__name__)

SHAME_GIF = 'https://media.tenor.com/images/f6f91f0f5bd4d733e1fb9dfee1c37580/tenor.gif'
httpstatus = {
    '100': 'Continue',
    '101': 'Switching Protocols',
    '102': 'Processing',
    '200': 'OK',
    '201': 'Created',
    '202': 'Accepted',
    '203': 'Non-Authoritative Information',
    '204': 'No Content',
    '205': 'Reset Content',
    '206': 'Partial Content',
    '207': 'Multi-Status',
    '208': 'Already Reported',
    '226': 'IM Used',
    '300': 'Multiple Choices',
    '301': 'Moved Permanently',
    '302': 'Found',
    '303': 'See Other',
    '304': 'Not Modified',
    '305': 'Use Proxy',
    '306': 'Switch Proxy',
    '307': 'Temporary Redirect',
    '308': 'Permanent Redirect',
    '400': 'Bad Request',
    '401': 'Unauthorized',
    '402': 'Payment Required',
    '403': 'Forbidden',
    '404': 'Not Found',
    '405': 'Method Not Allowed',
    '406': 'Not Acceptable',
    '407': 'Proxy Authentication Required',
    '408': 'Request Timeout',
    '409': 'Conflict',
    '410': 'Gone',
    '411': 'Length Required',
    '412': 'Precondition Failed',
    '413': 'Payload Too Large',
    '414': 'URI Too Long',
    '415': 'Unsupported Media Type',
    '416': 'Range Not Satisfiable',
    '417': 'Expectation Failed',
    '418': 'I\'m a teapot',
    '421': 'Misdirected Request',
    '422': 'Unprocessable Entity',
    '423': 'Locked',
    '424': 'Failed Dependency',
    '426': 'Upgrade Required',
    '428': 'Precondition Required',
    '429': 'Too Many Requests',
    '431': 'Request Header Fields Too Large',
    '451': 'Unavailable For Legal Reasons',
    '500': 'Internal Server Error',
    '501': 'Not Implemented',
    '502': 'Bad Gateway',
    '503': 'Service Unavailable',
    '504': 'Gateway Timeout',
    '505': 'HTTP Version Not Supported',
    '506': 'Variant Also Negotiates',
    '507': 'Insufficient Storage',
    '508': 'Loop Detected',
    '510': 'Not Extended',
    '511': 'Network Authentication Required',
    '103': '[Unofficial] Checkpoint',
    '420': '[Unofficial] Enhance Your Calm (Twitter). Method Failure (Spring Framework).',
    '419': '[Unofficial] I\'m a fox (Smoothwall/Foxwall)',
    '450': '[Unofficial] Blocked by Windows Parental Controls (Microsoft)',
    '498': '[Unofficial] Invalid Token (Esri)',
    '499': '[Unofficial] Token Required (Esri), Request has been forbidden by antivirus (wget), Client Closed Request (nginx)',
    '509': '[Unofficial] Bandwidth Limit Exceeded (Apache Web Server/cPanel)',
    '530': '[Unofficial] Site is frozen (Pantheon)',
    '440': '[Unofficial] Login Timeout (Internet Information Services)',
    '449': '[Unofficial] Retry With (Internet Information Services)',
    '444': '[Unofficial] No Response (nginx)',
    '495': '[Unofficial] SSL Certificate Error (nginx)',
    '496': '[Unofficial] SSL Certificate Required (nginx)',
    '497': '[Unofficial] HTTP Request Sent to HTTPS Port (nginx)',
    '520': '[Unofficial] Unknown Error (CloudFlare)',
    '521': '[Unofficial] Web Server Is Down (CloudFlare)',
    '522': '[Unofficial] Connection Timed Out (CloudFlare)',
    '523': '[Unofficial] Origin Is Unreachable (CloudFlare)',
    '524': '[Unofficial] A Timeout Occurred (CloudFlare)',
    '525': '[Unofficial] SSL Handshake Failed (CloudFlare)',
    '526': '[Unofficial] Invalid SSL Certificate (CloudFlare)'
}


@app.route("/", methods=['POST'])
def status():
    data = request.form
    if data['text'] == "":
        response = jsonify(response_type='ephemeral',
                           text=':catshake: How to use `/http` command:',
                           attachments=[{
                                'text': "Type a status code _e.g._ /http 400"
                           }])
    elif not data['text'] in httpstatus.keys():
        response = jsonify(response_type='ephemeral',
                           text=data['text'] + ': Invalid Status Code',
                           attachments=[{
                               'image_url': SHAME_GIF,
                               'pretext': "Shame!"
                           }])
    else:
        response = jsonify(response_type='in_channel',  attachments=[{
            'image_url': 'https://http.cat/' + data['text'],
            'pretext':  data['text'] + '\n' + httpstatus[data['text']]
        }])
    return response


if __name__ == "__main__":
    if os.environ['PORT']:
        app.run(host='0.0.0.0', port=os.environ['PORT'])
    else:
        app.run(host='0.0.0.0', port=5000)
