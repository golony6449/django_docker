import urllib


def get_instance_ip():
    response = urllib.urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
    instance_ip = response.read().decode('UTF-8')

    if response:
        response.close()

    return instance_ip