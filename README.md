# ASS (Astrometry Solutions Script)
Tired of manually solving and recording multiple solutions in astrometry? Here I have created the beta version of ASS,
A python script to automatically write solutions found by Astrometry to a text file!

Two verions are offered! mp_main.py offers multiprocessing power! Which can significantly reduce the time it takes to spend solving your images.


**you MUST change the directory pathing in the mp_main.py or main.py file.**


# Note 1
In both main.py and mp_main.py,     

ASTROMETRY_TERMINAL_COMMAND = 'solve-field --scale-units arcsecperpix --scale-low 6.000 --scale-high 7.000 ' + image +\
                    ' --overwrite --dir /home/james/Desktop/astrometry_solutions_script/solve_field_images --cpulimit 100'

Is the syntax which is used to run astrometry in the terminal. You can go to http://astrometry.net/doc/readme.html and add any parameters you desire.

# Note 2
Please delete the init text files in the raw_images and solve_field images! Do this after cloning this repository otherwise your program will crash!
