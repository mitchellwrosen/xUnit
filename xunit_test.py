import xunit

class TestClassTest(xunit.Test):
   def setUp(self):
      self.foo = True

   def tearDown(self):
      self.foo = False

   def testSetUp(self):
      assert(self.foo is True)

TestClassTest().run()
