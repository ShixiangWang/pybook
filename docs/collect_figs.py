import shutil, sys, os

with open("./fig_header.txt", mode="r", encoding="utf-8") as f:
    contents = f.readlines()

useful_text = []

for i in contents:
    if i == "\n":
        pass
    else:
        if i.startswith("File") or i.startswith("!["):
            useful_text += i.splitlines()
        else:
            pass

chunks = "".join(useful_text).split("File ")
for chunk in chunks:
    if chunk.endswith(".md") or chunk == "":
        continue
    fn, *figs = tuple(chunk.split('!['))
    print("=> Processing file", fn, "...")
    dirname = "./figures/chapter" + fn.split("-")[0]
    print("==> Creating ", dirname)
    os.makedirs(dirname)
    for fig in figs:
        fig_name, fig_loc = tuple(fig.split("]("))
        if fig_loc.endswith(")"):
            fig_loc = fig_loc[:-1]
        print("==> Found figure title %s and path %s" %(fig_name, fig_loc))
        print("==> Processing ...")
        if fig_loc.endswith("png"):
            shutil.copy(fig_loc, dirname + "/" + fig_name + ".png")
        elif fig_loc.endswith("jpg"):
            shutil.copy(fig_loc, dirname + "/" + fig_name + ".jpg")
        else:
            print("Something is not captured for ", fig_loc)
            sys.exit(1)
    
