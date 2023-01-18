import sys, os
sys.path.append(sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src')))
# sys.path.insert(0, '/Users/pradeeppatil/Documents/Classes/Spring 2023/CSC 591 Automated Software Engineering/workspace/engr-csc591-021-spring2023/HW1/src/')
import run, globalVariables, examples

passed, failed = run.main(globalVariables.the, globalVariables.help, examples.examples_added)
print("Number of tests passing -> " + str(passed))
print("Number of tests failing -> " + str(failed))

failed = 1

if(failed != 0):
    sys.stderr.write("There are Failing Tests\n")
    sys.exit(1)
