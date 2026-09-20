import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

# 1. MNIST 데이터세트 로드 및 모델 학습
print("Initializing Handwritten Digit Recognition System...")
print("Loading MNIST dataset...")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Building neural network model...")
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Training model...")
model.fit(x_train, y_train, epochs=5)

# 2. GUI 애플리케이션 클래스
class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognition")
        self.root.geometry("400x500")

        # 캔버스 설정
        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white", cursor="cross")
        self.canvas.pack(pady=20)
        self.canvas.bind("<B1-Motion>", self.draw)

        # 내부 이미지 객체 생성 (사용자 입력 저장용)
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), "white")
        self.draw_engine = ImageDraw.Draw(self.image)

        # 버튼 프레임
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.btn_clear = tk.Button(btn_frame, text="Clear", command=self.clear_canvas)
        self.btn_clear.pack(side="left", padx=10)

        self.btn_recognize = tk.Button(btn_frame, text="Recognize", command=self.recognize_digit)
        self.btn_recognize.pack(side="left", padx=10)

        # 결과 출력 라벨
        self.label_result = tk.Label(self.root, text="Draw a digit and click 'Recognize'", font=("Arial", 14))
        self.label_result.pack(pady=10)
        
        self.label_confidence = tk.Label(self.root, text="Draw a digit (0-9) in the white area above\nThen click Recognize to see the prediction.", font=("Arial", 10))
        self.label_confidence.pack()

    def draw(self, event):
        x, y = event.x, event.y
        r = 8  # 브러시 두께
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")
        self.draw_engine.ellipse([x-r, y-r, x+r, y+r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), "white")
        self.draw_engine = ImageDraw.Draw(self.image)
        self.label_result.config(text="Draw a digit and click 'Recognize'", fg="black")
        self.label_confidence.config(text="Draw a digit (0-9) in the white area above\nThen click Recognize to see the prediction.", fg="black")

    def recognize_digit(self):
        # 이미지를 28x28 크기로 리사이징하고 반전 (MNIST 데이터와 동일한 형태로 변환)
        img_resized = self.image.resize((28, 28))
        img_array = np.array(img_resized)
        img_array = 255 - img_array  # 흰 바탕 검은 글씨 -> 검은 바탕 흰 글씨로 반전
        img_array = img_array / 255.0  # 정규화
        img_array = img_array.reshape(1, 28, 28)

        # 예측
        predictions = model.predict(img_array)
        predicted_digit = np.argmax(predictions)
        confidence = np.max(predictions) * 100

        # 결과 업데이트
        self.label_result.config(text=f"Predicted Digit: {predicted_digit}", fg="red")
        self.label_confidence.config(text=f"Confidence: {confidence:.2f}%", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()