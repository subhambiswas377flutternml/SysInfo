import tkinter
import shutil
import psutil
from win32com.client import GetObject
from tkinter import messagebox

try:
    class showData:
        def __init__(self):

            info = GetObject('winmgmts:root\cimv2')
            cpu = info.ExecQuery('Select * from Win32_Processor')
            data = cpu[0].name
            data = data.split()
            
            freq = data[-1]
            data.pop()
            data.pop()

            name = ' '.join(data)

            threads = str(psutil.cpu_count())
            cores = str(psutil.cpu_count(logical = False))

            self.c_news = 'Processor :  '+name+'\n'+'Clockspeed :  '+freq+'\n'+'Cores :  '+cores+'\n'+'Threads :  '+threads
            

                        
        def cpu_Data(self):

            messagebox.showinfo('Processor',self.c_news)
            
        def memoryData(self):

            minfo = psutil.virtual_memory()
            t = round((minfo.total/1000000000-1),2)
            a = round((minfo.available/1000000000),2)

            md = 'Total :  '+str(t)+' GB'+'\n'+'Available :  '+str(a)+' GB'
            messagebox.showinfo('Memory',md)


            
        def diskData(self):

            location = shutil.which(cmd = 'cmd.exe')
            data = location.split('\\')
            directory = data[0]+'\\'

            du = shutil.disk_usage(directory)
            dt = round((du.total/1000000000))
            da = round((du.free/1000000000),2)

            dd = 'Total :  '+str(dt)+' GB'+'\n'+'Available :  '+str(da)+' GB'
            messagebox.showinfo('Installation Drive',dd)
    
        

    def colorChange(event):

        global obj
        global f1
        global f2
        global f3
        global f4
        global cpu_lab1
        global cpu_lab2
        global ram_lab1
        global ram_lab2
        global disk_lab1
        global disk_lab2
        global battery_lab1
        global battery_lab2
        global fb
        global flab
        global button
        global default_bgcolor

        mode = event.widget.cget('text')

        if mode=='Dark':
            obj.configure(bg = 'black')
            
            f1.configure(bg = 'black')
            f2.configure(bg = 'black')
            f3.configure(bg = 'black')
            f4.configure(bg = 'black')
            
            cpu_lab1.configure(fg = 'cyan',bg = 'black')
            ram_lab1.configure(fg = 'cyan',bg = 'black')
            disk_lab1.configure(fg = 'cyan',bg = 'black')
            battery_lab1.configure(fg = 'cyan',bg = 'black')
            
            cpu_lab2.configure(bg = 'cyan')
            ram_lab2.configure(bg = 'cyan')
            disk_lab2.configure(bg = 'cyan')
            battery_lab2.configure(bg = 'cyan')

            fb.configure(bg = 'black')
            flab.configure(bg = 'black')
            button.configure(text = 'Light')

        else:
            obj.configure(bg = default_bgcolor)
            
            f1.configure(bg = default_bgcolor)
            f2.configure(bg = default_bgcolor)
            f3.configure(bg = default_bgcolor)
            f4.configure(bg = default_bgcolor)
            
            cpu_lab1.configure(fg = 'black',bg = default_bgcolor)
            ram_lab1.configure(fg = 'black',bg = default_bgcolor)
            disk_lab1.configure(fg = 'black',bg = default_bgcolor)
            battery_lab1.configure(fg = 'black',bg = default_bgcolor)
            
            cpu_lab2.configure(bg = 'white')
            ram_lab2.configure(bg = 'white')
            disk_lab2.configure(bg = 'white')
            battery_lab2.configure(bg = 'white')

            fb.configure(bg = default_bgcolor)
            flab.configure(bg = default_bgcolor)
            button.configure(text = 'Dark')
            


    def operation():
        global cpu_lab2
        global ram_lab2
        global disk_lab2
        global battery_lab2

        c = 0
        cp = 0

        while True:
            
            # CPU Section
            if c==50:
                cp_val = str(round(cp/50))+'%'
                cpu_lab2.configure(text = cp_val)
                cpu_lab2.update()
                cp = 0
                c = 0
            else:
                cp+=psutil.cpu_percent(0.02)
                c+=1
                cpu_lab2.update()

            # RAM Section
            r_val = str(round(psutil.virtual_memory().percent))+'%'
            ram_lab2.configure(text = r_val)
            ram_lab2.update()

            # DISK Section
            location = shutil.which(cmd = 'cmd.exe')
            data = location.split('\\')
            directory = data[0]+'\\'
            
            du = shutil.disk_usage(directory)
            percent = str(round(((du.used/du.total)*100)))+'%'

            disk_lab2.configure(text = percent)
            disk_lab2.update()

            # Battery Section
            bat_obj = psutil.sensors_battery()
            
            if bat_obj==None:
                battery_lab2.configure(text = 'No Battery',fg = 'red')
                battery_lab2.update()
                
            else:
                plugged = bat_obj.power_plugged
                bat_percent = bat_obj.percent

                if plugged:
                    context = str(bat_percent)+'%  '+'CR'
                    battery_lab2.configure(fg = 'blue')
                else:
                    context = str(bat_percent)+'%  '+'NC'
                    battery_lab2.configure(fg = 'red')

                battery_lab2.configure(text = context)
                battery_lab2.update()
                
                


    # Front - End
    obj = tkinter.Tk()
    obj.geometry('280x298')
    obj.minsize(280,298)
    obj.maxsize(280,298)
    obj.title('SysInfo Meter')
    obj.iconbitmap('anywhere.ico')

    default_bgcolor = obj.cget('bg')
    data_object = showData()

    # cpu Info

    f1 = tkinter.Frame(obj)
    f1.pack(pady = 10,anchor = 'w')
    cpu_lab1 = tkinter.Label(f1,text = 'CPU',font = 'lucida 20 bold',
                             fg = 'black')
    cpu_lab1.pack(side = tkinter.LEFT,padx = 20)

    cpu_lab2 = tkinter.Label(f1,text = '',font = 'lucida 20 bold',
                             fg = 'blue',bg = 'white',relief = tkinter.SUNKEN,
                             width = 5)
    cpu_lab2.pack(side = tkinter.LEFT,padx = 11)

    cpu_bt = tkinter.Button(f1,text = 'info',font = 'lucida 14 bold',
                         fg = 'white',bg = 'orange',relief = tkinter.GROOVE)
    cpu_bt.pack(padx = 10)
    cpu_bt.configure(command = lambda:data_object.cpu_Data())


    # ram info

    f2 = tkinter.Frame(obj)
    f2.pack(pady = 10,anchor = 'w')
    ram_lab1 = tkinter.Label(f2,text = 'RAM',font = 'lucida 20 bold',
                             fg = 'black')
    ram_lab1.pack(side = tkinter.LEFT,padx = 20)

    ram_lab2 = tkinter.Label(f2,text = '',font = 'lucida 20 bold',
                             fg = 'blue',bg = 'white',relief = tkinter.SUNKEN,
                             width = 5)
    ram_lab2.pack(side = tkinter.LEFT,padx = 9)
    ram_bt = tkinter.Button(f2,text = 'info',font = 'lucida 14 bold',
                         fg = 'white',bg = 'orange',relief = tkinter.GROOVE)
    ram_bt.pack(padx = 10)
    ram_bt.configure(command = lambda:data_object.memoryData())

    # disk info

    f3 = tkinter.Frame(obj)
    f3.pack(pady = 10,anchor = 'w')
    disk_lab1 = tkinter.Label(f3,text = 'DISK',font = 'lucida 20 bold',
                             fg = 'black')
    disk_lab1.pack(side = tkinter.LEFT,padx = 20)

    disk_lab2 = tkinter.Label(f3,text = '',font = 'lucida 20 bold',
                             fg = 'blue',bg = 'white',relief = tkinter.SUNKEN,
                             width = 5)
    disk_lab2.pack(side = tkinter.LEFT,padx = 3)

    disk_bt = tkinter.Button(f3,text = 'info',font = 'lucida 14 bold',
                         fg = 'white',bg = 'orange',relief = tkinter.GROOVE)
    disk_bt.pack(padx = 10)
    disk_bt.configure(command = lambda:data_object.diskData())

    # battery info

    f4 = tkinter.Frame(obj)
    f4.pack(pady = 10,anchor = 'w')
    battery_lab1 = tkinter.Label(f4,text = 'BAT',font = 'lucida 20 bold',
                             fg = 'black')
    battery_lab1.pack(side = tkinter.LEFT,padx = 20)

    battery_lab2 = tkinter.Label(f4,text = '',font = 'lucida 20 bold',
                             fg = 'blue',bg = 'white',relief = tkinter.SUNKEN,
                             width = 10)
    battery_lab2.pack(side = tkinter.LEFT,padx = 12)


    # UI Color Change
    fb = tkinter.Frame(obj)
    fb.pack(pady = 10)
    flab = tkinter.Label(fb,text = '   ',fg = 'white',font = 'lucida 20 bold')
    flab.pack(side = tkinter.LEFT,padx = 5)
    button = tkinter.Button(fb,text = 'Dark',font = 'lucida 14 bold',
                            fg = 'white',bg = 'orange',
                            relief = tkinter.GROOVE)
    button.pack(padx = 50,anchor = 'e')
    button.bind('<Button-1>',colorChange)



    operation()


    obj.mainloop()

except:
    print('Program Ended')
