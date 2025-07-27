# 🏨 숙박 리뷰 감정 분석 프로젝트

Dataset - Kaggle 515k reviews

영문 숙소 리뷰 텍스트를 기반으로 감정을 **긍정(1)** 또는 **부정(0)**으로 자동 분류하는 머신러닝 프로젝트입니다.
전처리부터 TF-IDF 기반 모델 학습까지 로컬 환경에서 수행하였고, 이후 BERT 기반 분류 모델로 확장 예정입니다.

---

## 📁 프로젝트 구조

sentiment_review_project/
├── dataset/
│   ├── Hotel_Reviews.csv             # 원본 데이터셋
│   └── Hotel_Reviews_CLEAN.csv       # 전처리 완료 데이터셋
│
├── preprocessing/
│   ├── preprocess.py                 # spaCy 기반 전처리 함수
│   └── preprocess_demo.ipynb         # 전처리 결과 및 예시 확인용 노트북
│
├── tfidf_model/
│   └── train_tfidf.ipynb             # TF-IDF + Logistic Regression 학습/평가 코드
│
├── bert_model/
│   └── train_bert.ipynb              # (작성 예정) BERT 기반 분류기 학습 코드
│
├── figures/                          # 시각화 결과 저장 (추후 BERT 학습 결과 포함)
│
├── README.md
├── requirements.txt
└── .gitignore

## ⚙️ 사용 기술

- **언어**: Python 3.10.5
- **텍스트 전처리**: `spaCy`, `contractions`, 사용자 정의 감정/부정어 리스트
- **모델링**: `scikit-learn` (TF-IDF + Logistic Regression)
- **환경**: Windows + VSCode, 추후 Elice Cloud(GPU) 활용 예정

---

## 💻 Setup & Installation

```bash
# 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate            # (Windows)
# 또는
source venv/bin/activate        # (Mac/Linux)

# 필수 라이브러리 설치
pip install -r requirements.txt

# spaCy 영어 모델 다운로드 (최초 1회만 실행)
python -m spacy download en_core_web_sm

## 🚀 실행 방법

1. 가상환경 활성화
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
패키지 설치

bash

pip install -r requirements.txt
데이터 전처리

bash

python preprocessing/preprocess.py
모델 학습/평가 (TF-IDF)
→ tfidf_model/train_tfidf.ipynb 실행

📈 모델 성능 (TF-IDF + LogisticRegression)
Accuracy: 92.87%

F1 Score: 92.87%

Confusion Matrix:
[[66846  5671]
 [ 6243 88367]]

💡 향후 계획
bert_model/train_bert.ipynb 내에서 BERT 기반 분류 모델 학습 예정

모델 비교: TF-IDF vs BERT

추가 전처리 전략 검토: 데이터 정합성 보정, 단어 사전 확장 등

📝 참고사항
venv/, __pycache__/, .ipynb_checkpoints/ 등은 .gitignore로 관리 중입니다.

BERT 모델 학습은 GPU 환경(Elice Cloud)에서 별도로 진행 예정입니다.