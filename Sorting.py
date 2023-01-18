import  tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Importing algorithms file where all the sorting functions are present
from algorithms import *


# Main window 
window = Tk()
window.title("Sorting")

window.geometry("1400x900")



algorithm_name = StringVar()
#drop down list for all sorting methods
algo_list = ['Bubble Sort','Insertion Sort',"Selection Sort","Merge Sort","Heap Sort","Quick Sort","Quick Sort Using 3 Median" ]


data = []

res = []

# This funciton will trigger a selected algorithm and start sorting also calculate the time 
def sort():
    
    sizen = int(Array_size.get())
    
    if algo_menu.get() == 'Bubble Sort':
        data = random.sample(range(1, 100), sizen)
        
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res = bubble_sort(data)
        time_taken = time.time() - start_time
        
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
        

    #below comments apply to all functions 
    elif algo_menu.get() == 'Insertion Sort':
        
        data = random.sample(range(1, 100), sizen) #generating array using range
        
        original_array.config(text="Input:"+str(data)) #printing the original aaray in GUI
        start_time = time.time()
        res = Insertion_sort(data) # call the sort function
        time_taken = time.time() - start_time
        
        result_array.config(text="Result "+str(res)) # print the result array in GUI
        Run_time.config(text="Run time :"+str(time_taken)+" seconds") # print the time taken
        
    elif algo_menu.get() == 'Selection Sort':
        
        data = random.sample(range(1, 100), sizen)
        
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res = Selection_sort(data)
        time_taken = time.time() - start_time
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
        
        
        
    elif algo_menu.get() == 'Merge Sort':
        
        data = random.sample(range(1, 100), sizen)
        
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res =  merge_sort_main(data)
        time_taken = time.time() - start_time
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
        
    elif algo_menu.get() == 'Heap Sort':
        
        data = random.sample(range(1, 100), sizen)
        
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res = Heap_sort_main(data)
        time_taken = time.time() - start_time
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
       
    elif algo_menu.get() == 'Quick Sort':
        
        data = random.sample(range(1, 100), sizen)
        
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res = Quick_sort_main(data)
        time_taken = time.time() - start_time
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
        
    elif algo_menu.get() == 'Quick Sort Using 3 Median':
        
        data = random.sample(range(1, 100), sizen)
        original_array.config(text="Input:"+str(data))
        start_time = time.time()
        res = Quick_median(data)
        time_taken = time.time() - start_time
        result_array.config(text="Result "+str(res))
        Run_time.config(text="Run time :"+str(time_taken)+" seconds")
        
    


### User interface here ###
UI_frame = Frame(window, width= 1000, height=400)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ")
l1.grid(row=0, column=0, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1,sticky=NW)
algo_menu.current(0)

# dropdown to select Array size
l2 = Label(UI_frame, text="Array Size ")
l2.grid(row=1, column=0, sticky=W)
Array_size =Entry(UI_frame, width=35)
Array_size.grid(row=1, column=1,sticky=W)


# sort button 

b1 = Button(UI_frame, text="Sort", command=sort)
b1.grid(row=3, column=1, padx=5, pady=5)

#Original array display
original_array=Label(UI_frame, text="Input", font=('Calibri 10'))
original_array.grid(row=8,column=0,columnspan=10,sticky=W,rowspan=5)

#Result array display
result_array=Label(UI_frame, text="Result", font=('Calibri 10'))
result_array.grid(row=15,column=0,columnspan=10,sticky=W)

#Runtime in Seconds display
Run_time=Label(UI_frame, text="Run time", font=('Calibri 10'))
Run_time.grid(row=25,column=0,columnspan=10,sticky=W)






#The below plot function is to plot the size vs run time for sorting algorithms in GUI
def plot():
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().grid(row=20,column=0,sticky=W,columnspan=20)
    sizen =100
    
    x = []
    y =[]
    z = []
    a = []
    b = []
    d= []
    ax1.set_xlabel("Size of an Input Array")
    ax1.set_ylabel("Time Taken in (s)")
    t = []
    for i in range(0,5):
        t = Compare_all(sizen)
        print(t)
        x.append(sizen)
        y.append(t[0])
        z.append(t[1])
        a.append(t[2])
        b.append(t[3])
        d.append(t[4])
        sizen+=1500
    

    
    ax1.plot(x,y,label="Insertion Sort")
    ax1.plot(x,z,label="Bubble Sort")
    ax1.plot(x,a,label="Merge Sort")
    ax1.plot(x,b,label="Selection Sort")
    
    ax1.plot(x,d,label="Heap Sort")
    

    ax1.legend()
    

# button that displays the plot

plot_button = Button(UI_frame, text=" Compare Size vs Run Time ", command=plot)
plot_button.grid(row=35, column=1, padx=5, pady=5)
  


window.mainloop()