using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using MagicJupyter;
using BlackBoardCSharp;

namespace UnitTestCSHelper
{
    [TestClass]
    public class UnitTestMagic
    {
        [TestMethod]
        public void TestFunction()
        {
            string code = @"public static double Square_X(double x) {return x*x ; }";
            var func = MagicCS.CreateFunction("Square_X", code, null, null);

            object result = MagicCS.RunFunction(func, new object[] { 2.0 });
            double x2 = (double)result;
            Assert.AreEqual(x2, 4.0);
        }

        [TestMethod]
        public void TestFunction2()
        {
            string code = @"
                    public static int[] cs_qsort(int[] li)
                    {
                        if (li.Length == 0)
                        {
                            return null;
                        }
                        else
                        {
                            var pivot = li[0];
                            var lesser = cs_qsort(li.Skip(1).Where(x => x < pivot).ToArray());
                            var greater = cs_qsort(li.Skip(1).Where(x => x >= pivot).ToArray());
                            int[] res = new int[li.Length];

                            if (lesser != null && lesser.Length > 0) Array.Copy(lesser, 0, res, 0, lesser.Length);
                            int nb = lesser == null ? 0 : lesser.Length;
                            res[nb] = pivot;
                            if (greater != null && greater.Length > 0) Array.Copy(greater, 0, res, nb + 1, greater.Length);

                            return res;
                        }
                    }    
                    ";
            var ari = new int[] { 1,2,3,1};
            var result2 = Try1.cs_qsort(ari);

            var func = MagicCS.CreateFunction("cs_qsort", code, null, null);
            var aro = ari as object;
            object result = MagicCS.RunFunction(func, new object[] { aro });
            var resi = result as int[];
            Assert.AreEqual(result2.Length, resi.Length);
            for (int i = 0; i < result2.Length; ++i)
            {
                Assert.AreEqual(result2[i], resi[i]);
            }
        }
    }
}
