import socket

def checkUrl(path_link):
    http_status='HTTP/1.1 200 OK\n\n'

    try: 
        with open(path_link[1:]+'.html') as f:
            var2=f.read()
        return bytes(http_status+var2,'utf-8')
    except (FileNotFoundError):
        return bytes('HTTP/1.1 404 NotFound','utf-8')


'''    if var1=='/hello':
        with open('hello.html') as file:
            var5=file.read()
        return bytes(http_status+var5,'utf-8')
    
    elif var1=='/contacts':
        import random
        b=str()
        for x in range(20):
            a='+996707'+str(random.randint(100000,999999))
            b+=a+'\n'
        return bytes(http_status+b,'utf-8')
    
    elif var1=='/images':
        with open('images.html')as file:
            var2=file.read()
        return bytes('HTTP/1.1 200 OK\n\n'+var2,'utf-8')
    
    elif var1=='/about':
        with open('about.html')as file:
            var4=file.read()
        return bytes(http_status+var4,'utf-8')
    
    elif var1=='/video':
        with open('video.html')as file:
            var6=file.read()
        return bytes(http_status+var6,'utf-8')

    elif var1=='/profile':
        with open('profile.html')as file:
            var7=file.read()
        return bytes(http_status+var7,'utf-8')

    else:
        return bytes('HTTP/1.1 404 NotFound','utf-8')
'''    

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print(f'Serving HTTP on port {PORT} ...')
conca=1
while True:
    if conca%2==0:
        client_connection, client_address = listen_socket.accept()
        request_data = client_connection.recv(2048)
        # print(request_data.decode('utf-8'))
        a=request_data.decode()
        index_of_http=a.find('/')
        afterHTTP=a[index_of_http:]
        index_of_ending=(str(afterHTTP).find('HTTP'))-1
        complete=afterHTTP[:index_of_ending]
        client_connection.sendall(checkUrl(complete))
        client_connection.close()
    conca+=1



