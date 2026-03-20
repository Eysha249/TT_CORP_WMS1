from app.database.db_setup import create_tables, insert_sample_users
from app.gui.main_window import run_app

def main():
    #prepare database
    create_tables()
    insert_sample_users()

    # start GUI
    run_app()


if __name__ == "__main__":
    run_app()


