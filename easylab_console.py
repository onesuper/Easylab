#!/usr/bin/python
# Filename: easylab.py


import cmd
import sys
import subprocess
import easylab_db as db
import easylab_autorun as autorun

class Shell(cmd.Cmd):
    intro = '''=============================================
easylab 0.1.0
Type "help" for more information.'''
    
    doc_header = "Type <command> to see the instruction."
    undoc_header = "other commands"


    prompt = "easylab> "
    ruler = "="

    def emptyline(self):
        '''if the input is an empty line'''
        return
    

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
        

    def do_show(self, tablename):
        if tablename != "":
            db.showTable(conn, tablename)
        else:
            print "the command looks like: show [tablename]"
    
    def do_drop(self, tablename):
        if tablename != "":
            db.dropTable(conn, tablename)
        else:
            print "the command looks like: drop [tablename]"

    def do_exit(self, path):
        conn.close()
        sys.exit()

    def do_select(self, sql):
        sql = "select " + sql
        db.query(conn, sql)
        

    def do_help(self, path):
        print '''Help
-------------------------------------------------------
show [tablename]:
drop [tablename]:
run [program] [arv0] [argv1] ...:
autorun [program] [range of argv0] ...:
exit: goodbye my lover
sql: [sql syntax]: 
'''

if __name__ == "__main__":
    
    conn = db.createConn()
    sh = Shell()
    sh.cmdloop()
    conn.close()
