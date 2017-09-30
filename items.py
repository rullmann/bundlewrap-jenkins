files = {
    '/etc/yum.repos.d/jenkins.repo': {
        'source': 'jenkins.repo',
        'mode': '0644',
        'triggers': [
            'action:dnf_makecache',
        ],
    },
    '/etc/sysconfig/jenkins': {
        'source': 'sysconfig',
        'content_type': 'mako',
        'mode': '0600',
        'needs': [
            'pkg_dnf:jenkins',
        ],
        'triggers': [
            'svc_systemd:jenkins:restart',
        ],
    },
}

actions = {
    'jenkins_import_gpg_key': {
        'command': 'rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key',
        'unless': 'rpm -ql gpg-pubkey-d50582e6-4a3feef6',
    },
}

pkg_dnf = {
    'jenkins': {
        'needs': [
            'file:/etc/yum.repos.d/jenkins.repo',
            'action:jenkins_import_gpg_key'
        ],
    },
}

svc_systemd = {
    'jenkins': {
        'needs': [
            'pkg_dnf:jenkins',
        ],
    },
}

if node.has_bundle('monit'):
    files['/etc/monit.d/jenkins'] = {
        'source': 'monit',
        'mode': '0640',
        'content_type': 'mako',
        'triggers': [
            'svc_systemd:monit:restart',
        ],
    }
