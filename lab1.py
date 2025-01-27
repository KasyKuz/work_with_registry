import argparse
import os
import shutil
import winreg

def file_creating (fname):
    try:
        f = open(fname, 'x')
        f.close()
        print("-----success----")
    except FileExistsError:
        print("-----File already exists------")
def file_deleting (fname):
    try:
        os.remove(fname)
        print("-----success----")
    except FileNotFoundError:
        print("---------No such file----------")




def file_writing (fname, texting):
    try:
        f = open(fname, 'w')
        f.write(texting)
        f.close()
        print("-----success----")
    except FileNotFoundError:
        print("---------No such file----------")

    except PermissionError:
        print("---------Permission denied-----------")

def file_reading (fname: str):
    try:
        f = open(fname, 'r')
        print(f.read())
        f.close()
        print("-----success----")
    except FileNotFoundError:
        print("---------No such file----------")

def file_coping (ffrom: str, fto: str):
    try:
        shutil.copy(ffrom, fto)
    except FileNotFoundError:
        print("------------No such file---------")
    except PermissionError:
        print("-----Permission denied-----")

def file_new_name (fname, nname):
    try:
        os.rename(fname, nname)
    except FileNotFoundError:
        print("--------No such file--------")
    ''' 
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    file_deleting(fname)
    file_creating(fname)
    file_writing(nname, lines)
    '''

def fkCreate (cn: str, key: str):
    cnst = cn[:4]
    try:
        if cnst == "HKCU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

        if cnst == "HKCR":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

        if cnst == "HKLM":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        elif cnst == "HKU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)

        elif cnst == "HKCC":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)
    
        winreg.CreateKey(reg, key)
#сделать класс exeption, в котором все ошибки
#разобраться почему ошибка аргумента
    except PermissionError:
        print("-----Permission denied-----")
        return
    except OSError:
        print("-----error in paramentra-----")
        return
    #winreg.CreateKey(reg, key)



def fkDelete (cnst: str, key: str):
    try:
        if cnst == "HKCU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

        elif cnst == "HKCR":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

        elif cnst == "HKLM":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        elif cnst == "HKU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)

        elif cnst == "HKCC":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)

        winreg.DeleteKey(reg, key)
    except PermissionError:
        print("-----Permission denied-----")

def fkMean (cnst: str, key: str, name: str, meaning: str):
    try:
        if cnst == "HKCU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

        elif cnst == "HKCR":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

        elif cnst == "HKLM":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        elif cnst == "HKU":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)

        elif cnst == "HKCC":
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)

        open_key = winreg.OpenKeyEx(reg, key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(open_key, name, 0, winreg.REG_SZ, meaning)
        winreg.CloseKey(reg)
    except PermissionError:
        print("-----Permission denied-----")

def make_arguments ():
    p = argparse.ArgumentParser()
#file
    p.add_argument("-cr", "--f_create", help="we will create file")
    p.add_argument("-del", "--f_delete", help="we will delete file")
    p.add_argument("-wr", "--f_write_in", nargs=2, help="sth will be written in file")
    p.add_argument("-re", "--f_read_from", help="sth will be read from file")
    p.add_argument("-cpy", "--f_copy", nargs=2, help="file will be coped")
    p.add_argument("-nn", "--f_rename", nargs=2, help="file will be renamed")
#registry
    p.add_argument("-ksr", "--keyCreate", nargs=2, help="we will create key for registry")
    p.add_argument("-kdel", "--keyDelete", nargs=2, help="we will delete key for registry")
    p.add_argument("-km", "--keyMean", nargs=4, help="we will add meaning key for registry")

    args = p.parse_args()
    if (args.f_create):
        file_creating(args.f_create)
    elif (args.f_delete):
        file_deleting(args.f_delete)
    elif (args.f_write_in):
        file_writing(args.f_write_in[0], args.f_write_in[1])
    elif (args.f_read_from):
        file_reading(args.f_read_from)
    elif (args.f_rename):
        file_new_name(args.f_rename[0], args.f_rename[1])
    elif (args.f_copy):
        file_coping(args.f_copy[0], args.f_copy[1])
    elif (args.keyCreate):
        fkCreate(args.keyCreate[0], args.keyCreate[1])
    elif (args.keyDelete):
        fkDelete(args.keyDelete[0], args.keyDelete[1])
    elif (args.keyMean):
        fkMean(args.keyMean[0], args.keyMean[1], args.keyMean[2], args.keyMean[3])
    else:
        print("Something's gone wrong")
    #return p.parse_args()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #a = input()
   # print(a)
    make_arguments()
