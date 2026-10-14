# ✍️ 손글씨 숫자 인식 프로그램 (Handwritten Digit Recognition)

사용자가 마우스로 그린 0~9까지의 숫자를 인공지능이 인식하여 결과를 알려주는 데스크톱 및 웹 애플리케이션입니다. 

## 🛠 Tech Stack
- **Language:** Python, HTML/CSS/JavaScript (Web Version)
- **AI Library:** TensorFlow, Keras, TensorFlow.js
- **GUI & Image Processing:** Tkinter, Pillow
- **Dataset:** MNIST Dataset

## ✨ Key Features
- **데스크톱 앱 (Python/Tkinter):** 캔버스에 숫자를 그리면 학습된 모델이 즉시 예측 결과와 신뢰도(%)를 출력합니다.
- **웹 버전 (TensorFlow.js):** 파이썬 환경 없이 인터넷 브라우저상에서 작동하는 가벼운 웹 애플리케이션입니다.
- **자동화:** `.bat` 파일을 통해 터미널 명령어 입력 없이 더블클릭만으로 가상환경을 불러오고 프로그램을 실행할 수 있습니다.
- **CLAUDE.md 활용:** 프로젝트 규칙과 구조를 분리하여 관리합니다.

## 🚀 How to Run
1. `desktop_version` 폴더 내의 `run_digit_recognition.bat` 파일을 더블클릭하여 실행합니다.
2. 캔버스에 마우스로 숫자를 그리고 **[Recognize]** 버튼을 클릭합니다.