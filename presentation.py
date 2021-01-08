import tkinter as tk


class App(tk.Tk):
    """ Main Application Window. all other frames will be inside App"""


    windows = []

    @classmethod
    def close_window(cls, window):
        ind = cls.windows.index(window)
        del cls.windows[ind]
        cls.show_window()

    @classmethod
    def show_window(cls):
        if len(cls.windows)>0:
            if len(cls.windows)>=2:
                cls.windows[-2].pack_forget()
            cls.windows[-1].pack(side='top', fill='both', expand=True, pady=3)


    def __init__(self):
        tk.Tk.__init__(self)
        
        """Navigation panel at top of main window"""
        navigation_bar = tk.Frame(self, height=55, bg='#c2c2c2')
        navigation_bar.pack(fill='x')
        navigation_bar.pack_propagate(False)

        tk.Label(navigation_bar, text='', height= 22, bg='#a9a9a9').pack(side='left') #for left margin in navigation panel

        """Down here create navigation buttons"""     
        btn_first = NavButton(navigation_bar, text='First', height= 22)
        btn_first.bind('<ButtonRelease>', lambda event: self.create_window(First))
        
        btn_second = NavButton(navigation_bar, text='Second', height=22)
        btn_second.bind('<ButtonRelease>', lambda event: self.create_window(Second))
        
        btn_third = NavButton(navigation_bar, text='Third', height=22)
        btn_third.bind('<ButtonRelease>', lambda event: self.create_window(Third))
        
        btn_fourth= NavButton(navigation_bar, text='Fourth', height=22)
        btn_fourth.bind('<ButtonRelease>', lambda event: self.create_window(Fourth))


    def create_window(self, W):
        """invoke if navigation button pressed"""
        windows = App.windows
        window = W(self)
        for wind in windows:
            if isinstance(wind, W):
                ind = windows.index(wind)
                temp = windows.pop(ind)
                windows.append(temp)
                App.show_window()
                return

        windows.append(window)
        App.show_window()


class NavButton(tk.Label):
    """Label customized for navigation buttons"""
    def __init__(self, master, cnf=None, **kw):
        tk.Label.__init__(self, master, cnf, **kw)
        self.pack(side='left', padx=1, pady=1)
        self.configure(width=10)
        self.bind('<Enter>', lambda event:self.config(bg='silver',
         cursor='hand2', fg='white')) 
        self.bind('<Leave>', lambda event:self.config(bg='#d9d9d9', fg='black'))    



class FullWindow(tk.Frame):
    """Abstract Parent Frame """

    def __init__(self, master, cnf=None, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.pack_propagate(False)

        manu_bar = tk.Frame(self, height=20, bg='silver')
        manu_bar.pack(side='top', fill='x')
        manu_bar.pack_propagate(False)
        close = tk.Button(manu_bar, text='x', relief='flat', command=self.delete)
        close.pack(side='right')

    def delete(self):
        self.pack_forget()
        App.close_window(self)


class First(FullWindow):
    """concrete frames inheret customization from FullWindow"""
    def __init__(self, master, cnf=None, **kw):
        FullWindow.__init__(self, master, cnf, **kw)
        self.configure(bg='red')
        lb = tk.Label(self, text='First')
        lb.pack()



class Second(FullWindow):
    """concrete frames inheret customization from FullWindow"""
    def __init__(self, master, cnf=None, **kw):
        FullWindow.__init__(self, master, cnf, **kw)
        self.configure(bg='pink')
        lf = tk.Label(self, text='Second')
        lf.pack()
      


class Third(FullWindow):
    """concrete frames inheret customization from FullWindow"""
    def __init__(self, master, cnf=None, **kw):
        FullWindow.__init__(self, master, cnf=None, **kw)
        self.configure(bg='yellow')
        lb = tk.Label(self, text='Third')
        lb.pack()


class Fourth(FullWindow):
    """concrete frames inheret customization from FullWindow"""
    def __init__(self, master, cnf=None, **kw):
        FullWindow.__init__(self, master, cnf=None, **kw)
        self.configure(bg='orange')
        lb = tk.Label(self, text='Fourth')
        lb.pack()
        



if __name__ == '__main__':
    root = App()
    root.geometry('1000x550+180+50')
    root.mainloop()
    
