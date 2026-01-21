import streamlit as st #required for webapps
import functions
from functions import get_todos

todos = functions.get_todos()#reads data from text file and stores it in todos variable
def add_todo(): #new function to add t,odo checkbox
    web_todo = st.session_state["new_todo"] +"\n" #takes the value of the key new_todo in the dictionary and puts it into web_todo variable
                                        #(gets userinput puts it in t,odo variable with a breakline)
    todos.append(web_todo)# adds web_todo to todos list
    functions.write_todos(todos) #overwrites text file with new list todos

    #creates a function that receives data of the input box of the web app and puts it in the t,odo variable



st.title("My TODO APP BRO")
st.subheader("yoyo")
#st.write("This app is sick bro")



for index, todo in enumerate(todos): # for every t,odo in todos list create a checkbox for them. function is called above rewrites the todos list
    checkbox = st.checkbox(todo,key = todo) # creates a checkbox for each t,odo, each t,odo item has a key of its own name
    # and outputs true or false whether the checkbox is ticked this info is stored in checkbox variable
    if checkbox:
        todos.pop(index) #deletes the entry of the list which has the same index.
        functions.write_todos(todos) #writes new todos to Todos.txt
        del st.session_state[todo] #deletes the t,odo selected from the session state dictionary
        st.rerun()#reruns the code, needed for checkboxes

st.text_input(label="",placeholder="Enter a todo",
              on_change=add_todo,key="new_todo") # creates an input box and empty label below the checkbox,
                                                # placeholder text within the input box
#key=new_todo gives a key to refer to the data inputted by the user in input box
#on change (pressing enter) call the add_todo function

st.session_state #allows to view terminal in webapp for testing, refresh page to get it to work, delete when finished