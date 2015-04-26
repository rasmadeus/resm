Resm
===== 
Resm is a simple resource manager that provides resources on demand. 
How install
---------------
1. install python (see: python.org)
2. run command: python setup.py install

How run resm
--------------------
In pythom shell:
>>>  from resm import view
>>>  view.run(number_of_res=10, port=5000)

Functions of resm
-------------------------
1. /list - get full list of resources.
2. /list/user_name - get list of resources allocated by user_name
3. /deallocate/res_name - deallocate resource. The resource name is in r1 ... r{number_of_res}
4. /reset - deallocate all resources

How stop
-------------
CTRL+C

How test
------------
In pythom shell:
>>> from resm import test
>>> test.run()
