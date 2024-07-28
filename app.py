import streamlit as st
import os

# Constants
USER_DATA_FILE = 'user_data.csv'

# Function to load user data
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        return pd.read_csv(USER_DATA_FILE)
    else:
        return pd.DataFrame(columns=['username', 'password'])

# Function to save user data
def save_user_data(data):
    data.to_csv(USER_DATA_FILE, index=False)

# Define pages
def login_page():
    st.title('Login and Registration System with Google')

    # Google login button (placeholder for actual implementation)
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.button('Login with Google'):
        # Implement Google login here (This is a placeholder)
        st.session_state['logged_in'] = True
        st.session_state['user'] = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'picture': 'https://via.placeholder.com/100'
        }

    if st.session_state['logged_in']:
        user = st.session_state['user']
        st.success(f'Welcome {user["name"]} ({user["email"]})')
        st.image(user['picture'], width=100)
        if st.button('Logout'):
            st.session_state['logged_in'] = False
            st.session_state['user'] = None
        if st.button('Go to News Application'):
            st.session_state['page'] = 'news_page'
    else:
        st.warning('Please log in using Google.')

# Main App
def main():
    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login_page'
    
    # Render the appropriate page
    if st.session_state['page'] == 'login_page':
        login_page()
    elif st.session_state['page'] == 'news_page':
        st.experimental_rerun('/pages/page1')

if __name__ == '__main__':
    main()
