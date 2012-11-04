import sys

class Test:
   def __init__(self):
      self.cases = []
      for member in dir(self):
         if member.startswith('test'):
            self.cases.append(member)

   def setUp(self):
      pass

   def tearDown(self):
      pass

   def run(self):
      failures = []
      for test in self.cases:
         self.setUp()

         output = '%s -- ' % test
         try:
            getattr(self, test)()
            output += 'PASSED'
         except Exception, e:
            output += 'FAILED: %s' % e
            failures.append(test)

         self.tearDown()
         print output

      print '%d run, %d failed: %s' % (len(self.cases), len(failures), failures)
