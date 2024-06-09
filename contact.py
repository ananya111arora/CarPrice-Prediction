import streamlit as st

def app():
    st.title('Contact Us 💻')

    # Main container with background color and padding
    st.markdown(
        """
        <style>
            .main-container {
                background-color: #9df9ef;
                padding: 30px;
                border-radius: 15px;
                animation: fadein 1s;
            }
            
            .section-container {
                margin-bottom: 20px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
            }

            .get-in-touch {
                background-color: #51e2f5;
            }

            .contact-info {
                background-color: #9df9ef;
            }

            .office-hours {
                background-color: #ffa8B6;
            }

            @keyframes fadein {
                from { opacity: 0; }
                to   { opacity: 1; }
            }
        </style>
        """
    , unsafe_allow_html=True)

    # Main container for content
    main_container = st.container()
    with main_container:
        # Title and introduction
        st.markdown("<h2 style='color: #a28089;'>Get in Touch!</h2>", unsafe_allow_html=True)
        st.write("Thank you for your interest in our car price prediction model. If you have any inquiries, feedback, or would like to collaborate, please feel free to reach out to us using any of the following methods:")

    # Contact Information
    contact_info_container = st.container()
    with contact_info_container:
        st.markdown("<h3 style='color: #a28089;'>Contact Information:</h3>", unsafe_allow_html=True)
        st.write("- **Email:** [contact@carpricepredictionmodel.com](mailto:contact@carpricepredictionmodel.com)")
        st.write("- **Phone:** +1 (555) 123-4567")
        st.write("- **Address:** 123 Main Street, Cityville, State, Zip Code")
    contact_info_container.markdown('<style> .section-container { background-color: #9df9ef; }</style>', unsafe_allow_html=True)

    # Office Hours
    office_hours_container = st.container()
    with office_hours_container:
        st.markdown("<h3 style='color: #a28089;'>Office Hours:</h3>", unsafe_allow_html=True)
        st.write("Monday - Friday: 9:00 AM - 5:00 PM (EST)")
    office_hours_container.markdown('<style> .section-container { background-color: #ffa8B6; }</style>', unsafe_allow_html=True)

    # Apply animation to the main container
    main_container.markdown(
        """
        <script>
            var container = document.querySelector('.main-container');
            container.style.animation = "fadein 1s";
        </script>
        """
    , unsafe_allow_html=True)

if __name__ == '__app__':
    app()
