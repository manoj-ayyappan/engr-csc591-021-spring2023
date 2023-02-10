#Test File

import sys, os

#Getting relative file path to import needed packages
hw_number = sys.argv[1]
sys.path.append(os.path.join('src', hw_number))

import run, globalVars, examples

# Running tests from the main function in run/py
passed, failed = run.main(globalVars.the, globalVars.help, examples.examples_added)
print("✅ Number of tests passing -> " + str(passed))
print("❌ Number of tests failing -> " + str(failed))

#Exit with error if any test failed
if(failed != 0):
    sys.exit(1)
