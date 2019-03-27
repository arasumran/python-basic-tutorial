import cplex
import os

import cplex
import sys

from cplex.exceptions import CplexSolverError


def sample1(filename):
    c = cplex.Cplex(filename)
    try:
        c.solve()
    except CplexSolverError as a:
        print ("Exception raised during solve")
        return
# solution.get_status() returns an integer code
    status = c.solution.get_status()
    print ("Solution status = " , status, ":")
    print (c.solution.status[status])
    print ("Objective value = " , c.solution.get_objective_value())

sample1("/root/opl/fileload/f.mod")