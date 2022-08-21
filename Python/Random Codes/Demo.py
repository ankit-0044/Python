import os
import glob
import pandas as pd

def restart_csv():
    try:
        path = input("Enter path: ")
        Section = input("Enter section: ")
        print("Yhn tak sab shi hai")

        all_files = glob.glob(os.path.join(path, "Makgn*.csv"))
        print("Sari Files ye hai",all_files)
        frame = pd.DataFrame()
        list_ = []
        print("Loop se phle",list_)
        for file_ in all_files:
            df = pd.read_csv(file_, nrow =1, low_memory=False)
            list_.append(df)
            print("Loop k andr",list_)
        print("Loop k baad",list_)
        if list_ == []:
            print("List khali hai")
        else:
            frame = pd.concat(list_)
            frame.to_csv(path + "csv file" + Section + ".csv", index=False)

        print("CSV bn gyi")
        return True
    except:
        print("Koi dikkat hai")
        return True
while True:
    check = input("Enter Y to continue: ")
    if check == 'y':
        restart_csv()
    else:
        print('Exiting..')
        break
