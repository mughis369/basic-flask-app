from flask import Flask, render_template, request, url_for, redirect




logging.basicConfig(

    level=logging.DEBUG,
    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)


    # region routes


    @app.route('/')
    def home():
        return render_template('home.html')


    @app.route('/account')
    def account():
        return render_template('account.html')


    @app.route('/orders', methods=["GET", "POST", "DELETE"])
    def orders():
        return render_template('orders.html')


    @app.route('/market_watch')
    def market_watch():
        return render_template('watch.html')

    # endregion


    return app


if __name__ == "__main__":
   app = create_app()
   app.run(host='0.0.0.0', debug=True)









if __name__=="__main__":
    app.run(debug=True)