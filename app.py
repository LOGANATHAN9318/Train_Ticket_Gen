import streamlit as st
from streamlit_option_menu import option_menu

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
footer{
    visibility:hidden;
}

footer:after{
    content:'Copyright @ 2022';
    visibility:visible;
    display:block;
    position:relative;
    color:tomato;
}
</style>
"""


def booking_ticket():
    st.subheader("Book Your Train Ticket")
    station_list =['','Salem','Chennai','Villupuram','Madurai']
    From = st.selectbox('From',station_list)  
    to = st.selectbox('To',station_list)   
    board_sta = st.text_input("Boarding Station")        
    name = st.text_input("Passenger Name")

    
def about_app():
    pass


    
def main():
    choice = option_menu(
        menu_title=None,
        options=["Home","About","Contact"],
        icons=["house","book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal")

    st.title("Train Ticket Generator")
    st.markdown(hide_menu,unsafe_allow_html=True)
    
    if choice == 'Home':
        booking_ticket()

    elif choice == 'About':
        about_app()


        
if __name__ == '__main__':
    main()

