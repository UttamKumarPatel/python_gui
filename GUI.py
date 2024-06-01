import streamlit as st
import functions as tf

st.title("Hello World!")
# st.subheader("Patel")
# st.checkbox("I am fine")
todos = tf.gettodos()
def addTodo():
    todo = st.session_state['todoinput']
    todos.append(todo + '\n')
    tf.writetodos(todos)
    st.session_state['todoinput']=''

st.text_input(label='Enter a todo',placeholder='Add a todo',on_change=addTodo, key='todoinput')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = f"{todo}_{index}")
    # print(checkbox)
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        tf.writetodos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.experimental_rerun()

# st.session_state
