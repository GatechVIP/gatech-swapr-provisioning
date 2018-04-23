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
