using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.CodeDom.Compiler;
using Microsoft.CSharp;
using System.Reflection;

namespace MagicIPython
{
    public static class MagicCS
    {
        private const string embedCode = @"
                    {4};

                    namespace MagicCSIPython
                    {0}                
                        public static class MagicCSFunctions_{2}
                        {0}  
                            {3}
                        {1}
                    {1}
                    ";

        public static MethodInfo CreateFunction(string functionName, string code, string[] dependencies, string[] usings)
        {
            CSharpCodeProvider provider = new CSharpCodeProvider();
            CompilerParameters parameters = new CompilerParameters();

            if (usings == null || usings.Length == 0)
            {
                usings = new string[] { "System", "System.Text", "System.Collections.Generic", "System.Linq" };
            }

            if (dependencies == null || dependencies.Length == 0 )
            {
                dependencies = new string[] { "System.dll", "System.Core.dll" };
            }
            else
            {
                var deps = dependencies.ToList();
                if (!deps.Contains("System.dll")) deps.Add("System.dll");
                if (!deps.Contains("System.Core.dll")) deps.Add("System.Core.dll");
                dependencies = deps.ToArray() ;
            }

            if (dependencies != null)
            {
                foreach (var d in dependencies)
                    parameters.ReferencedAssemblies.Add(d);
            }

            parameters.GenerateInMemory = true;
            parameters.GenerateExecutable = false;

            string suse = string.Join(";\n", 
                                      usings.Select (c => string.Format("using {0}", c)).ToArray()) ;

            code = string.Format(embedCode, "{", "}", functionName, code, suse);

            CompilerResults results = provider.CompileAssemblyFromSource(parameters, code);
            if (results.Errors.HasErrors)
            {
                StringBuilder sb = new StringBuilder();
                foreach (CompilerError error in results.Errors)
                {
                    sb.AppendLine(String.Format("Error ({0}): {1}", error.ErrorNumber, error.ErrorText));
                }
                throw new InvalidOperationException(sb.ToString());
            }
            Type binaryFunction = results.CompiledAssembly.GetType(string.Format("MagicCSIPython.MagicCSFunctions_{0}", functionName));
            return binaryFunction.GetMethod(functionName);

            /*
             var betterFunction = (Func<double, double, double>)Delegate.CreateDelegate(
                                                        typeof(Func<double, double, double>), function);
            double result = betterFunction(2, 3);
            Console.WriteLine(result);
             * * 
             */
        }

        public static object RunFunction(MethodInfo function, object[] parameters)
        {
            return function.Invoke(null, parameters);
        }

        public static List<long> NewListIntLong()
        {
            return new List<long>();
        }
    }
}
