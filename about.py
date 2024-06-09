import streamlit as st
import random

def get_random_color():
    colors = ['#51e2f5', '#9df9ef', '#edf756', '#ffa8b6', '#a28089']
    return random.choice(colors)

def app():
    st.title('About Us')

    # Generate random background color
    random_color = get_random_color()

    # Apply custom CSS for the main container
    st.markdown(
        f"""
        <style>
            .main-container {{
                background-color: #edf756;
                padding: 30px;
                border-radius: 15px;
                animation: fadein 1s;
            }}
            
            .section-container {{
                margin-bottom: 20px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
                background-color: #9df9ef; /* Set a contrasting color for the content */
            }}

            @keyframes fadein {{
                from {{ opacity: 0; }}
                to   {{ opacity: 1; }}
            }}
        </style>
        """
    , unsafe_allow_html=True)

    # Main container for content
    with st.container() as main_container:
        # Title and introduction
        st.markdown("<h2 style='color: #51e2f5;'>Get in Touch!</h2>", unsafe_allow_html=True)
        st.write("Thank you for your interest in our car price prediction model. If you have any inquiries, feedback, or would like to collaborate, please feel free to reach out to us using any of the following methods:")

    # FAQ Section
    with st.container() as faq_section:
        st.subheader('FAQ Section:')
        st.write("Q: How accurate is your car price prediction model?")
        st.write("A: Our model boasts an accuracy rate of over 90%, backed by rigorous testing and validation.")
        st.write("Q: Do you offer customized solutions for specific car markets?")
        st.write("A: Yes, we provide tailored solutions to meet the unique needs of different car markets globally.")

    # Social Media Links
    with st.container() as social_media_section:
        st.subheader('Social Media:')
        st.write("Connect with us on social media:")
        st.write("- [Facebook](https://www.facebook.com/carpricepredictionmodel)")
        st.write("- [Twitter](https://twitter.com/carpricepredict)")
        st.write("- [Instagram](https://www.instagram.com/carpricepredictionmodel)")

    # Map and Directions
    with st.container() as map_section:
        st.subheader('Map and Directions:')
        st.write("[Google Maps Embed]")

    # Privacy Policy
    with st.container() as privacy_policy_section:
        st.subheader('Privacy Policy:')
        st.write("Please read our [Privacy Policy](/privacy-policy) to understand how we handle your personal information securely.")

    # Terms of Service
    with st.container() as terms_of_service_section:
        st.subheader('Terms of Service:')
        st.write("By using our website and services, you agree to our [Terms of Service](/terms-of-service).")

    # Customer Support Options
    with st.container() as customer_support_section:
        st.subheader('Customer Support Options:')
        st.write("For additional support, you can reach out to our customer support team through:")
        st.write("- Live Chat: [Chat Now]")
        st.write("- Support Ticket System: [Submit a Ticket]")

    st.write("We value your feedback and strive to provide the best possible service to our customers. Thank you for choosing our car price prediction model!")

if __name__ == "__app__":
    app()
