# Easylab 

0.1.0


Easylab is a simple, convenient tool to make the 'lab' easier. It captures the results as well as the arguments of a program, stores them in a database, and visualizes them with a simple, SQL-style query.


## Install

Install from source:

    python setup.py install



## Getting Started

1\. Install the codes in your program:
    
    # Python Code
    
    import easylab
    e = easylab.Easylab("NAME")
    e.log(var1=var1, var2=var2, var3=var3)


2\. Fire up the console:

    >python easylab_console.py
    =============================================
    easylab 0.1.0
    Type "help" for more information.
    easylab> 


3\. Run your program with a set of arguments automatically:

    easylab>autorun python your_program 1:100 1:100 1:100


4\. Check the results of the program:

    easylab>show NAME
    var1    |var2    |var3     |
    1       |2       |3        |
    6       |4       |7        |
    ...

5\. Check the results in a more specified way:

    easylab>select * from NAME where var3=3



6\. Plot the results:

    eastlab>compare var1, var3 from NAME where var2=3




## Dependencies


* sqlite3
* python-matplotlib


Install them on Ubuntu/Debian:


    >sudo apt-get install python-matplotlib
    >sudo apt-get install sqlite3
