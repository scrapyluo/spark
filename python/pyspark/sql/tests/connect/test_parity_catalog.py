#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest

from pyspark.sql.tests.test_catalog import CatalogTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase


class CatalogParityTests(CatalogTestsMixin, ReusedConnectTestCase):
    # TODO(SPARK-41612): Support Catalog.isCached
    # TODO(SPARK-41600): Support Catalog.cacheTable
    # TODO(SPARK-41623): Support Catalog.uncacheTable
    @unittest.skip("Fails in Spark Connect, should enable.")
    def test_table_cache(self):
        super().test_table_cache()

    # TODO(SPARK-41600): Support Catalog.cacheTable
    @unittest.skip("Fails in Spark Connect, should enable.")
    def test_refresh_table(self):
        super().test_refresh_table()


if __name__ == "__main__":
    import unittest
    from pyspark.sql.tests.connect.test_parity_catalog import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
