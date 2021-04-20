from multiprocessing import Process, Pipe
import time

def f(conn):
    conn.send([42, None, 'hello'])
    print (conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    time.sleep(1)
    parent_conn.send("algo")
    p.join()
