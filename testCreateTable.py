import unittest

from createTable import readHQL, athenaQuery

class TestSum(unittest.TestCase):
    def ReadHQL(self):
        """
            Read the Content of HQL File
        """
        fileLocation = ""
        result = readHQL(fileLocation)
        self.assertEqual(result, "Select * from .....")

    def AthenaQuery(self):
        """
            Execute Athena Query
        """
        fileLocation = ''
        database = ''
        outputLocation = ''
        result = athenaQuery(fileLocation, database, outputLocation)
        self.assertEqual(result, "13313242412121324")

if __name__ == "__main__":
    unittest.main()