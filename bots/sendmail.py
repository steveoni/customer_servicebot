from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(to_email,link):

    message = Mail(
        from_email='anyemail@gmail.com',
        to_emails=to_email,
        subject='Emergency Status',
        html_content=f"Hi this fellow need an emergency attention {link}")


    sg = SendGridAPIClient(api_key="SG.WhupG9M") #input your api key from sendgrid account

    response = sg.send(message)


if __name__ == "__main__":

    send_mail("youremial@gmail.com",'https://twitter.com/_mytwtbot/status/1208295229725515777')
