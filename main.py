from app import create_app
import os


def main():
    app = create_app()
    app.run(debug=os.getenv('FLASK_DEBUG'), host=os.getenv(
        'FLASK_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT'))


if __name__ == '__main__':
    main()
