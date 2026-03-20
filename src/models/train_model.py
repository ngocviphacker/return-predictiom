from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

from src.config import TEST_SIZE, RANDOM_STATE, THRESHOLD

def train_all_models(df_model):
    X = df_model.drop('Return', axis=1)
    y = df_model['Return']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    smote = SMOTE(random_state=RANDOM_STATE)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    # Logistic
    lr = LogisticRegression(max_iter=200)
    lr.fit(X_train, y_train)

    y_prob = lr.predict_proba(X_test)[:, 1]
    y_pred = (y_prob > THRESHOLD).astype(int)

    print("=== Logistic ===")
    print(classification_report(y_test, y_pred))
    print("ROC:", roc_auc_score(y_test, y_prob))
    print("PR:", average_precision_score(y_test, y_prob))

    # Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    y_prob = rf.predict_proba(X_test)[:, 1]
    y_pred = (y_prob > THRESHOLD).astype(int)

    print("=== Random Forest ===")
    print(classification_report(y_test, y_pred))

    # XGBoost
    xgb = XGBClassifier(eval_metric='logloss')
    xgb.fit(X_train, y_train)

    y_prob = xgb.predict_proba(X_test)[:, 1]
    y_pred = (y_prob > THRESHOLD).astype(int)

    print("=== XGBoost ===")
    print(classification_report(y_test, y_pred))