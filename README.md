# Astrometry Solutions Script
Here I have created a very simple python script to automatically write solutions found by Astrometry to a text file!

Two verions are offered! mp_main.py offers multiprocessing power! Which can significantly reduce the time it takes to spend solving your images.

<ol>
  <li>You MUST change the directory pathing in the mp_main.py or main.py file.</li>
  <li>It is key you download and install ASTROMETRY prior to running this script</li>
</ol>

It might be better to email me (20jjp1@queensu.ca) for setting up to program but I can guarentee that the investment will be worth it.

<em>Instructions to install Astrometry</em> -- http://astrometry.net/doc/build.html


# IMPORTANT
In both main.py and mp_main.py,     

ASTROMETRY_TERMINAL_COMMAND = 'solve-field --scale-units arcsecperpix --scale-low 6.000 --scale-high 7.000 ' + image +\
                    ' --overwrite --dir /home/james/Desktop/astrometry_solutions_script/solve_field_images --cpulimit 100'

Is the syntax which is used to run astrometry in the terminal. You can go to http://astrometry.net/doc/readme.html and add any parameters you desire.

DELETE THE __.init__.py FILES!! Do this after cloning this repository otherwise your program will crash!
