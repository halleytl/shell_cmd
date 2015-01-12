#!/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import time
import sys
import os
import signal

def shell_cmd(cmd, timeout=None, show=True, stdin_file=None):
    '''
    Will execute a command, read the output and return it back.
    
    @param cmd: command to execute
    @param timeout: process timeout in seconds
    @param show: Display output to the front
    @param stdin_file: Enter the interactive information content of the file
    @return: a tuple of three: first stdout, then stderr, then exit code
    @raise OSError: on missing command or if a timeout was reached
    '''

    ph_out = None # process output
    ph_err = None # stderr
    ph_ret = None # return code

    if show is True:
        if stdin_file is not None:
            _stdin = open(stdin_file)
        else:
            _stdin = sys.stdin
        _stdout = sys.stdout
        _stderr = sys.stderr
    else:
        if stdin_file is not None:
            _stdin = open(stdin_file)
        else:
            _stdin = subprocess.PIPE
        _stdout = _stderr = subprocess.PIPE

    p = subprocess.Popen(cmd, shell=True,
                         stdout=_stdout,
                         stdin=_stdin,
                         stderr=_stderr)

    # if timeout is not set wait for process to complete
    if not timeout:
        ph_ret = p.wait()
    else:
        fin_time = time.time() + timeout
        while p.poll() == None and fin_time > time.time():
            time.sleep(1)

        # if timeout reached, raise an exception
        if fin_time < time.time():
            # starting 2.6 subprocess has a kill() method which is preferable
            p.kill()
            #os.kill(p.pid, signal.SIGKILL)
            raise OSError("Process timeout has been reached")

        ph_ret = p.returncode


    ph_out, ph_err = p.communicate()

    return (ph_out, ph_err, ph_ret)


if __name__ == "__main__": 
    #print shell_cmd("pwd", show=True)
    shell_cmd("python test.py", show=True, stdin_file="b.txt")
    print shell_cmd("python test.py", show=False, stdin_file="b.txt")

