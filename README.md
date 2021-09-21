# Scripts, tools, themes, settings etc., that makes your worklife easier.

**Scripts**:
1. [nb_rsync](https://github.com/vulcun99/hydsdgr/blob/master/README.md#nb_rsync--rsync-the-latest-build-of-platform-of-choice-to-local-machine)
2. [download_schrodinger_hosts.py](https://github.com/vulcun99/hydsdgr/blob/master/README.md#download_schrodinger_hostspy-download-schrodingerhosts-file-for-the-releasebuildbuildtype-of-choice)
3. [vpn](https://github.com/vulcun99/hydsdgr/blob/master/README.md#vpn--disconnect-from-andor-connect-to-a-vpn-service-on-mac-from-terminal)
4. [appgate](https://github.com/vulcun99/hydsdgr/blob/master/README.md#appgate--activate-or-quit-appgate-on-mac)

### *nb_rsync*:  Rsync the latest build of platform of choice to local machine
Pre-requisites:
1. One of SDGR VPN service should be enabled (*vpn* or *appgate* scripts can be used to do this)
2. Executable permissions to the script (`chmod +x nb_rsync`)

**Good to have**: Passwordless SSH setup between the local and remote hosts (Otherwise, user has to manually type password whenever needed)

Usage: Use "-h" to know more details
```bash
nb_rsync -r 2021-3 -d /home/myhome -v -H my-remote-host.domain.com
```
### *download_schrodinger_hosts.py*: Download schrodinger.hosts file for the release/build/buildtype of choice
Pre-requisites:
1. Needs python3 version
2. Install `requests` module (*pip3 install requests*)

Usage:
```python
download_schrodinger_hosts.py --release 2021-3 --buildtype OB --build_id build-123 installer_location/schrodinger.hosts
```


### *vpn*:  Disconnect from and/or Connect to a VPN service on Mac from terminal
Pre-requisites:
1. Executable permissions to the script

Usage:
```bash
# To list available services
vpn -l

# To disconnect from a service titles "MY CON" and connect to "NYC-VPN"
vpn -d "MY CON" -c NYC-VPN
```


### *appgate*:  Activate or Quit Appgate on Mac
Pre-requisites:
1. Executable permissions to the script

```bash
Usage:
# To activate AppGate app
appgate -c

# To quite Appate app
appgate -q
```
