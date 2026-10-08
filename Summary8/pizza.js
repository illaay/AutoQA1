import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10000,
  duration: '10s',
  // iterations: 100
//    stages: [
//        { duration: '10s', target: '10'},
//        { duration: '10s', target: '20'},
//        { duration: '10s', target: '0'},
//    ]
};

export default function (data) {
    const url = 'https://quickpizza.grafana.com/api/pizza';

    const payload = JSON.stringify({
    "maxCaloriesPerSlice": 1000,
    "mustBeVegetarian": false,
    "excludedIngredients": [],
    "excludedTools": [],
    "maxNumberOfToppings": 5,
    "minNumberOfToppings": 2,
    "customName": ""
});

    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Authorization': 'Token Rq0A93vkSYdGateq'
        },
    };

    let res = http.post(url, payload, params);

    check(res, { 'status was 200': (r) => r.status === 200 });

    sleep(1);
}