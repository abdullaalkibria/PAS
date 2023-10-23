from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import pandas as pd
from kivy.properties import ObjectProperty
import csv


class validCheck(MDDialog):
    def btn(self):
        popUp()
        emailCheck()
        passCheck()
        numericCheck()
        
def popUp():
    dialog = None
    if not dialog:
        dialog = MDDialog(
            text = "Please provide every information appropriately!",
            buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    # theme_text_color = "Custom",
                    # text_color = self.theme_cls.primary_color,
                    #on_release = self.dialog.dismiss(),
                    on_release=lambda _: dialog.dismiss()
                    ),
                # MDFlatButton(
                #     text = "DISCARD",
                #     theme_text_color = "Custom",
                #     text_color = self.theme_cls.primary_color,
                #     # on_release = self.dialog.dismiss(),
                #     ),
                ],
            )
    dialog.open()
    
def emailCheck(self, email):
    at=0
    dot = 0
    ch = 0
    # print(ord('@'))
    
    for i in email:
        # print(i)
        if i == '@':
            at+=1
            if at>1:
                return False
            
        elif i=='.':
            dot+=1
            if dot>1:
                return False
            
        elif (ord(email[0])  in range(65, 91)) or (ord(email[0])  in range(97, 123)):
            # print(ord(i))
            ch += 1
        
        else:
            continue
    if (at==0 or at>1) or (dot==0 or dot>1) or ch==0:
        return False
    else:
        return True
    
def passCheck(self, pwd):
    upper = 0
    lower = 0
    digit = 0
    
    if len(pwd)<8 or len(pwd)>32:
        print("Less than 8 or > 32")
        return False
    else:
        for i in pwd:
            if ord(i) in range(65, 91):
                upper += 1
            elif ord(i) in range(90, 123):
                lower += 1
            elif ord(i) in range(0, 10):
                digit += 1
            else:
                continue
            
        if upper==0 and  lower==0 and digit==0:
            return False
        else: 
            print("Valid")
            return True
    
def numericCheck(self):
    pass
class SignUp(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    dob = ObjectProperty(None)
    email = ObjectProperty(None)
    npwd = ObjectProperty(None)
    cpwd = ObjectProperty(None)
    
    def btn(self):
        self.t=False
        
        if (self.npwd.text != "") and (self.npwd.text == self.cpwd.text) and emailCheck(self, self.email.text) == True and passCheck(self, self.cpwd.text) == True:
            
            user = pd.DataFrame([[self.fname.text +" "+ self.lname.text, self.email.text, self.cpwd.text]],
    							columns = ['Name', 'Email', 'Password'])
            
            
            # if self.email.text != "" and self.cpwd.text !="":
            if self.email.text not in users['Email'].unique():
                user.to_csv('login.csv',mode ='a', header = False, index = False )
                
                self.t=True
                
                self.fname.text = ""
                self.lname.text =""
                self.dob.text =""
                self.email.text = ""
                self.npwd.text = ""
                self.cpwd.text = ""

        else:
            popUp()

class Login(Screen):
    
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    # sm = ScreenManager()
    
    def validate(self):
        self.t=False
        
        if self.email.text not in users['Email'].unique() or emailCheck(self, self.email.text) == False:
            popUp()
        elif self.pwd.text not in users['Password'].unique() and passCheck(self, self.pwd.text) == False:
            popUp()
        elif self.pwd.text =="":
            popUp()
        
        elif passCheck(self, self.pwd.text) == True:
            self.t=True
            
            self.email.text = ""
            self.pwd.text = ""
        else:
            popUp()
            
class Home(Screen):
    pass
class Earns(Screen):
    salary = ObjectProperty()
    overTime = ObjectProperty()
    wages = ObjectProperty()
    fbus = ObjectProperty()
    com = ObjectProperty()
    others = ObjectProperty()
    
    def calc1(self):
        self.t = False
        
        # if self.salary.text == ""
        self.sum = int(self.salary.text) + int(self.overTime.text) + int(self.wages.text) + int(self.fbus.text) + int(self.com.text) + int(self.others.text)
        print(self.sum)
        
        earns = pd.DataFrame([[self.sum]], columns = ['Earns'])
        earns.to_csv('earn_cost.csv',mode ='a', header = False, index = False )
        
        # with open('earn_cost.csv','w') as csvfile:
        #     write = csv.writer(csvfile, delimiter =',')
        #     write.writerow(['Spam'] * 5 + ['Baked Beans'])
        #     write.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
            
        # with open('earn_cost.csv') as cs:
        #     read = csv.reader(cs, delimiter =',')
        #     for row in read:
        #         print(','.join(row))
        
class Costs(Screen):
    rent = ObjectProperty()
    hins = ObjectProperty()
    shop = ObjectProperty()
    helth = ObjectProperty()
    tution = ObjectProperty()
    oth = ObjectProperty()
    def calc2(self):
        self.t = False
        
        # if self.salary.text == ""
        self.sumc = int(self.rent.text) + int(self.hins.text) + int(self.shop.text) + int(self.helth.text) + int(self.tution.text) + int(self.oth.text)
        print(self.sumc)
        
        costs = pd.DataFrame([[self.sumc]], columns = ['Costs'])
        costs.to_csv('earn_cost.csv',mode ='a', header = False, index = False )
        
        
class Suggestions(Screen):
    pass
class History(Screen):
    def table(self):
        screen = MDScreen()
        self.t = MDDataTable(
            pos_hint = {"center_x": .5, "center_y":.5},
            size_hint = (.9, 1),
            check = True,
            column_data = [
                ("Date",dp(30)),
                ("Earns",dp(30)),
                ("Costs",dp(30)),
                ("Save",dp(30)),
                
                ],
            row_data = [
                ("07 Oct, 2022",dp(30)),
                ("3000",dp(30)),
                ("1500",dp(30)),
                ("1500",dp(30)),
                ],
            sorted_on = "Date",
            sorted_order = "ASC",
            elevation = 10,
            )
        self.t.bind(on_row_press=self.on_row_press)
        self.t.bind(on_check_press=self.on_check_press)
        
        screen.add_widget(self.t)
        return screen
    def on_enter(self):
        self.table()
        
    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''
        print(instance_table, instance_row)
    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''
        print(instance_table, current_row)
    
   
        
class Profile(Screen):
    pass
class AboutUs(Screen):
    pass
  
users=pd.read_csv('login.csv',sep=',')
print("Users",users)
# earns_costs = pd.read_csv('earn_cost.csv', sep = ',')
# print("Earns_Costs", earns_costs)


class Personal_Accounting_System(MDApp):
    
    def build(self):
        
        self.icon = "iconPAS.png"
        self.theme_cls.theme_style = "Light"
        self.root = Builder.load_file("PAS.kv")
        
        
       
Personal_Accounting_System().run()


