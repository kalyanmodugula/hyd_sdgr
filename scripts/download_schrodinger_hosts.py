#!/usr/bin/python3
"""
Download schrodinger.hosts file.

Uses the USER variable and localhost name of where we are running to determine
adjustments.

"""
import argparse
import getpass

import requests

HOSTS_URL = 'http://build-download.schrodinger.com/generatehosts/generate_hosts_file'


def parse_arguments():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("hostfile", help="schrodinger.hosts filename")
    parser.add_argument("--release",
                        required=True,
                        help="Schrodinger release (e.g. 2016-1)")
    parser.add_argument("--buildtype",
                        required=True,
                        help="Build type (NB or OB)",
                        choices=('NB', 'OB'))
    parser.add_argument("--build_id", required=True, help="Build ID")
    parser.add_argument("--user", help="Username to add in schrodinger.hosts")
    parser.add_argument("--tmpdir",
                        help="tmpdir for localhost. Usually specified as /scr")

    return parser.parse_args()


def get_hosts_file_text(release, buildtype, build_id, tmpdir=None, user=None):
    """
    Download the hosts file for the requested release/buildtype/build_id
    """
    data = dict(release=release, build_type=buildtype, build_id=build_id)

    if user:
        data['remote_user'] = user

    if getpass.getuser() == 'buildbot':
        data['remote_user'] = 'buildbot'

    if tmpdir:
        data['tmpdir'] = tmpdir

    response = requests.post(HOSTS_URL, data)
    response.raise_for_status()

    return response.text


def main():

    args = parse_arguments()
    hosts_text = get_hosts_file_text(args.release, args.buildtype,
                                     args.build_id, args.tmpdir, args.user)

    with open(args.hostfile, 'w') as fh:
        fh.write(hosts_text)


if __name__ == "__main__":
    main()
