# 🏨 숙박 리뷰 감정 분석 프로젝트

📦 데이터 출처
본 프로젝트에 사용된 원본 리뷰 데이터는 Kaggle에서 공개된 515K Hotel Reviews Data 를 기반으로 합니다.

데이터셋은 용량 제한으로 인해 GitHub 저장소에는 포함되어 있지 않습니다.

프로젝트 실행을 위해서는 해당 데이터를 Kaggle에서 다운로드 후 dataset/Hotel_Reviews.csv로 저장해 주세요.

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

## 📦 전처리 데이터셋 (용량 초과로 외부 제공)

> `Hotel_Reviews_CLEAN.csv` (약 242MB)는 GitHub 단일 파일 제한(100MB)을 초과하여,  
> 아래 링크를 통해 다운로드할 수 있습니다.

🔗 [전처리 데이터셋 다운로드 (Google Drive)](https://drive.google.com/file/d/1HvTmHWmatG7jtiXfM1bIC4WPM9Fcb_jV/view?usp=sharing)

다운로드한 후 `dataset/` 폴더에 넣어주세요:
dataset/
├── Hotel_Reviews.csv
└── Hotel_Reviews_CLEAN.csv ← (다운로드 파일)

📈 모델 성능 (TF-IDF + LogisticRegression)
Accuracy: 92.87%

F1 Score: 92.87%

Confusion Matrix:
[[66846  5671]
 [ 6243 88367]]

## 📊 주요 인사이트

본 프로젝트는 호텔 리뷰 데이터를 바탕으로 감성 분석을 수행하였으며, Logistic Regression 모델을 통해 다음과 같은 인사이트를 도출했습니다:

- **부정 리뷰 인사이트**
  - `rude`, `poorly`, `disappointing` 등은 직원 태도와 서비스에 대한 불만을 반영
  - `noisy`, `small`, `limited` 등은 시설 및 공간 제약에 대한 지적
  - `expensive`, `not`, `lack` 등은 가격 대비 낮은 만족도를 의미

- **긍정 리뷰 인사이트**
  - `friendly`, `helpful` 등은 친절한 서비스에 대한 긍정적 평가
  - `clean`, `comfortable`, `quiet` 등은 청결하고 쾌적한 환경에 대한 만족
  - `location`, `convenient`, `stylish` 등은 입지 조건과 디자인에 대한 호평

이러한 결과는 향후 서비스 개선 및 마케팅 전략 수립에 직접적인 참고가 될 수 있습니다.
상세 분석결과 및 인사이트는 train_tfidf.ipynb에 Markdown으로 제공되어 있습니다.

💡 향후 계획
bert_model/train_bert.ipynb 내에서 BERT 기반 분류 모델 학습 예정

모델 비교: TF-IDF vs BERT

추가 전처리 전략 검토: 데이터 정합성 보정, 단어 사전 확장 등

📝 참고사항
venv/, __pycache__/, .ipynb_checkpoints/ 등은 .gitignore로 관리 중입니다.

BERT 모델 학습은 GPU 환경(Elice Cloud)에서 별도로 진행 예정입니다.