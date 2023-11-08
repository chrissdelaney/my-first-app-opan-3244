import os

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# ENVIRONMENT VARIABLES AND CONSTANTS

load_dotenv() # go look in the .env file for any env vars

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")


def send_email(recipient_address=SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)
    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)
        return response.status_code

    except Exception as err:
        print(type(err))
        print(err)
        return None



if __name__ == "__main__":

    # ONLY WANT TO DO IF RUNNING THIS FILE FROM COMMAND LINE
    # (NOT IF IMPORTING A FUNCTION FROM THIS FILE)
    user_address = input("Please enter your email address: ")


    my_content = """

        <img
            src="https://img.freepik.com/free-vector/flat-ice-cream-collection_23-2148982427.jpg"
            alt="image of an ice cream"
            height=100
        >

        <h1>Ice Cream Shop Menu</h1>

        <p>Most popular flavors:</p>

        <ul>
            <li>Vanilla Bean </li>
            <li>Choc </li>
            <li>Strawberry</li>
        </ul>
    """
    send_email(html_content=my_content, recipient_address=user_address)