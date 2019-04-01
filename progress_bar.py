def progress_bar(count, _list):
    rounded_perc = round((count/len(_list))*100)
    print("|" + "#" * rounded_perc + "-" * (100-rounded_perc) + "|" + str(rounded_perc) + "%", end="\r", flush=True)

    if len(_list)-1 == count:
        print("\n", flush=True)