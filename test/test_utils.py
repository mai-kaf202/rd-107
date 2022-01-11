import unittest


class TestTest(unittest.TestCase):
    def test_existence(self):
        self.assertTrue(True)

    def test_docs(self):
        """Запускает все тесты документации в подмодулях."""
        import doctest
        import rd107
        import pkgutil
        for importer, name, ispkg in pkgutil.walk_packages(rd107.__path__, rd107.__name__ + '.'):
            # tests.addTests(doctest.DocTestSuite(name))
            suite = doctest.DocTestSuite(name)
            result = unittest.TextTestRunner().run(suite)
            # print(name, suite, result)
            # TODO: use [extended API](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner)
            self.assertTrue(result.wasSuccessful())
