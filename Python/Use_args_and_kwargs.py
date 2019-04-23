
# coding: utf-8

# * *args to pass nonkeyworded list argument
# * **kwargs to pass keyworded list argument

# Following is the example of non keyworded list argument

# In[4]:

def test_var_nonkey_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_nonkey_args(3, "Avinash", "Barnwal")


# Following is the example of keyworded list argument

# In[9]:

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "FirstArgument: %s,SecondArgument: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, FirstName="Avinash", SecondName="Barnwal")


# Using *args and **kwargs when calling a function

# In[15]:

def test_var_nonkey_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("Avinash", "Barnwal")
test_var_nonkey_args_call(3, *args)


# In[16]:

def test_var_args_call(arg1,FirstName,SecondName):
    print "arg1:", arg1
    print "arg2:", FirstName
    print "arg3:", SecondName

kwargs = {"FirstName": "Avinash", "SecondName": "Barnwal"}
test_var_args_call(3, **kwargs)

