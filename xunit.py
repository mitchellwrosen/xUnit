import sys

################################################################################
# A simple testing framework. Test classes should derive from xunit.Test, and
# should define:
#
#   - setUp(self)
#   - tearDown(self)
#   - any number of methods of the form: testXXX(self)
#
# The setUp and tearDown methods will be called before and after every test.
# A sample is shown below:
#
#   class FooTest(xunit.Test):
#      def setUp(self):
#         self.foo = True
#
#      def tearDown(self):
#         pass
#
#      def testOnePlusOne:
#         assert(2 == 1 + 1)
#
#      def testFooIsTrue:
#         assert(self.foo = True)
#         self.foo = False
#
#      def testFooIsStillTrue:
#         assert(self.foo = True)
#
# The class is run thusly:
#
#   FooTest().run()
################################################################################

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
