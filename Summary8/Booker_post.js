import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10, 
  duration: '10s',
  // iterations: 100
//    stages: [
//        { duration: '10s', target: '10'},
//        { duration: '10s', target: '20'},
//        { duration: '10s', target: '0'},
//    ]
};

export function setup() {
    const authUrl = 'https://restful-booker.herokuapp.com/auth';
    const authPayload = JSON.stringify({
        username: 'admin',
        password: 'password123' 
    });
    
    const authParams = {
        headers: { 'Content-Type': 'application/json' },
    };

    const res = http.post(authUrl, authPayload, authParams);
    
    check(res, { 'auth status was 200': (r) => r.status === 200 });

    const token = res.json('token'); 
    
    return { token: token };
}

export default function (data) {
    const url = 'https://restful-booker.herokuapp.com/booking';
    
    const payload = JSON.stringify({
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": true,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    });

    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Authorization': `Bearer ${data.token}` 
        },
    };

    let res = http.post(url, payload, params);

    check(res, { 'status was 200': (r) => r.status === 200 });

    sleep(1);
}