# This file is part of ts_config_mttcs.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
import unittest

from lsst.ts import salobj


class ConfigTestCase(salobj.BaseConfigTestCase, unittest.TestCase):
    def setUp(self):
        self.config_package_root = pathlib.Path(__file__).parents[1]

    def test_MTAOS(self):
        # Use env var ts_MTAOS to find the package because it uses packages
        # missing from the standard devlopment Docker image
        self.check_standard_config_files(sal_name="MTAOS",
                                         package_name="ts_MTAOS",
                                         config_package_root=self.config_package_root)

    def test_MTMount(self):
        self.check_standard_config_files(sal_name="MTMount",
                                         package_name="ts_MTMount",
                                         config_package_root=self.config_package_root)
