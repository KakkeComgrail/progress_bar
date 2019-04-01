def progress_bar(count, _list):
    print("|" + "#" * round((count/len(_list))*100) + "-" * (100-round((count/len(_list))*100)) + "|" + str(round((count/len(_list))*100)) + "%", end="\r", flush=True)
    if len(_list)-1 == count:
        print("\n", flush=True)