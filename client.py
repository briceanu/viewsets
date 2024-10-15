
import requests
import sys




def list1():
    url = 'http://127.0.0.1:8000/blog/list'
    res = requests.get(url=url)
    print(f"{res.status_code}\n{res.url}\n{res.text}")



def create():
    url = 'http://127.0.0.1:8000/blog/create/'

    data = {'content':'last last alst costica d ','private':True,'hacking':'sql injection'}

    res = requests.post(url=url,data=data)
    print(f"{res.status_code}\n{res.url}\n{res.text}")



def retrieve():
    url = 'http://127.0.0.1:8000/blog/6a006242-140b-4374-b70c-1799b0ef8741/'
    res = requests.get(url=url)
    print(f"{res.status_code}\n{res.url}\n{res.text}")


def update():
    url = 'http://127.0.0.1:8000/blog/update/6a006242-140b-4374-b70c-1799b0ef8741'

    data = {'content':'this is updatate tupadat','private':True,'hacking':'sql injection'}

    res = requests.put(url=url,data=data)
    print(f"{res.status_code}\n{res.url}\n{res.text}")


def partial():
    url = 'http://127.0.0.1:8000/blog/partial-update/6a006242-140b-4374-b70c-1799b0ef8741/'

    data = {'content':' gigi gigi gigig  ','private':False,'hacking':'remove code exctuint'}

    res = requests.patch(url=url,data=data)
    print(f"{res.status_code}\n{res.url}\n{res.text}")


def destroy():
    url = 'http://127.0.0.1:8000/blog/remove/6a006242-140b-4374-b70c-1799b0ef8741/'

   
    res = requests.post(url=url )
    print(f"{res.status_code}\n{res.url}\n{res.text}")


def criteria():
    url = f'http://127.0.0.1:8000/blog/get_blogs_by_criteria/?match={sys.argv[2]}'
    res = requests.get(url=url )
    print(f"{res.status_code}\n{res.url}\n{res.text}")





if __name__ == "__main__":
    if sys.argv[1] == 'list':
        list1()
    elif sys.argv[1] =='create':
        create()
    elif sys.argv[1] =='retrive':
        retrieve()
    elif sys.argv[1] =='update':
        update()
    elif sys.argv[1] =='partial':
        partial()
    elif sys.argv[1] =='destroy':
        destroy()
    elif sys.argv[1] =='criteria':
        criteria()
        
    else:
        exit(1)