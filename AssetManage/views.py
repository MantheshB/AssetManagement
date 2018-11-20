from django.shortcuts import render,resolve_url, reverse
from django.db import connection
import pymysql

# Create your views here.


cur = connection.cursor()
cur.execute("SELECT * FROM asset_manager.inventory")
users=cur.fetchall()
mylist=[]
for row in users:
    mylist.append(row)
    #print(row)
    #print(mylist)
    #return render(request,'index.html',{'mylist':mylist})

def index(request):
    #print(mylist)

    return render(request,'index.html', {'mylist': mylist})


def add_asset(request):
    print("before post")
    if request.method=='POST':
       print("starting post..")
       cur=connection.cursor()
       #Asset_Id=request.POST.get['Asset_Id','']
       Asset_Name=request.POST.get('aname','')
       Manufacturer=request.POST.get('man','')
       IMEI=request.POST.get('imei','')
       sql="INSERT INTO asset_manager.inventory (Asset_Name,Manufacturer,IMEI) values (%s,%s,%s)"
       args=(Asset_Name,Manufacturer,IMEI)
       print(sql)
       print(args)
       cur.execute(sql,args)
       cur.execute('commit')
    return render( request,'index.html',{'mylist': mylist})


def delete_asset(request,aid):
    """Delete a post."""


    print(aid)
    sql = "Delete from  asset_manager.inventory where Asset_id=(%s)"
    args = (aid)
    cur = connection.cursor()
    cur.execute(sql, args)
    cur.execute("commit")
    #return "Asset Deleted Successfully"
    global mylist
    return render(request,"index.html",{'mylist': mylist})


