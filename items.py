files = {
    '/etc/yum.repos.d/jenkins.repo': {
        'source': "jenkins.repo",
        'owner': "root",
        'mode': "0644",
        'triggers': [
            "action:yum_makecache",
        ],
    },
    '/etc/sysconfig/jenkins': {
        'source': "sysconfig",
        'content_type': "mako",
        'owner': "root",
        'mode': "0600",
        'needs': [
            "pkg_dnf:jenkins",
        ],
        'triggers': [
            "svc_systemd:jenkins:restart",
        ],
    },
}

actions = {
    'jenkins_import_gpg_key': {
        'command': "rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key",
        'unless': "rpm -ql gpg-pubkey-d50582e6-4a3feef6",
    },
}

pkg_dnf = {
    "jenkins": {
        'needs': [
            "file:/etc/yum.repos.d/jenkins.repo",
            "action:jenkins_import_gpg_key"
        ],
    },
}

svc_systemd = {
    'jenkins': {
        'enabled': True,
        'needs': [
            "pkg_dnf:jenkins",
        ],
    },
}
