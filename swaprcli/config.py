import os

PRODUCTION_DOCKER_IMAGES = {
    'backend': {
        'context': 'gatech-swapr-server-node',
        'dockerfile': 'gatech-swapr-server-node/Dockerfile'
    },
    'www': {
        'context': 'swapr-react-client',
        'dockerfile': 'swapr-react-client/Dockerfile.build'
    }
}

PRODUCTION_STACK_NAME = 'swapr'

PRODUCTION_DOCKER_ENV = {
    'DOCKER_HOST': 'swapr.vip.gatech.edu:2376',
    'DOCKER_TLS_VERIFY': '1',
    'DOCKER_CERT_PATHS': '{}/docker-certs'.format(os.getcwd()),
}