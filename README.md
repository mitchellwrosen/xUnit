xUnit
=====

A simple testing framework. Test classes should derive from xunit.Test, and
should define:

   - setUp(self)
   - tearDown(self)
   - any number of methods of the form: testXXX(self)

The setUp and tearDown methods will be called before and after every test.
A sample is shown below:

   class FooTest(xunit.Test):
      def setUp(self):
         self.foo = True

      def tearDown(self):
         pass

      def testOnePlusOne:
         assert(2 == 1 + 1)

      def testFooIsTrue:
         assert(self.foo = True)
         self.foo = False

      def testFooIsStillTrue:
          assert(self.foo = True)

The class is run thusly:

   FooTest().run()
