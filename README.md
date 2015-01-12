平台:linux 
python :2.6+

linux下的命令行支持回答模式

Will execute a command, read the output and return it back.

param cmd: command to execute

param timeout: process timeout in seconds

param show: Display output to the front

param stdin_file: Enter the interactive information content of the file

return: a tuple of three: first stdout, then stderr, then exit code

raise OSError: on missing command or if a timeout was reached

example:

python shellCmd.py

