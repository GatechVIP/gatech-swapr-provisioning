from subprocess import call

from cement.core.controller import CementBaseController, expose

from .config import PRODUCTION_DOCKER_IMAGES


class SwaprCLIImagesController(CementBaseController):
    class Meta:
        label = 'images'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Utilities for building and pushing production-ready Docker images.'

    @expose(help="Builds production Docker images for all services.")
    def build(self):
        self.app.log.info("Building {} images: {}".format(
            len(PRODUCTION_DOCKER_IMAGES), ', '.join(PRODUCTION_DOCKER_IMAGES.keys())
        ))

        errors = []
        success = []

        for name, options in PRODUCTION_DOCKER_IMAGES.items():
            self.app.log.info("Building image '{}'...".format(name))

            retcode = call([
                'docker', 'build',
                '-f', options['dockerfile'],
                '-t', 'gatechswapr/{}'.format(name),
                options['context']
            ])

            if retcode:
                self.app.log.error("Container failed to build")
                errors.append(name)
            else:
                success.append(name)

        if errors:
            self.app.log.error("{} images failed to build: {}".format(
                len(errors), ', '.join(errors)))

        if success:
            self.app.log.info("Built {} images successfully: {}".format(
                len(success), ', '.join(success)))

    @expose(help="Pushes all production Docker images to Docker Hub.")
    def push(self):
        self.app.log.info("Pushing {} images: {}".format(
            len(PRODUCTION_DOCKER_IMAGES), ', '.join(PRODUCTION_DOCKER_IMAGES.keys())
        ))

        for name, options in PRODUCTION_DOCKER_IMAGES.items():
            self.app.log.info("Pushing image '{}'...".format(name))

            retcode = call([
                'docker', 'push', 'gatechswapr/{}'.format(name)
            ])

