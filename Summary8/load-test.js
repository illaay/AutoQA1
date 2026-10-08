import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  // vus: 10, 
  // duration: '20s',
  // iterations: 100
   stages: [
       { duration: '10s', target: '10'},
       { duration: '10s', target: '20'},
       { duration: '10s', target: '0'},
   ]
};

export default function () {
  let res = http.post('https://test.k6.io/');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}