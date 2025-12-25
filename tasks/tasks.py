from celery import shared_task
import time

@shared_task
def send_welcome_email(username):
    """
    Simulates a heavy task (waiting 10 seconds).
    """
    print(f"Starting to send email to {username}...")
    time.sleep(10)  # Sleep for 10 seconds
    print(f"Email sent to {username}!")
    return "Done"