import multiprocessing

from celery import shared_task
from threading import Thread
from django.contrib.auth.models import User
from queue import Queue

# Creating the queue for sending custom mails
mail_queue = Queue()

def send_custom_mails():
     while not mail_queue.empty():
        email = mail_queue.get()        
        # Get the email structure from the queue
        # Logic to send the email to the user
    

@shared_task(bind = True)
def custom_mail(self, subject, preview_text, article_url, html_content, plain_text_content):
    
    # Getting the number of cores in the system
    num_cores = multiprocessing.cpu_count()
    
    # Setting the number of worker threads to twice the number of cores
    max_worker_threads = num_cores * 2 
    
    activeUsers = User.objects.filter(is_active = True)
    
    for user in activeUsers:
        email_structure = {
            'email' : user.email,
            'subject' : subject,
            'preview_text' : preview_text,
            'article_url' : article_url,
            'html_content' : html_content,
            'plain_text_content' : plain_text_content
        }
        
        # Putting the email structure in the queue
        mail_queue.put(email_structure)
    
    for i in range(max_worker_threads):
        
        # Creating the worker threads
        workerThread = Thread(target = send_custom_mails)

        # Setting the worker threads as daemon threads
        workerThread.daemon = True
        workerThread.start()
    
        
    