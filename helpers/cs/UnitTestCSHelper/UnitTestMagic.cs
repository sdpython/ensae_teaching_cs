using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using MagicIPython;

namespace UnitTestCSHelper
{
    [TestClass]
    public class UnitTestMagic
    {
        [TestMethod]
        public void TestFunction()
        {
            string code = @"public static double SquareX(double x) {return x*x ; }";
            var func = MagicCS.CreateFunction("SquareX", code, null);

            object result = MagicCS.RunFunction(func, new object[] { 2.0 });
            double x2 = (double)result;
            Assert.AreEqual(x2, 4.0);
        }
    }
}
