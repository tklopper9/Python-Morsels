For this exercise, we're going to normalize CSV files by writing a program, fix_csv.py, that turns a pipe-delimited file into a comma-delimited file. I'll explain how it should work by example.

Your original file will look like this:

```
Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
```

You'll then run your script by typing this at the command line:

```
$ python fix_csv.py cars-original.csv cars.csv
```

Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

```
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
```

Note that it's valid for a comma to be in your input data, but you'll need to surround data cells with commas in them by double quotes when writing your output file. It's also valid for a double quote character to be in your input (you'll need to double up quotes because that's how CSV escaping works). If you find yourself trying to implement these behaviors yourself, please check the hints. Python has utilities for properly implementing quote-handling.

Your program should also fail if too many file names are passed in (only an old file and a new file are allowed).

Remember that Python Morsels exercises rely entirely on the Python standard library: no Pandas or other third-party packages will work through the online test runner. If you're a very avid Pandas user, you could consider this one a learning experience or you might to skip this one.