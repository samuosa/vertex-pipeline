import os
import time
import pytest
import requests

# Test suite for Cloud Run Image Generation API
# Requires TARGET_URL to be set, otherwise uses the dev/staging endpoint placeholder
BASE_URL = os.getenv("TARGET_URL", "https://staging-image-generation-service-url.run.app")

@pytest.fixture
def base_payload():
    return {
        "prompt": "A beautiful landscape, photorealistic, 8k, highly detailed",
        "negative_prompt": "blurry, low quality, distorted",
        "num_inference_steps": 30,
        "guidance_scale": 7.5
    }

def test_generation_success(base_payload):
    """
    Test that a valid generation request returns 200 OK and an image URL.
    This also validates that the endpoint responds within the cold-start + generation time bounds.
    """
    start_time = time.time()
    response = requests.post(f"{BASE_URL}/generate", json=base_payload, timeout=60)
    duration = time.time() - start_time
    
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}: {response.text}"
    
    data = response.json()
    assert "image_url" in data, "Response JSON is missing 'image_url'"
    assert data["image_url"].startswith("https://"), "image_url should be a valid HTTPS URL"
    
    # Assert duration is within the SLA (cold start + generation < 45 seconds)
    assert duration < 45.0, f"Response took too long: {duration} seconds (SLA < 45s)"

def test_generation_missing_prompt(base_payload):
    """
    Test that omitting the required 'prompt' field results in a 400 Bad Request.
    """
    payload = base_payload.copy()
    del payload["prompt"]
    
    response = requests.post(f"{BASE_URL}/generate", json=payload, timeout=10)
    
    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    # Optionally assert that the error message mentions 'prompt'
    assert "error" in response.json(), "Response should contain an error field"

def test_generation_invalid_parameters(base_payload):
    """
    Test that providing out-of-bounds parameters results in a 400 Bad Request.
    """
    payload = base_payload.copy()
    payload["num_inference_steps"] = 1000  # Assume max is 50-100 to prevent DOS/timeouts
    
    response = requests.post(f"{BASE_URL}/generate", json=payload, timeout=10)
    
    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"

def test_generation_wrong_method():
    """
    Test that using a GET request correctly throws a 405 Method Not Allowed.
    """
    response = requests.get(f"{BASE_URL}/generate", timeout=10)
    
    assert response.status_code == 405, f"Expected 405 Method Not Allowed, got {response.status_code}"
