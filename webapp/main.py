from flask import (
    Flask,
    render_template,
    request,
    escape,
    session,
    copy_current_request_context,
)
from src.vsearch import search4letters
from src.DBcm import (
    UseDatabase,
    ConnectionError,
    CredentialsError,
    SQLError,
)
from src.decorator import check_logged_in
from threading import Thread
import logging
import configparser


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

config = configparser.ConfigParser()
config.read("config/.env", encoding="utf-8-sig")

HOST_DATABASE = config["DATABASE"]["HOST"]
USER_DATABASE = config["DATABASE"]["USER"]
PASSWORD_DATABASE = config["DATABASE"]["PASSWORD"]
NAME_DATABASE = config["DATABASE"]["DATABASE"]


app = Flask(__name__)

app.secret_key = "YouWillNeverGuess"


@app.route("/search4", methods=["POST"])
def do_search() -> str:
    """Extract the posted data; perform the search; return results."""

    @copy_current_request_context
    def log_request(req, res: str) -> None:
        """Log details of the web request and the results."""
        with UseDatabase(
            host=HOST_DATABASE,
            user=USER_DATABASE,
            password=PASSWORD_DATABASE,
            database=NAME_DATABASE,
        ) as cursor:
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(
                _SQL,
                (
                    req.form["phrase"],
                    req.form["letters"],
                    req.remote_addr,
                    req.user_agent.browser,
                    res,
                ),
            )

    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        logging.info(f"Logging failed with this error: {str(err)}")
    return render_template(
        "results.html",
        the_title=title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results,
    )


@app.route("/")
@app.route("/entry")
def entry_page():
    """Display this webapp's HTML form."""
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web!"
    )


@app.route("/viewlog")
@check_logged_in
def view_the_log() -> str:
    try:
        with UseDatabase(
            host=HOST_DATABASE,
            user=USER_DATABASE,
            password=PASSWORD_DATABASE,
            database=NAME_DATABASE,
        ) as cursor:
            _SQL = """
                select 
                    phrase, 
                    letters, 
                    ip, 
                    browser_string, 
                    results 
                from 
                    log
            """

            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = (
            "Phrase",
            "Letters",
            "Remote_addr",
            "User_agent",
            "Results",
        )

        return render_template(
            "viewlog.html",
            the_title="View Log",
            the_row_titles=titles,
            the_data=contents,
        )

    except ConnectionError as err:
        logging.info(f"Is your database switched on? Error: {str(err)}")
    except CredentialsError as err:
        logging.info(f"User-id/Password issues. Error: {str(err)}")
    except SQLError as err:
        logging.info("Is your query correct? Error: {str(err)}")
    except Exception as err:
        logging.info(f"Something went wrong: {str(err)}")
    return render_template(
        "message.html",
        the_title="There was an error, try again!",
    )


@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True
    title = "You are now logged in."
    return render_template("message.html", the_title=title)


@app.route("/logout")
def do_logout() -> str:
    session.pop("logged_in")
    title = "You are NOT Logged in."
    return render_template("message.html", the_title=title)


if __name__ == "__main__":
    app.run(debug=True)
