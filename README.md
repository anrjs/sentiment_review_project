# 🏨 숙박 리뷰 감정 분석 프로젝트

영문 숙소 리뷰 텍스트를 기반으로 감정을 **긍정(1)** 또는 **부정(0)**으로 자동 분류하는 머신러닝 프로젝트입니다.  
전처리부터 TF-IDF 기반 모델 학습까지 로컬 환경에서 수행하였고, 이후 BERT 기반 분류 모델로 확장 예정입니다.

---

## 📦 데이터 출처

본 프로젝트에 사용된 원본 리뷰 데이터는 Kaggle에서 공개된 [515K Hotel Reviews Data](https://www.kaggle.com/datasets/datafiniti/hotel-reviews) 를 기반으로 합니다.

> ⚠️ 데이터셋은 용량 제한으로 인해 GitHub 저장소에는 포함되어 있지 않습니다.

### 📥 데이터 다운로드 및 저장 위치

- Kaggle에서 다운로드 후, 다음 위치에 저장해주세요:

```plaintext
dataset/
├── Hotel_Reviews.csv             # 원본 데이터셋
└── Hotel_Reviews_CLEAN.csv       # 전처리 완료 데이터셋
````

> ✅ 전처리 완료 파일(`Hotel_Reviews_CLEAN.csv`, 약 242MB)은 아래 링크에서도 받을 수 있습니다:
> 🔗 [Google Drive 다운로드](https://drive.google.com/file/d/1HvTmHWmatG7jtiXfM1bIC4WPM9Fcb_jV/view?usp=sharing)

---

## 📁 프로젝트 구조

```plaintext
sentiment_review_project/
├── dataset/
│   ├── Hotel_Reviews.csv
│   └── Hotel_Reviews_CLEAN.csv
│
├── preprocessing/
│   ├── preprocess.py                 # spaCy 기반 전처리 스크립트
│   └── preprocess_demo.ipynb         # 전처리 결과 확인용 노트북
│
├── tfidf_model/
│   └── train_tfidf.ipynb             # TF-IDF + Logistic Regression 학습/분석
│
├── bert_model/
│   └── train_bert.ipynb              # (작성 예정) BERT 기반 분류기
│
├── figures/                          # 시각화 이미지 저장 폴더
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ 사용 기술

* **언어**: Python 3.10.5
* **텍스트 전처리**: `spaCy`, `contractions`, 사용자 정의 부정어·감정어 처리
* **모델링**: `scikit-learn` (TF-IDF + Logistic Regression)
* **시각화**: `matplotlib`, `seaborn`
* **환경**: Windows + VSCode / 추후 GPU 환경(Elice Cloud) 기반 확장 예정

---

## 💻 Setup & Installation

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. spaCy 영어 모델 설치 (최초 1회)

```bash
python -m spacy download en_core_web_sm
```

---

## 🚀 실행 방법

### 1. 전처리 실행

```bash
python preprocessing/preprocess.py
```

* 전처리 결과는 `dataset/Hotel_Reviews_CLEAN.csv`로 저장됨

### 2. 모델 학습/분석 실행

* 다음 노트북을 실행해 학습 및 인사이트 도출

```plaintext
tfidf_model/train_tfidf.ipynb
```

> 추가 전처리 전략은 `preprocessing/preprocess_demo.ipynb`에서 실험 가능

---

## 📈 모델 성능 (TF-IDF + Logistic Regression)

* Accuracy: **92.87%**
* F1 Score: **92.87%**
* Confusion Matrix:

```
[[66846  5671]
 [ 6243 88367]]
```

---

## 📊 주요 인사이트

본 프로젝트는 호텔 리뷰 데이터를 바탕으로 감성 분석을 수행하였으며, Logistic Regression 모델을 통해 다음과 같은 인사이트를 도출했습니다.

### 🔻 부정 리뷰 인사이트

* `rude`, `poorly`, `disappointing` → 직원 태도 및 서비스에 대한 불만
* `noisy`, `small`, `limited`, `weak` → 공간 및 시설에 대한 지적
* `expensive`, `not`, `lack` → 가격 대비 만족도 하락

📌 **개선 제안**:
직원 CS 교육 강화, 객실 리모델링 및 방음 개선, 가격 정책 재검토

### 🔺 긍정 리뷰 인사이트

* `friendly`, `helpful` → 직원 친절도에 대한 긍정 평가
* `clean`, `comfortable`, `quiet`, `spacious` → 쾌적한 숙소 환경
* `location`, `convenient`, `stylish` → 위치 및 디자인 만족도

📌 **활용 방안**:
긍정 키워드 기반 마케팅, 핵심 경쟁력 강화 요소 파악

> 📌 인사이트 및 단어 시각화 결과는 `train_tfidf.ipynb` 내 Markdown 셀로 정리되어 있습니다.

---

## 🧠 향후 계획

* `bert_model/train_bert.ipynb`: BERT 기반 분류기 학습 예정
* TF-IDF vs BERT 성능 비교
* 추가 전처리 전략 고도화 (ex. 사용자 정의 감정 사전 확장, 오타 보정 등)

---

## 📝 참고사항

* `.gitignore`를 통해 다음 파일/폴더는 Git에서 제외됨:

  * `venv/`, `__pycache__/`, `.ipynb_checkpoints/`
* 시각화 이미지는 추후 `figures/` 폴더에 저장 예정