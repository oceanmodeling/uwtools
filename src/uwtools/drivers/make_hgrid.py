"""
A driver for make_hgrid.
"""

from pathlib import Path

from iotaa import tasks

from uwtools.drivers.driver import DriverTimeInvariant
from uwtools.drivers.support import set_driver_docstring
from uwtools.strings import STR


class MakeHgrid(DriverTimeInvariant):
    """
    A driver for make_hgrid.
    """

    # Workflow tasks

    @tasks
    def provisioned_rundir(self):
        """
        Run directory provisioned with all required content.
        """
        yield self.taskname("provisioned run directory")
        yield self.runscript()

    # Public helper methods

    @classmethod
    def driver_name(cls) -> str:
        """
        The name of this driver.
        """
        return STR.makehgrid

    @property
    def output(self) -> dict[str, Path]:
        """
        Returns a description of the file(s) created when this component runs.
        """
        grid_name = self.config["config"].get("grid_name", "horizontal_grid")
        return {"path": (self.rundir / grid_name).with_suffix(".nc")}

    # Private helper methods

    @property
    def _runcmd(self):
        """
        The full command-line component invocation.
        """
        executable = self.config[STR.execution][STR.executable]
        config = self.config["config"]
        flags = []
        for k, v in config.items():
            if isinstance(v, bool):
                flags.append("--%s" % k)
            elif isinstance(v, list):
                flags.append("--%s %s" % (k, ",".join(map(str, v))))
            else:
                flags.append("--%s %s" % (k, v))
        return f"{executable} " + " ".join(flags)


set_driver_docstring(MakeHgrid)
