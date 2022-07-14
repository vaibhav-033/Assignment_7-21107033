#1

def Calculate_GST(org_cost, N_price):
 
    return (((N_price - org_cost) * 100) / org_cost);

org_cost = int(input("Enter the original price: "))
N_price = int(input("Enter the new price: "))
print("GST = ",end='')
print(Calculate_GST(org_cost, N_price),"%")


#2

from tkinter import *

import calendar

def showCal() :

	new_gui = Tk()

	new_gui.config(background = "white")

	new_gui.title("CALENDAR")

	new_gui.geometry("550x600")

	fetch_year = int(year_field.get())

	cal_content = calendar.calendar(fetch_year)

	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

	cal_year.grid(row = 5, column = 1, padx = 20)
	
	new_gui.mainloop()


#Driver Code
if __name__ == "__main__" :

	gui = Tk()

	gui.config(background = "white")

	gui.title("CALENDAR")

	gui.geometry("250x140")

	cal = Label(gui, text = "CALENDAR", bg = "dark gray",
							font = ("times", 28, 'bold'))

	year = Label(gui, text = "Enter Year", bg = "light green")
	
	year_field = Entry(gui)

	Show = Button(gui, text = "Show Calendar", fg = "Black",
							bg = "Red", command = showCal)

	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	cal.grid(row = 1, column = 1)

	year.grid(row = 2, column = 1)

	year_field.grid(row = 3, column = 1)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	gui.mainloop()
	

#3

from tkinter import *

expression = ""

def press(num):
	global expression

	expression = expression + str(num)

	equation.set(expression)

def equalpress():

	try:

		global expression

		total = str(eval(expression))

		equation.set(total)

		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


#Driver Code
if __name__ == "__main__":
	
	gui = Tk()

	gui.configure(background="light green")

	gui.title("Simple Calculator")

	gui.geometry("270x150")

	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation)

	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)

	gui.mainloop()


#4

lst_in = eval(input("Enter the list: "))

#Using quick sort algorithm
def quick_sort(list):
    if len(list) <= 1:                                                                                  #Base case
        return list
    else:
        left_arr = [x for x in list if x < list[0]]
        pivot = [x for x in list if x == list[0]]
        right_arr = [x for x in list if x > list[0]]
        return quick_sort(left_arr) + pivot + quick_sort(right_arr)                                     #Recursive call by taking pivot as the first element of the unsorted list
def merge_sort(list):
    pass

lst_out = quick_sort(lst_in)
print("The sorted list(using quick sort algorithm) is: ", lst_out)
lst_out2 = merge_sort(lst_in)
print("The sorted list(using merge sort algorithm) is: ", lst_out)


#5

n = int(input())
li = list(map(int, input().strip().split()))

# Part 1
li.sort()
print("Sorted array is:", li)

# Part 2
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input())
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# Part 3
if(ind == -1):
    print("No element\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)


#6

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))