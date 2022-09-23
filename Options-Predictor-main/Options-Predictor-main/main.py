#Imported Libraries
from send_sms import *


#Variables
Menu_Selection = 0
sms_Selection = 0
ap_Selection = 0
OpSt_Selection = 0
dev_Selection = 0


#Functions
def Menu():#main menu
    #Menu_Selection = input("Please select an option: \n0: Menu \n1: Stock Prediction \n2: Current Stock Analysis \n3: Current Options Analysis \n4: Select New Options \n5: Ameritrade Connection Info \n6: Send SMS test \n7: SMS Commands \n9: Quit \n")
    #if Menu_Selection == "0":
    #    Menu()
    #if Menu_Selection == "1":
    #   Stock_Prediction()
    #if Menu_Selection == "2":
    #    Current_Stock_Analysis()
    #if Menu_Selection == "3":
    #    Current_Options_Analysis()
    #if Menu_Selection == "4":
    #    Select_New_Options()
    #if Menu_Selection == "5":
    #    Ameritrade_Connection_Info()
    #if Menu_Selection == "6":
    #    Send_SMS()
    #if Menu_Selection == "6":
    #    SMS_Commands()
    #if Menu_Selection == "9":
    #    Quit()
    #^old menu code, do not use^

    Menu_Selection = input("1: Analysis and Predictions \n2: SMS Settings \n3: Select Options/Stock \nd: Dev Stuff \nq: Quit \n")#menu selection
    if Menu_Selection == "1":
        Analysis_Predictions()
    if Menu_Selection == "2":
        sms_Settings()
    if Menu_Selection == "3":
        Select_OpSt()
    if Menu_Selection == "d":
        Dev_Stuff()
    if Menu_Selection == "q":
        Quit()


def Analysis_Predictions():
    ap_Selection = input("1: Stock Prediction \n2: Stock Analysis \n3: Options Analysis \nm: Menu \nq: Quit \n")#menu selection
    if ap_Selection == "1":
        Stock_Prediction()
        Analysis_Predictions()
    if ap_Selection == "2":
        Current_Stock_Analysis()
        Analysis_Predictions()
    if ap_Selection == "3":
        Current_Options_Analysis()
        Analysis_Predictions()
    if ap_Selection == "m":
        Menu()
    if ap_Selection == "q":
        Quit()


def Stock_Prediction():
    print("Stock Prediction")


def Current_Stock_Analysis():
    print("Stock Analysis")


def Current_Options_Analysis():
    print("Options Analysis")


def sms_Settings():
    sms_Selection = input("1: Positions \n2: Confidence \n3: Balance \n4: Stop \nm: Menu \nq: Quit \n")
    if sms_Selection == "1":
        Positions()
        sms_Settings()
    if sms_Selection == "2":
        Confidence()
        sms_Settings()
    if sms_Selection == "3":
        Balance()
        sms_Settings()
    if sms_Selection == "4":
        Stop()
        sms_Settings()
    if sms_Selection == "m":
        Menu()
    if sms_Selection == "q":
        Quit()
    

def Positions():
    print("Gets current positions")
    sms_Settings()


def Confidence():
    print("Gets confidence level")
    sms_Settings()


def Balance():
    print("Gets current account balance")
    sms_Settings()


def Stop():
    print("Stops the program")
    sms_Settings()


def Select_OpSt():
    OpSt_Selection = input("1: Select New Options \nm: Menu \nq: Quit")
    if OpSt_Selection == "1":
        Select_New_Options()
        Select_OpSt()
    if OpSt_Selection == "m":
        Menu()
    if OpSt_Selection == "q":
        Quit()


def Select_New_Options():
    print("New Options")
    Menu()


def Dev_Stuff():
    dev_Selection = input("1: Ameritrade Connection Info \n2: Send Test SMS \nm: Menu \nq: Quit \n")
    if dev_Selection == "1":
        Ameritrade_Connection_Info()
        Dev_Stuff()
    if dev_Selection == "2":
        Send_SMS()
        Dev_Stuff()
    if dev_Selection == "m":
        Menu()
    if dev_Selection == "q":
        Quit()


def Ameritrade_Connection_Info():
    print("Connection Info")
    Menu()


def Send_SMS():
    Select_Message()
    Menu()


def Quit():
    print("Quitting...")


#Start
Menu()
