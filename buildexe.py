import subprocess
import urlparse
import os

ovpn_source = "http://swupdate.openvpn.org/community/releases/"
ovpn_version = "2.3.6-I601"
tuntap_version = "9.21.1"


def create_executable():
    print "Creating executables..."
    subprocess.call("python setup.py py2exe -q")


def get_platform():
    platforms = {'32bit': "i686", '64bit': "x86_64"}
    import platform
    return platforms[platform.architecture()[0]]


def download_third_parties():
    print "Downloading third-parties..."
    import urllib
    downloader = urllib.URLopener()

    # Download openvpn from source
    ovpn_filename = 'openvpn-install-{0}-{1}.exe'.format(ovpn_version, get_platform())
    ovpn_url = urlparse.urljoin(ovpn_source, ovpn_filename)
    print 'Downloading', ovpn_url
    downloader.retrieve(ovpn_url, ovpn_filename)

    # Download tuntap driver from source
    tuntap_filename = 'tap-windows-{0}.exe'.format(tuntap_version)
    tuntap_url = urlparse.urljoin(ovpn_source, tuntap_filename)
    print 'Downloading', tuntap_url
    downloader.retrieve(tuntap_url, tuntap_filename)


def initialize():
    print "Initializing..."
    third_party_path = os.path.join(os.getcwd(), "third-party")
    dist_path = os.path.join(os.getcwd(), "dist")

    if not os.path.exists(third_party_path):
        os.makedirs(third_party_path)

    if not os.path.exists(dist_path):
        os.makedirs(dist_path)


if __name__ == "__main__":
    initialize()
    create_executable()
    download_third_parties()
