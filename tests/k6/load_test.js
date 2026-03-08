import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  // Simulate a burst of traffic to evaluate scale-to-zero cold starts and throughput
  stages: [
    { duration: '30s', target: 5 },  // Ramp-up to 5 concurrent requests
    { duration: '1m', target: 5 },   // Stay at 5 concurrent requests (warm state)
    { duration: '30s', target: 15 }, // Spike to 15 to trigger autoscaling of new L4 GPU instances
    { duration: '1m', target: 0 },   // Ramp-down to 0 to observe scale-to-zero behavior
  ],
  thresholds: {
    // 95% of requests must complete within 45s (Cold starts can take 15-30s + generation time)
    http_req_duration: ['p(95)<45000'],
    // Ensure less than 5% error rate
    http_req_failed: ['rate<0.05'],
  },
};

const BASE_URL = __ENV.TARGET_URL || 'https://staging-image-generation-service-url.run.app';

export default function () {
  const payload = JSON.stringify({
    prompt: "A futuristic cyberpunk city skyline at sunset, highly detailed, 8k resolution, trending on artstation",
    negative_prompt: "blurry, low quality, distorted",
    num_inference_steps: 30,
    guidance_scale: 7.5
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
    timeout: '60000', // 60s timeout to account for cold starts and inference
  };

  const res = http.post(`${BASE_URL}/generate`, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response has image URL': (r) => {
      try {
        const body = JSON.parse(r.body);
        return body && body.image_url && body.image_url.startsWith('https://');
      } catch (e) {
        return false;
      }
    },
    'cold start handled (or warm response)': (r) => r.timings.duration < 45000,
  });

  sleep(1);
}
