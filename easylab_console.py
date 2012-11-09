#!/usr/bin/python
# Filename: easylab.py


import cmd
import sys
import os
import subprocess
import easylab_db as db
import easylab_autorun as autorun
import easylab_plot as plot



class Shell(cmd.Cmd):
    intro = '''=============================================
easylab 0.1.0
Type "help" for more information.'''
    
    doc_header = "Type <command> to see the instruction."
    undoc_header = "other commands"


    prompt = "easylab> "
    ruler = "="

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.database = db.EasylabDB()
        self.plot = plot.EasylabPlot()
   
    def emptyline(self):
        '''if the input is an empty line'''
        return
    

    def do_ls(self, path):
        result = self.database.showTables()
        for r in result:
            print r[0] + '\t',
        print "\n",


    def do_run(self, argvstr):
        argv = argvstr.split()
        try:
            subprocess.call(argv)
        except OSError, e:
            print e


    def do_autorun(self, argvstr):
        argv = argvstr.split()
        if len(argv) >= 2:
            many_argvs = autorun.argvTransform(argv)
            # run these argvs
            try:
                for argv in many_argvs:
                    subprocess.call(argv)
            except OSError, e:
                print e
        else:
            print "the command looks like: autorun [program] [argv1] [argv2]..."
        

    def do_show(self, table):
        if table != "":
            self.database.showTable(table)
        else:
            print "the command looks like: show [tablename]"
    

    def do_drop(self, table):
        if table != "":
            self.database.dropTable(table)
        else:
            print "the command looks like: drop [tablename]"


    def do_exit(self, path):
        sys.exit(0)
    

    def do_select(self, sql):
        sql = "select " + sql
        result = self.database.query(sql)
        db.printfResult(result)


    def do_plot(self, sql):
        fromIndex = sql.find("from") # -1 = not found

        #get the column names
        argstr = sql[0:fromIndex].strip()
        arglist = argstr.split(",")
        if len(arglist) != 2:
            print "plot command only accept two columns"
            return
        namelist = [arg.strip() for arg in arglist]

        #get the table name
        table = sql[fromIndex:].strip().replace("from", "")

        # query the result
        sql = "select " + sql
        result = self.database.query(sql)
        
        # plot it!
        self.plot.plot(result, namelist, table)


    def do_plots(self, sql):
        fromIndex = sql.find("from") # -1 = not found
        argstr = sql[0:fromIndex].strip()
        arglist = argstr.split(",")
        if len(arglist) <= 2:
            print "plots command accept more than two columns"
            return
        """
        argstr looks like:
        fib2.N, fib1.time ,fib2.time fib3.time
        so, N is the xlabel
            time is the ylabel
            fib1, fib2, fib3 are the line labels
        """
        dotIndex = arglist[0].find(".")
        xlabel = arglist[0][dotIndex+1:].strip()
        dotIndex = arglist[1].find(".")
        ylabel = arglist[1][dotIndex+1:].strip()
        namelist = []
        for i in range(1, len(arglist)):
            dotIndex = arglist[i].find(".")
            name = arglist[i][0: dotIndex]
            namelist.append(name.strip())
    
        # query the result
        sql = "select " + sql
        result = self.database.query(sql)

        # pass the result to plot
        self.plot.plots(result, xlabel, ylabel, namelist)


    def do_compare(self, sql):
        fromIndex = sql.find("from")  # -1 = not found
        argstr = sql[0:fromIndex].strip()
        if argstr == "*":
            print "compare does not support * selector"
            return
        arglist = argstr.split(",")
        namelist = [arg.strip() for arg in arglist]
            
        # query the result
        sql = "select " + sql
        result = self.database.query(sql)
        
        # pass the result and arglist to plot
        self.plot.bar(result, namelist)


    def do_help(self, path):
        print '''Help
-------------------------------------------------------
ls:      show all the tables in the database
         ls

show:    display a table quickly
         show [tablename]
        
drop:    drop a table quickly         
         drop [tablename]
         
run:     run a program quickly 
         run [program_path] [arv0] [argv1] ...

autorun: run a program looply
         autorun [program] [range of argv0] ...


select:  query a table
         select * from [tablename] ...

compare: plot to compare data
         compare a,b from [tablename] where c=1:  

exit:    Goodbye My Lover
         exit
-------------------------------------------------------
'''

if __name__ == "__main__":
    


    sh = Shell()
    sh.cmdloop()
    
    
