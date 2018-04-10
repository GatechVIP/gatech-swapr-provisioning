from subprocess import call

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

from .images import SwaprCLIImagesController


class SwaprCLIBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Tools for developing and managing SWAPR.'

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()


class SwaprCLI(CementApp):
    class Meta:
        label = 'swaprcli'
        base_controller = 'base'
        handlers = [SwaprCLIBaseController, SwaprCLIImagesController]


if __name__ == '__main__':
    with SwaprCLI() as app:
        app.run()
