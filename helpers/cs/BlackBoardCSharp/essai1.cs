using System;
using System.Collections.Generic;
using System.Linq;


namespace BlackBoardCSharp
{
    public static class Try1
    {
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
    }
}
