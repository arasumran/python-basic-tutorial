import paramiko
ps = ["pass2", "pass1", "pass3"]
def start_connection():
    for ip in range(194,197):
        for pswd in ps:
            u_name = 'root'
#            pswd = 'pas21'
            port = 22
            r_ip = '%d' % (ip)
            myconn = paramiko.SSHClient()
            myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session = myconn.connect(r_ip, username =u_name, password=pswd, port=port)

            if session is None:
                remote_cmd = 'hostname'
                (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
                print(stdout.read())
                myconn.close()
            else :
                pass
if __name__ == '__main__':
    start_connection()