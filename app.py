import streamlit as st


def booking_ticket():
    st.subheader("Book Your Train Ticket")
    From = st.text_input("From")  
    to = st.text_input("To")    
    board_sta = st.text_input("Boarding Station")        
    name = st.text_input("Passenger Name")
    btn = 


def about_app():
    pass


    
def main():
    st.title("Train Ticket Generator")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == 'Home':
        booking_ticket()

    elif choice == 'About':
        about_app()
        
        
if __name__ == '__main__':
    main()

