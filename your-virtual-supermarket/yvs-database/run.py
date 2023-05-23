from subprocess import Popen

if __name__ == '__main__':
    auth_app_process = Popen(['python', 'auth.py'])
    supermarket_app_process = Popen(['python', 'supermarketapp.py'])

    # Wait for both processes to finish
    auth_app_process.wait()
    supermarket_app_process.wait()
