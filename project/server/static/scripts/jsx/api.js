var loginByJWT = require('../utils.js').loginByJWT;
var getUserData = require('../utils.js').getUserData;

var DemoFetch = React.createClass({
    // sets initial state
    getInitialState: function () {
        return {
            email: this.props.email,
            password: this.props.password,
            token: '',
            userdata: ''
        };
    },

    render: function () {
        return (
            <div>
                <input
                    type="text"
                    value={this.state.email}
                    onChange={(event) => {
                        this.setState({ email: event.target.value }, () => {
                            console.log('email updated: ' + this.state.email);
                        });
                    }}
                    placeholder="email"
                />
                <input
                    type="text"
                    value={this.state.password}
                    onChange={(event) => {
                        this.setState({ password: event.target.value }, () => {
                            console.log('password updated: ' + this.state.password);
                        });
                    }}
                    placeholder="password"
                />
                <br/>
                <p>current token: {this.state.token}</p>
                <br/>
                <button
                    onClick={async () => {
                        console.log('submit to login');
                        result = await loginByJWT(this.state.email, this.state.password);
                        if (result.loggedin) {
                            console.log('success!');
                            this.setState({ token: result.token }, () => {
                                console.log('token updated: ' + this.state.token);
                            });
                        } else {
                            console.log('failure!');
                        }
                    }}
                >
                    login
                </button>
                <hr/>
                <p>result:</p>
                <pre>{this.state.userdata}</pre>
                <button
                    onClick={async () => {
                        console.log('go get some user data');
                        result = await getUserData(this.state.token);
                        this.setState({ userdata: result.data });
                    }}
                >
                    get user data
                </button>
                <hr/>
                <form action="/methodview/template" method="post">
                    <button name="foo" value="bar">Test Post to MethodView</button>
                </form>
            </div>
        )
    }

});

ReactDOM.render(
    <DemoFetch email='test1@test.com' password='12345' />,
    document.getElementById('main')
);