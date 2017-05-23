async function fetchTimeout(url, options, timeout, error) {
    let timer = new Promise((resolve, reject) => {
        setTimeout(reject, timeout, error);
    });
    let request = new Promise((resolve, reject) => {
        fetch(url, options)
        .then(response => resolve(response))
        .catch(reject)
    });

    return Promise.race([timer, request]);
}

const RESTAPI_URL = 'http://localhost:5000';
const REST_ERRORS = {
    FETCH_TIMEOUT: '===== Fetch Request Timed Out ====='
}

export async function loginByJWT(email, password) {
    var payload = {
        email: email,
        password: password
    };

    // Edit this to be a reasonable value.
    const TIMEOUT = 3000;

    let response = await fetchTimeout(
        RESTAPI_URL + '/auth/login',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        },
        TIMEOUT,
        REST_ERRORS.FETCH_TIMEOUT
    )
    .then((response) => {
        if (response.ok) {
            return response.json();
        }
        throw Error(response.statusText);
    }).then((json) => {
        console.log(Object.keys(json));
        let token = json.auth_token;
        console.log("Received token: " + token);
        return {
            loggedin: true,
            token: token
        };
    }).catch((error) => {
        console.log("Sorry, bad credentials.");
        return {
            loggedin: false,
            token: ''
        };
    });

    return response;
}

export async function getUserData(token) {
    // Edit this to be a reasonable value.
    const TIMEOUT = 3000;

    let response = await fetchTimeout(
        RESTAPI_URL + '/auth/status',
        {
            method: 'GET',
            headers: {
                Authorization: 'Bearer ' + token,
            },
        },
        TIMEOUT,
        REST_ERRORS.FETCH_TIMEOUT
    )
    .then((response) => {
        if (response.ok) {
            return response.json();
        }
        // TODO: Figure out how to get Flask responseObject JSON response.
        throw Error(response.statusText);
    }).then((json) => {
        console.log(Object.keys(json));
        let status = json.status;
        let data = json.data;
        console.log("Response status: " + status);
        console.log("Data: " + JSON.stringify(data));
        return {
            success: status == 'success' ? true : false,
            data: '{\n  data: ' + data.user_id +
                '\n  email: ' + data.email +
                '\n  admin: ' + data.admin +
                '\n  registered_on: ' + data.registered_on + '\n}'
        };
    }).catch((error) => {
        console.log("Failed to get user data." + error);
        return {
            success: false,
            data: error.toString()
        };
    });

    return response;
}
