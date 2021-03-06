import json
import requests


def get_help_string():
    return "Update clustersitter logging level"


def get_command():
    return "updateloglevel"


def get_parser(parser):
    parser.add_argument(dest="level",
                        help='New Debug Level '
                        '(10=debug,20=info,30=warning,40=error)',
                        type=int)

    return parser


def run_command(clustersitter_url, level):
    data = {'data': json.dumps({'level': level})}
    print "%s/update_idle_limit" % clustersitter_url
    resp = requests.post("%s/update_logging_level" % clustersitter_url,
                         data=data)
    print resp.content
