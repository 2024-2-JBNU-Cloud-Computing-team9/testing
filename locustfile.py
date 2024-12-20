from locust import HttpUser, task, between, TaskSet
import base64

def encode_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

content_image = encode_image("./kurukuru(1).jpg")
style_image = encode_image("./sunset.jpg")
alpha = 0.5

class UserBehavior(TaskSet):
    @task
    def post_request(self):
        url = "/images"
        headers = {"Content-Type": "application/json"}
        payload = {
            "content_image": content_image,
            "style_image": style_image,
            "alpha": alpha
        }
        
        response = self.client.post(url, headers=headers, json=payload)
        

class LocustUser(HttpUser):
    host = "http://capstone-ALB-625441092.us-east-1.elb.amazonaws.com:8080"
    tasks = [UserBehavior]
    wait_time = between(10, 15)