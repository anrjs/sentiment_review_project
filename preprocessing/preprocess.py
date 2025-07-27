# ✅ [0] 라이브러리 설치 및 spaCy 모델 다운로드
#!pip install spacy
#!python -m spacy download en_core_web_sm
#!pip install contractions

# ✅ [1] 라이브러리 불러오기 및 spaCy 초기화
import pandas as pd
import re
import spacy

# spaCy 영어 모델 로딩
nlp = spacy.load("en_core_web_sm")

# ✅ [2] 데이터 불러오기
df = pd.read_csv("dataset/Hotel_Reviews.csv")
print("데이터 개수:", len(df))
df.head()

# ✅ [3] 감정별 리뷰 분리 및 통합
# 긍정 리뷰
pos_df = df[df['Positive_Review'].str.strip().str.lower() != 'no positive'][['Positive_Review']]
pos_df = pos_df.rename(columns={'Positive_Review': 'Review'})
pos_df['Sentiment'] = 1

# 부정 리뷰
neg_df = df[df['Negative_Review'].str.strip().str.lower() != 'no negative'][['Negative_Review']]
neg_df = neg_df.rename(columns={'Negative_Review': 'Review'})
neg_df['Sentiment'] = 0

# 병합 및 정리
df_clean = pd.concat([pos_df, neg_df], ignore_index=True)
df_clean.dropna(subset=['Review'], inplace=True)
df_clean = df_clean.reset_index(drop=True)

print("최종 리뷰 개수:", len(df_clean))
df_clean.sample(5)

# ✅ [4] 리뷰 텍스트 전처리 (spaCy 기반)
# ✅ [4-1]: 축약형 복원 및 리스트 생성 (검증 포함)
import pandas as pd
import contractions
import re
from tqdm import tqdm

# ✅ 1단계: 깨진 축약형 복원 함수 정의
def fix_broken_contractions(text):
    broken_patterns = [
        (r"\b(can)\s+t\b", r"\1't"),
        (r"\b(won)\s+t\b", r"\1't"),
        (r"\b(don)\s+t\b", r"\1't"),
        (r"\b(doesn)\s+t\b", r"\1't"),
        (r"\b(didn)\s+t\b", r"\1't"),
        (r"\b(shouldn)\s+t\b", r"\1't"),
        (r"\b(wasn)\s+t\b", r"\1't"),
        (r"\b(weren)\s+t\b", r"\1't"),
        (r"\b(couldn)\s+t\b", r"\1't"),
        (r"\b(i)\s+m\b", r"\1'm"),
        (r"\b(it)\s+s\b", r"\1's"),
        (r"\b(you)\s+re\b", r"\1're"),
        (r"\b(we)\s+re\b", r"\1're"),
        (r"\b(they)\s+re\b", r"\1're"),
        (r"\b(who)\s+s\b", r"\1's"),
        (r"\b(that)\s+s\b", r"\1's"),
    ]
    for pattern, repl in broken_patterns:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

# ✅ 원본 텍스트 로딩
texts = df_clean["Review"].fillna("").tolist()

# ✅ 1단계 적용: 깨진 축약형 복원
fixed_contraction_texts = [fix_broken_contractions(text) for text in tqdm(texts, desc="🔧 깨진 축약형 복원")]

# ✅ 2단계 적용: contractions 패키지 복원
expanded_texts = [contractions.fix(text) for text in tqdm(fixed_contraction_texts, desc="🔧 표준 축약형 복원")]

# ✅ 결과 저장
df_clean["Expanded_Review"] = expanded_texts
print("✅ 축약형 복원 완료!")

# ✅ 검증 (예시 키워드 확인)
keywords = [
    ("don t", "don't"), ("wasn t", "wasn't"), ("can t", "can't"),
    ("it s", "it's"), ("i m", "i'm"), ("won t", "won't")
]

for wrong, fixed in keywords:
    wrong_count = sum(wrong in t.lower() for t in texts)
    fixed_count = sum(fixed in t.lower() for t in df_clean["Expanded_Review"])
    print(f"🔍 '{wrong}' 포함 원문 수: {wrong_count}")
    print(f"✅ '{fixed}' 복원 후 포함 수: {fixed_count}")
    print("-" * 50)

# ✅ 예시 비교 출력
SAMPLE_INDEXES = [9, 14, 24, 25, 50]
for idx in SAMPLE_INDEXES:
    print(f"[Index {idx}]")
    print("원문  :", texts[idx])
    print("복원후:", df_clean['Expanded_Review'][idx])
    print("------------------------------------------------------------")

# ✅ [4-2]: spaCy 전처리 + 부정어 및 감정 단어 보존 + 저장
import spacy
from tqdm import tqdm

# ✅ 사전 정의: 보존할 단어들
NEGATION_WORDS = {"not", "no", "never", "nor"}
SENTIMENT_WORDS = {"good", "bad", "clean", "dirty", "friendly", "unfriendly", "helpful", "rude"}

# ✅ 처리 대상
texts = df_clean['Expanded_Review'].fillna("").tolist()

# ✅ 결과 저장용 리스트
processed_texts = []

print("🔧 spaCy pipe 전처리 시작...")

# ✅ pipe 방식으로 빠르게 처리
for doc in tqdm(nlp.pipe(texts, batch_size=2000, n_process=1), total=len(texts)):
    try:
        tokens = [
            token.lemma_.lower()
            for token in doc
            if (
                not token.is_stop
                or token.text.lower() in NEGATION_WORDS
                or token.text.lower() in SENTIMENT_WORDS
            )
            and not token.is_punct
            and not token.is_space
        ]
        processed_texts.append(' '.join(tokens))
    except Exception as e:
        processed_texts.append("")
        print("⚠️ 전처리 오류:", e)

# ✅ 결과 저장
df_clean["Processed"] = processed_texts

# ✅ CSV로 저장
output_path = "dataset/Hotel_Reviews_CLEAN.csv"
df_clean.to_csv(output_path, index=False)

print("✅ 전처리 완료 및 저장 완료!")
print(df_clean[["Expanded_Review", "Processed"]].sample(3))

# 🧪 [4-3]: 전처리 품질 검증 코드
# ✅ 검증 대상 단어 목록
NEGATION_WORDS = {"not", "no", "never", "nor"}
SENTIMENT_WORDS = {"good", "bad", "clean", "dirty", "friendly", "unfriendly", "helpful", "rude"}

# ✅ 부정어 포함 리뷰 수 확인
print("🔍 부정어 포함 리뷰 수:")
for word in NEGATION_WORDS:
    count = df_clean["Processed"].str.contains(rf"\b{word}\b", case=False).sum()
    print(f"{word:>6}: {count}")

print("\n🔍 감정 단어 포함 리뷰 수:")
for word in SENTIMENT_WORDS:
    count = df_clean["Processed"].str.contains(rf"\b{word}\b", case=False).sum()
    print(f"{word:>10}: {count}")

# ✅ 예시 추출
print("\n🔍 예시 리뷰 (부정어/감정어 포함):")
mask = df_clean["Processed"].str.contains(r"\b(no|not|never|good|bad|helpful|friendly|dirty)\b", case=False)
print(df_clean[mask][["Expanded_Review", "Processed"]].sample(5, random_state=42))